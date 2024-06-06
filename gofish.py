
import pygame
import random

from pygame import event

from pygameRogers import Game, TextRectangle, Alarm
from pygameRogers import Room
from pygameRogers import GameObject


g = Game(640, 480)
g.timer = Alarm()

Black = (0, 0, 0)
White = (255, 255, 255)

simpleBackground = g.makeBackground(Black)
gameFont = g.makeFont("Arial", 38)

r1 = Room("Game", simpleBackground)
g.addRoom(r1)
r2 = Room("go fish", simpleBackground)
g.addRoom(r2)
r3 = Room("Player 1 victory room", simpleBackground)
g.addRoom(r3)
r4 = Room("Player 2 victory room", simpleBackground)
g.addRoom(r4)

diamondpics = []
for i in range(2, 15):
    diamondpics.append(g.makeSpriteImage("cards\DIAMONDS" + str(i) + ".jpg"))

clubpics = []
for i in range(2, 15):
    clubpics.append(g.makeSpriteImage("cards\CLUBS" + str(i) + ".jpg"))

heartpics = []
for i in range(2, 15):
    heartpics.append(g.makeSpriteImage("cards\HEARTS" + str(i) + ".jpg"))

spadepics = []
for i in range(2, 15):
    spadepics.append(g.makeSpriteImage("cards\SPADES" + str(i) + ".jpg"))

topcard = g.makeSpriteImage("cards/TOP.jpg")

class War(TextRectangle):
    def __init__(self, text, xpos, ypos, font, textcolor, buttonwidth, buttonheight, buttoncolor):
        TextRectangle.__init__(self, text, xpos, ypos, font, textcolor, buttonwidth, buttonheight, buttoncolor)
        self.timer = Alarm()

    def update(self):
        self.checkMousePressedOnMe(event)

        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            g.nextRoom()
            self.mouseHasPressedOnMe = False

class card(GameObject):
    def __init__(self, picture, value, suit, xPos, yPos):
        GameObject.__init__(self, picture)

        self.value = value
        self.suit = suit  # H, D, C, S
        self.original = picture

    def compare(self, card2):
        if self.value > card2.value:
            return self
        elif self.value < card2.value:
            return card2
    
    def __str__(self):
        return str(self.value) + self.suit


class deck(GameObject):
    def __init__(self, picture, xpos, ypos):
        GameObject.__init__(self, picture)

        self.rect.x = xpos
        self.rect.y = ypos

        self.deck = []

        for i in range(0, len(diamondpics)):
            c = card(diamondpics[i], i + 2, "D", 0, 0)
            self.deck.append(c)

        for i in range(0, len(clubpics)):
            c = card(clubpics[i], i + 2, "C", 0, 0)
            self.deck.append(c)

        for i in range(0, len(heartpics)):
            c = card(heartpics[i], i + 2, "H", 0, 0)
            self.deck.append(c)

        for i in range(0, len(spadepics)):
            c = card(spadepics[i], i + 2, "S", 0, 0)
            self.deck.append(c)

        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) > 0:
            c = self.deck[0]
            del self.deck[0]

        if len(self.deck) == 0:
            self.kill()

        return c


    def __str__(self):

        s = ""
        for card in self.deck:
            s = s + str(card) + " "
        return s

class playerhand(GameObject):
    def __init__(self, handsize, xpos, ypos):
        GameObject.__init__(self)
        self.rect.x = xpos
        self.rect.y = ypos
        
        self.hand = []
        self.cardsinhand = 0
        occurence = 0
        appearing_values_list=[]
        self.score = 0

    def update(self):
        score.setText("Score: " + str(self.score))

    def takecard(self, card):
        self.hand.append(card)
        self.cardsinhand = self.cardsinhand + 1

    def __str__(self):
        s = ""
        for card in self.hand:
            s = s + str(card) + " "
            # s = "playerhand:/n" + s + "/n"
        return s
    
    def win(self):
        if self.score == 7:
            g.nextRoom()
        else:
            pass

    def scorecard(self):
        valuelist = []
        for i in range(0, len(self.hand)):
            l = self.hand[i].value
            valuelist.append(l)
            selectionSort(valuelist)
            print(valuelist)
        for i in range(0,len(valuelist)):
            num = valuelist[i]
            if valuelist.count(num) == 4:
                m = valuelist[i]
                print(m)
                self.score = self.score + 1
                print("p1 score", self.score)
                for i in range(0, len(self.hand)):
                    n = self.hand[i]
                    if m == n.value:
                        del self.hand[i]
                        break
                for i in range(0, len(self.hand)):
                    o = self.hand[i]
                    if m == o.value:
                        del self.hand[i]
                        break
                for i in range(0, len(self.hand)):
                    p = self.hand[i]
                    if m == p.value:
                        del self.hand[i]
                        break
                for i in range(0, len(self.hand)):
                    q = self.hand[i]
                    if m == q.value:
                        del self.hand[i]
                        break
                break
            
            
                
            else:
                pass
    
    def createcardobject(self):
        for i in range (0, len(self.hand)):
            pcard=self.hand[i]
            pcard.rect.x=25*i
            pcard.rect.y=275
            pcard.image=pcard.original
            
            r2.addObject(pcard)
        
def selectionSort(nlist):
    small=0
    smallindex=0
    for i in range (0,len(nlist)):
        small=nlist[i]
        for j in range (i, len(nlist)):
            if nlist[j] <= small:
                small = nlist[j]
                smallindex= j
        nlist[smallindex] = nlist[i]
        nlist[i]=small

def selectionSortcard(p):
    small = 0
    smallindex = 0
    for i in range(0,len(p)):
        small = p[i].value
        for j in range (0, len(p)):
            if p[j].value <= small:
                small = p[j].value
                smallindex = j
        p[smallindex] = p[i]
        p[i] = small
        

            
class playerhand2(GameObject):
    def __init__(self,handsize, xpos, ypos):
        GameObject.__init__(self,)
        self.rect.x = xpos
        self.rect.y = ypos

        self.hand = []
        self.cardsinhand = 0
        self.picked2 = []
        self.score = 0

    def update(self):
        score2.setText("Score: " + str(self.score))
        
    def takecard(self, card):
        self.hand.append(card)
        self.cardsinhand = self.cardsinhand + 1
        

    def play(self):
        b = 0
        a = random.randint(2,14)
        print(a)
        for i in range (0,len(p.hand)):
            g = p.hand[i]
            if int(g.value) == int(a):
                self.picked2.append(g)
                del p.hand[i]
                b = 1
                break
            else:
                pass         
        for i in range (0,len(p.hand)):
            h = p.hand[i]
            if int(h.value) == int(a):
                self.picked2.append(h)
                del p.hand[i]
                break
            else:
                pass
        for i in range (0,len(p.hand)):
            j = p.hand[i]
            if int(j.value) == int(a):
                self.picked2.append(j)
                del p.hand[i]
                break
            else:
                pass
        for i in range (0,len(p.hand)):
            k = p.hand[i]
            if int(k.value) == int(a):
                self.picked2.append(k)
                del p.hand[i]
                break
            else:
                pass
        p2.scorecard()
        p2.win()
        
        if int(g.value) != int(a) and len(deck.deck) > 0:
            zcard = deck.deal()
            p2.takecard(zcard)
            print("kys", p)
            print("kys", p2)
        if int(g.value) != int(a) and len(deck.deck) == 0:
            print("kys", p)
            print("kys", p2)
            
        if b == 1 and len(p.hand) > 1:
            p2.picked2list()
            print(p)
            print(p2)
            p2.play()
        if b == 2  and len(p.hand) == 1:
            print(p)
            print(p2)
        else:
            pass
        
    def picked2list(self):
         for i in range (0, len(self.picked2)):
            f = self.picked2[0]
            p2.takecard(f)
            p2.createcardobject()
            del self.picked2[0]
        

    def __str__(self):
        s = ""
        for card in self.hand:
            s = s + str(card) + " "
            # s = "playerhand:/n" + s + "/n"
        return s
    
    def scorecard(self):
        valuelist = []
        for i in range(0, len(self.hand)):
            l = self.hand[i].value
            valuelist.append(l)
            selectionSort(valuelist)
            print(valuelist)
            
        for i in range(0,len(valuelist)):
            num = valuelist[i]
            if valuelist.count(num) == 4:
                m = valuelist[i]
                print(m)
                self.score = self.score + 1
                print("p2 score", self.score)
                for i in range(0, len(self.hand)):
                    n = self.hand[i]
                    if m == n.value:
                        del self.hand[i]
                        break
                for i in range(0, len(self.hand)):
                    o = self.hand[i]
                    if m == o.value:
                        del self.hand[i]
                        break
                for i in range(0, len(self.hand)):
                    p = self.hand[i]
                    if m == p.value:
                        del self.hand[i]
                        break
                for i in range(0, len(self.hand)):
                    q = self.hand[i]
                    if m == q.value:
                        del self.hand[i]
                        break
                break
            
            
                
            else:
                pass
    def win(self):
        if self.score == 7:
            g.nextRoom()
            g.nextRoom()
        else:
            pass
    
    def createcardobject(self):
        for i in range (0, len(self.hand)):
            rcard = self.hand[i]
            rcard.rect.x = 25*i
            rcard.rect.y = 75
            rcard.image = topcard
            r2.addObject(rcard)
    

class DealButton(TextRectangle):

    def __init__(self, text, xPos, yPos, font, textcolor, buttonwidth, buttonheight, buttoncolor):
        TextRectangle.__init__(self, text, xPos, yPos, font, textcolor, buttonwidth, buttonheight, buttoncolor)

    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            for i in range(0, 7):
                acard = deck.deal()
                p.takecard(acard)
                bcard = deck.deal()
                p2.takecard(bcard)
            self.mouseHasPressedOnMe = False
            print(p)
            print(p2)
            p.createcardobject()
            p2.createcardobject()
            
            checkbutton_2 = CheckButton("2", 15, 400, gameFont, Black, 30, 30, White, 2)
            r2.addObject(checkbutton_2)

            checkbutton_3 = CheckButton("3", 50, 400, gameFont, Black, 30, 30, White, 3)
            r2.addObject(checkbutton_3)

            checkbutton_4 = CheckButton("4", 85, 400, gameFont, Black, 30, 30, White, 4)
            r2.addObject(checkbutton_4)

            checkbutton_5 = CheckButton("5", 120, 400, gameFont, Black, 30, 30, White, 5)
            r2.addObject(checkbutton_5)

            checkbutton_6 = CheckButton("6", 155, 400, gameFont, Black, 30, 30, White, 6)
            r2.addObject(checkbutton_6)

            checkbutton_7 = CheckButton("7", 190, 400, gameFont, Black, 30, 30, White, 7)
            r2.addObject(checkbutton_7)

            checkbutton_8 = CheckButton("8", 225, 400, gameFont, Black, 30, 30, White, 8)
            r2.addObject(checkbutton_8)

            checkbutton_9 = CheckButton("9", 15, 435, gameFont, Black, 30, 30, White, 9)
            r2.addObject(checkbutton_9)

            checkbutton_10 = CheckButton("10", 50, 435, gameFont, Black, 30, 30, White, 10)
            r2.addObject(checkbutton_10)

            checkbutton_J = CheckButton("J", 85, 435, gameFont, Black, 30, 30, White, 11)
            r2.addObject(checkbutton_J)

            checkbutton_Q = CheckButton("Q", 120, 435, gameFont, Black, 30, 30, White, 12)
            r2.addObject(checkbutton_Q)

            checkbutton_K = CheckButton("K", 155, 435, gameFont, Black, 30, 30, White, 13)
            r2.addObject(checkbutton_K)

            checkbutton_A = CheckButton("A", 190, 435, gameFont, Black, 30, 30, White, 14)
            r2.addObject(checkbutton_A)
            
            self.kill()
        else:
            pass

class CheckButton(TextRectangle):

    def __init__(self, text, xPos, yPos, font, textcolor, buttonwidth, buttonheight, buttoncolor, value):
        TextRectangle.__init__(self, text, xPos, yPos, font, textcolor, buttonwidth, buttonheight, buttoncolor)
        
        self.value = value
        
    def check(self):
        
        for i in range (0,len(p2.hand)):
            c = p2.hand[i]
            picked=[]
            if c.value == self.value:
                picked.append(c)
                del p2.hand[i]
                break
        if c.value != self.value and len(deck.deck) > 0:
            acard = deck.deal()
            p.takecard(acard)
            p2.play()
        if c.value != self.value and len(deck.deck) == 0:
            p2.play()
            
        for i in range (0,len(p2.hand)):
            d = p2.hand[i]
            if d.value == self.value:
                picked.append(d)
                del p2.hand[i]
                break
            else:   
                pass
        for i in range (0,len(p2.hand)):
            e = p2.hand[i]
            if e.value == self.value:
                picked.append(d)
                del p2.hand[i]
                break
            else:   
                pass
        for i in range (0,len(p2.hand)):
            f = p2.hand[i]
            if f.value == self.value:
                picked.append(d)
                del p2.hand[i]
                break
            else:   
                pass
        for i in range (0, len(picked)):
            e = picked[0]
            p.takecard(e)
            del picked[0]
        if len(p2.hand) == 0:
            acard = deck.deal()
            p.takecard(acard)
            p2.play()
        p.scorecard()
        p.createcardobject()
        p.scorecard()
        p.win()
        print("nanana", p)
        print("banana", p2)

            
    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            self.check()
            self.mouseHasPressedOnMe = False        

class textbox(TextRectangle):

    def __init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor):
        TextRectangle.__init__(self, text, xPos, yPos, font, textColor, buttonWidth, buttonHeight, buttonColor)


score = textbox("", 400, g.windowHeight - 100, gameFont, Black, 150, 40, White)
r2.addObject(score)

score2 = textbox("", 400, g.windowHeight - 450, gameFont, Black, 150, 40, White)
r2.addObject(score2)

Warbutton = War("Start", 250, g.windowHeight - 250, gameFont, Black, 150, 40, White)
r1.addObject(Warbutton)

deck = deck(topcard, 287, 175)
r2.addObject(deck)

p = playerhand(52, 400, 30)
r2.addObject(p)

p2 = playerhand2(52, 400, 300)
r2.addObject(p2)

dealbutton = DealButton("Deal", 400, g.windowHeight - 250, gameFont, Black, 150, 40, White)
r2.addObject(dealbutton)

winbutton1 = textbox("P1 Wins", 400, g.windowHeight - 250, gameFont, Black, 150, 40, White)
r3.addObject(winbutton1)

winbutton2 = textbox("P2 Wins", 400, g.windowHeight - 250, gameFont, Black, 150, 40, White)
r4.addObject(winbutton2)

g.start()
while g.running:
    dt = g.clock.tick(60)
    for event in pygame.event.get():

        # Check for [x]
        if event.type == pygame.QUIT:
            g.stop()

    # Update All objects in Room
    g.currentRoom().updateObjects()

    # Render Background to the game surface
    g.currentRoom().renderBackground(g)

    # Render Objects to the game surface
    g.currentRoom().renderObjects(g)

    # Draw everything on the screen
    pygame.display.flip()

pygame.quit()

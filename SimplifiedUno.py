import random

class UnoCard:

    def __init__(self, c, n):
        self.color = c
        self.number = n

    def __str__(self):
        return self.color + ' ' + str(self.number)

    def canplay(self, other):
        if (self.number == other.number) or (self.color == other.color):
            return True
        return False

class CollectionOfUnoCards:

    def __init__(self):
        self.l = []

    def addCard(self, c):
        self.l.append(c)

    def makeDeck(self, deck):
        for num in range(1, 10):
            for color in ['Yellow', 'Red', 'Blue', 'Green']:
                newcard = UnoCard(color, num)
                deck.addCard(newcard)
                deck.addCard(newcard)

    def shuffle(self):
        for k in range(1, 100):
            i = random.randint(0, 71)
            j = random.randint(0, 71)
            self.l[i], self.l[j] = self.l[j], self.l[i]

    def __str__(self):
        col_str = ''
        for i in range(0, len(self.l)):
            col_str = col_str + ' ' + str(self.l[i]) +','
        return col_str

    def getNumCards(self):
        return len(self.l)

    def getTopCard(self):
        return self.l[-1]

    def canPlay(self, c, deck):
        for i in range(0, len(deck.l)):
            if deck.l[i].canplay(c):
                return True
        return False

    def playableCard(self,c,deck):
        for i in range(0, len(deck.l)):
            if deck.l[i].canplay(c):
                return i


    def getCard(self, index):
        i = index
        return self.l[i]

class Uno:

    def __init__(self):
        self.deck = CollectionOfUnoCards()
        self.deck.makeDeck(self.deck)
        self.deck.shuffle()
        self.hand1 = CollectionOfUnoCards()
        self.hand2 = CollectionOfUnoCards()
        self.lastPlayedCard =self.deck.l[-1]
        self.deck.l.pop(-1)

        for i in range(1, 8):
            a = self.deck.getTopCard()
            self.deck.l.pop(-1)
            self.hand1.addCard(a)

        for i in range(1, 8):
            a = self.deck.getTopCard()
            self.deck.l.pop(-1)
            self.hand2.addCard(a)

    def playTurn(self,player):
        if (player.canPlay(self.lastPlayedCard,player)):
            a=player.playableCard(self.lastPlayedCard,player)
            self.lastPlayedCard=player.l[a]
            player.l.pop(a)
        else:
            b=self.deck.l[-1]
            player.addCard(b)
            self.deck.l.pop(-1)

    def playGame(self):
        while(len(self.deck.l)>0):
            print("Player1's turn")

            print('Player1= ',self.hand1)
            print('lastPlayedCard= ',self.lastPlayedCard)

            if(self.hand1.canPlay(self.lastPlayedCard,self.hand1)):
                self.playTurn(self.hand1)
                print('Player1 discards: ', self.lastPlayedCard)
                print('Player1= ', self.hand1)

                if(len(self.hand1.l)==0):
                    print('PLAYER 1 HAS WON THE GAME')
                    break
            else:
                self.playTurn(self.hand1)
                print('there is no card that can be discarded')
                print('Player1= ', self.hand1)

            print("Player2's turn")
            print('Player2= ', self.hand2)
            print('lastPlayedCard= ',self.lastPlayedCard)

            if (self.hand2.canPlay(self.lastPlayedCard, self.hand2)):
                self.playTurn(self.hand2)
                print('Player2 discards: ', self.lastPlayedCard)
                print('Player2= ', self.hand2)

                if(len(self.hand2.l)==0):
                    print('PLAYER 2 HAS WON THE GAME')
                    break
            else:
                self.playTurn(self.hand2)
                print('there is no card that can be discarded')
                print('Player2= ', self.hand2)

        if(self.deck.l==0):
            print('Game finished in a tie')


my_game = Uno()
my_game.playGame()


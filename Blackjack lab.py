import random




class Card():

    def __init__(self, suit, face, value=None):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return "{} of {} ".format(self.face, self.suit)
    #
    def __repr__(self):
        return self.__str__()


class Deck():

    def __init__(self):
        self.hopper = self.createDeck()
        random.shuffle(self.hopper)


    def createDeck(self):
        card_face = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        card_suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

        deck = []

        for suit in card_suit:
            for face, value in card_face.items():
                deck.append(Card(suit, face, value))
        return deck


    def __str__(self):
        return "{}".format(self.hopper)



class Hand():

    def __init__(self):
        self.cards = []


    def addCard(self, deck):
        self.cards.append(deck.pop())
        # self.cards.append(deck.pop())

    def cardValues(self):
        total = 0
        A = False

        for c in self.cards:
            if c.value == 1:
                A = True
                total += c.value
            else:
                total += c.value

        if A and total + 10 <= 21:
            total += 10
        return total

    def __str__(self):
        return "{}".format(self.cards)






class deal():
    def __init__(self):


deck = Deck()
hand = Hand()
hand.addCard(deck.hopper)
hand.addCard(deck.hopper)

dealerHand = Hand()
# dealerShown = dealerHand[0]
dealerHand.addCard(deck.hopper)
dealerHand.addCard(deck.hopper)


print(hand)
print('player: ' + str(hand.cardValues()))
print(dealerHand)

print("dealer shows: {} ".format(dealerHand.cards[1]))


playing = True

playerStay = False
dealerStay = False
playerHandSize = 2
dealerHandSize = 2

while playing:

    if playerStay == False:
        query = input('Hit or Stay: ').lower()
        if query == 'h':
            hand.addCard(deck.hopper)
            print(hand)
            print('player: ' + str(hand.cardValues()))
            handTotal = hand.cardValues()
            playerHandSize += 1
        if query == 's':
            handTotal = hand.cardValues()
            playerStay = True
        if handTotal > 21:
            print("You busted!!!!")
            break
    if dealerStay == False:
        dealerTotal = dealerHand.cardValues()
        if dealerTotal <= 16:
            dealerHand.addCard(deck.hopper)
            dealerHandSize += 1
            dealerTotal = dealerHand.cardValues()
            if dealerHandSize == 5:
                if dealerTotal <= 21:
                    print('dealer got {} in 5 cards '.format(dealerTotal))
                    print("dealer wins")
                    break

            print("dealer hits")
            # print('dealer: ' + str(dealerHand.cardValues()))
            print("dealer shows: {} ".format(dealerHand.cards[1:]))
            if dealerTotal > 21:
                # print('player: {}'.format(handTotal))
                print("Dealer busted! You win!")
                print("dealer shows: {} ".format(dealerHand.cards))

                break
        if dealerTotal > 16:
            if dealerTotal > 21:
                print('player: {}'.format(handTotal))
                print("Dealer busted! You win!")
                break
            else:
                dealerStay = True
                print('dealer stays')
        if dealerTotal > 21:
            print('player: {}'.format(handTotal))
            print("Dealer busted! You win!")
            break

    if playerStay == True and dealerStay == True:
        if handTotal > dealerTotal:
            print("players's {} beats {}! ".format(handTotal, dealerTotal))

            print('you win!')
            break
        else:
            print("dealer's {} beats {}! ".format(dealerTotal, handTotal))
            print("dealer wins")
            break




            # again = input('Play again? y or n: ')
#     if again == y:
#         continue
#         break
#     else:



    # again = input('Play again? Y or N: ')
    # if again == N:
    #     playing = False

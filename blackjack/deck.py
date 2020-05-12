class Deck:
    def __init__(self):
        self.__cards = []
        self.__creation_date = datetime.date.today()
        for value in range(1, 14):
            for suit in SUIT:
                self.__cards.append(BlackjackCard(suit, value))

    def get_cards(self):
        self.__cards

class Shoe:
    def __init__(self, number_of_deck):
        self.__cards = []
        self.__number_of_deck = number_of_deck
        self.create_shoe()
        self.shuffle()

    def create_shoe(self):
        for decks in range(0, self.__number_of_deck):
            self.__cards.extend(Deck().get_cards())

    import random

    def shuffle(self):
        card_count = self.__cards.length
        for i in range(0, card_count):
            j = random.randrange(0, card_count -i -1)
            self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

    def deal_card(self):
        if self.__cards.size() == 0:
            create_shoe()
        return self.__cards.remove(0)

## Card objects

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
Card().__dict__

queen_of_diamonds = Card(1, 12)
queen_of_diamonds.__dict__

## Class attributes

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


card1 = Card(2, 11)
print(card1)


## comparing cards

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __gt__(self, other):
        # check the suits
        if self.suit > other.suit:
            return True
        else:
            if self.rank > other.rank:
                return True
            return False

  #  def cmp(self, other):
  #      (self > other) - (self < other)  이거 두줄이 아마 과제?? 부분일거임.

card1 = Card(2, 11)
card2 = Card(1, 11)
print(card1)
print(card2)
print(card1 > card2)
print(card1 < card2)
print(card1 == card2)


## decks

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


deck = Deck()
print(deck)


## add, remove, shuffle, and sort


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop() # 하나 뽑아주는 메소드.. .pop

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num): # 플레이어(hand)들에게 몇장씩 나눠줄 꺼냐
        for i in range(num):
            hand.add_card(self.pop_card())


## inheritance

class Hand(Deck): # 상속받는거.. Deck 부모... Deck이라는 클래스? 에잇는걸 다 쓸 수 있게 해줌
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


hand = Hand('new hand')
print(hand.cards)
print(hand.label)

import random
print(deck)
deck = Deck()
deck.shuffle()
card = deck.pop_card()
hand.add_card(card)
print(hand)


## debugging

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


hand = Hand()
print(find_defining_class(hand, 'shuffle'))

import random

deck = Deck()
deck.shuffle()

hand = Hand()

deck.move_cards(hand, 5)
print(hand)

## 과제설명

#2번 리스트 메쏘드 sort 를 사용해서 Deck 에 있는 카드들을 정렬하는 Deck 메쏘드 sort를 작성하세요. sort 는 정렬 순서를 정하기 위해 정의한 __cmp__ 메쏘드를 사용합니다.
# ? 하 이거 교수님이 cmp 메소드 없어졋다고 햇던거 같은데.. 파이썬 3에는 ... 밑에 한거아님. 그냥 위에 예제 복붙한거. 다시해보기
class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop() # 하나 뽑아주는 메소드.. .pop
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, hand, num): # 플레이어(hand)들에게 몇장씩 나눠줄 꺼냐
        for i in range(num):
            hand.add_card(self.pop_card())
deck = Deck()
print(deck)

#   3번 두 개의 매개변수, 패를 든 사람의 수와 패당 카드 수,를 받아서 새 Hand 객체들을 만들고, 패마다 적당한 수의 카드를 나눈 다음,
#  Hand 객체의 리스트를 돌려주는 Deck 이 메쏘드 deal_hands를 작성하세요.
class Hand(Deck): # 상속받는거.. Deck 부모... Deck이라는 클래스? 에잇는걸 다 쓸 수 있게 해줌
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop() # 하나 뽑아주는 메소드.. .pop
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, hand, num): # 플레이어(hand)들에게 몇장씩 나눠줄 꺼냐
        for i in range(num):
            hand.add_card(self.pop_card())
    def deal_hands(self, pnum,cnum):
        deal = {}
        for i in range(pnum):
            deal['hand'+str(i)] = Hand()
            self.move_cards(deal['hand'+str(i)], cnum)
        print(deal.keys())
        return deal
deck = Deck()
deck.shuffle()
deal = deck.deal_hands(4,5)
for i in range(len(deal)):
    print('hand'+str(i),'\n', deal['hand'+str(i)],'\n')

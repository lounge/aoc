import os, sys
from collections import Counter

rank = '23456789TJQKA' 
rank2 = 'J23456789TQKA' 

hands = [[], [], [], [], [], [], []]

def q2(lines):
    for line in lines:
        hand = line.split()[0]
        bet = line.split()[1]
        cards = Counter(hand).most_common()
        card_dict = dict(cards)

        if "J" in card_dict:
            jokers = card_dict.pop("J")
            if len(card_dict) == 0:
                card_dict["A"] = jokers
            else:
                card_dict[list(card_dict)[0]] += jokers
            hand = [hand, list(card_dict.items())]
        else:
            hand = [hand, cards]

        first = hand[1][0][1]
        second = hand[1][1][1] if len(cards) > 1 and len(hand[1]) > 1 else None

        hand.append(bet)
        group(first, second, hands, hand, bet)
    
    ordered_hands = sort_order(hands)

    score = 0
    for i, s in enumerate(ordered_hands):
        score += int(s[2]) * (i + 1);

    print(score)


def q1(lines):
    for line in lines:
        hand = line.split()[0]
        bet = line.split()[1]

        cards = Counter(hand).most_common()
        first = cards[0][1]
        second = cards[1][1] if len(cards) > 1 else None

        group(first, second, hands, hand, bet)
    
    ordered_hands = sort_order(hands)

    score = 0
    for i, s in enumerate(ordered_hands):
        score += int(s[1]) * (i + 1);

    print(score)


def group(first, second, hands, hand, bet) -> list:
    if first == 5:
        hands[6].append((hand, bet))
    elif first == 4:
        hands[5].append((hand, bet))
    elif first == 3 and second == 2:
        hands[4].append((hand, bet))
    elif first == 3 and second == 1:
        hands[3].append((hand, bet))
    elif first == 2 and second == 2:
        hands[2].append((hand, bet))
    elif first == 2:
        hands[1].append((hand, bet))
    else:
        hands[0].append((hand, bet))
    
def sort_order(hands) -> list:
    clean_hands = [x for x in hands if x]

    for i, hand in enumerate([x for x in clean_hands if x]):
        clean_hands[i] = sort_hands(hand)
 
    return [item for sublist in clean_hands for item in sublist]

def sort_hands(type: list) -> list:
   return sorted(type, key=lambda hand: [rank2.index(card) for card in hand[0]])

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    lines = file.readlines()
    q1(lines)
    q2(lines)


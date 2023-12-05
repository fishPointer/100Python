game = True
turn = True

import random

hand_P1 = []
hand_PC = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def aceflip(hand):
    for n in range(len(hand)):
        if hand[n] == 11:
            hand[n] = 1


def checkbust(hand):
    if sum(hand) > 21:
        aceflip(hand)
    if sum(hand) > 21:
        return True
    else:
        return False


def deal_card(hand):
    card = random.choice(cards)
    hand.append(card)


def printhands():
    print(f"Player Hand: {hand_P1} - Total: {sum(hand_P1)}")
    print(f"PC Hand: {hand_PC} - Total: {sum(hand_PC)}")


while game:
    print("Starting Hand...")
    deal_card(hand_P1)
    # hand_P1.append(11) # debug
    deal_card(hand_P1)
    deal_card(hand_PC)
    printhands()

    while turn:
        playermove = input("Hit(1) or Pass(2)?: ")
        if playermove == "1":
            print("Hit")
            deal_card(hand_P1)
            if checkbust(hand_P1):
                print("YOU LOSE")
                turn = False
            printhands()

        # could turn this into a recursive function but it's not that deep
        elif playermove == "2":
            print("Pass")
            deal_card(hand_PC)
            printhands()
            if checkbust(hand_PC):
                print("YOU WIN")
                turn = False
            elif sum(hand_PC) > sum(hand_P1):
                print("YOU LOSE")
                turn = False
            elif sum(hand_PC) > 17:
                if sum(hand_PC) == sum(hand_P1):
                    print("DRAW")
                    turn = False
                else:
                    print("YOU WIN")
                    turn = False
            else:
                deal_card(hand_PC)
                printhands()
                if checkbust(hand_PC):
                    print("YOU WIN")
                    turn = False
                elif sum(hand_PC) > sum(hand_P1):
                    print("YOU LOSE")
                    turn = False
                elif sum(hand_PC) > 17:
                    if sum(hand_PC) == sum(hand_P1):
                        print("DRAW")
                        turn = False
                    else:
                        print("YOU WIN")
                        turn = False
                else:
                    deal_card(hand_PC)
                    printhands()
                    if checkbust(hand_PC):
                        print("YOU WIN")
                        turn = False
                    elif sum(hand_PC) > sum(hand_P1):
                        print("YOU LOSE")
                        turn = False
                    elif sum(hand_PC) > 17:
                        if sum(hand_PC) == sum(hand_P1):
                            print("DRAW")
                            turn = False
                        else:
                            print("YOU WIN")
                            turn = False

        else:
            game = False
            turn = False
            print("Error1")

    hand_P1 = []
    hand_PC = []
    playagain = input("Play again? (y=1/n=2): ")
    if playagain == "2":
        game = False
        turn = False
    elif playagain == "1":
        game = True
        turn = True
    else:
        game = False
        turn = False
        print("Error2")

print("Game over")

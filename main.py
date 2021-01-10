import art
import random
import click



############## Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.




def calculate_total_score(cards):
 total_score=0
 for card_value in cards:
      total_score+=card_value

 if total_score>21 and is_ace(cards):
    total_score-=10
    cards.remove(11)
    cards.append(1)
 return total_score

def is_ace(cards):
    for card in cards:
        if card==11:
            return True
def compare_scores(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"



def blackjack():
 user_points = []
 dealer_points = []
 cards_of_players = {}
 start_the_game=True

 should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")



 print(art.logo)
 click.clear()
 user_points.append(random.choice(cards))
 user_points.append(random.choice(cards))
 dealer_points.append(random.choice(cards))
 dealer_points.append(random.choice(cards))
 while start_the_game:
    if should_continue == 'n':
        start_the_game = False
    else:

        cards_of_players["user"]=user_points
        cards_of_players["dealer"]=dealer_points

        user_total=calculate_total_score(cards_of_players["user"])
        dealer_total=calculate_total_score(cards_of_players["dealer"])

        if dealer_total==21 and len(cards_of_players["dealer"])==2:
            print('Dealer has a blackjack.\nYou lose')
            print(f"Your final hand: {cards_of_players['user']}, final score: {user_total}")
            print(f"Computer's final hand: {cards_of_players['dealer']}, final score: {dealer_total}")

            blackjack()

        elif user_total==21 and len(cards_of_players["user"])==2:
            print('User has a blackjack.\nYou win.')
            print(f"Your final hand: {cards_of_players['user']}, final score: {user_total}")
            print(f"Computer's final hand: {cards_of_players['dealer']}, final score: {dealer_total}")

            blackjack()



        print(f'Your cards: {cards_of_players["user"]}, current score: {user_total}')
        print(f"Computer's first card: {cards_of_players['dealer'][0]}")

        user_choice=input("Type 'y' to get another card, type 'n' to pass:")

        if user_choice == 'y':

            user_points.append(random.choice(cards))
            cards_of_players["user"] = user_points
            user_total = calculate_total_score(cards_of_players["user"])


            if user_total>21:
               print(compare_scores(user_total, dealer_total))
               print(f"Your final hand: {cards_of_players['user']}, final score: {user_total}")
               print(f"Computer's final hand: {cards_of_players['dealer']}, final score: {dealer_total}")

               blackjack()



        if user_choice == 'n':
            while dealer_total<17:
                 dealer_points.append(random.choice(cards))
                 cards_of_players["dealer"] = dealer_points
                 dealer_total = calculate_total_score(cards_of_players["dealer"])
            print(f"Your final hand: { cards_of_players['user'] }, final score: {user_total}")
            print(f"Computer's final hand: {cards_of_players['dealer']}, final score: {dealer_total}")
            print(compare_scores(user_total,dealer_total))

            blackjack()




blackjack()
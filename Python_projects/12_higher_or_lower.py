from art2 import logo,vs
from game_data import data
import random
print(logo)

# formate the account data in to printable form
def formate_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_descr},from{account_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

score = 0
#generate a random account from the game data

should_continue = True
account_b = random.choice(data)

while should_continue:
    #Makig account at position B become the next account at position A.
    account_a  = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{formate_data(account_a)}.")

    print(vs)
    print(f"Compare B:{formate_data(account_b)}.")

    #Ask the user to guess
    guess = input("Who has more followers? Type 'A' or 'B'.").lower()

    #check if user is correct.
    #Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # give user feedback on their guess.
    #score keeping
    if is_correct:
        score += 1
        print(f"You are right! current score: {score}")
    else:
        print(f"Sorry, that's wrong! correct answer is: {score}")
        should_continue = False
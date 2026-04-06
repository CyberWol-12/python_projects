from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-3: Whether if new bids need to be added
# TODO-2: Save data into dictionary {name: price}

    # TODO-4: Compare bids in dictionary
def compare_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with highest_bid of {highest_bid}")


bids = {} # empty dict
new_bid = True
while  new_bid:
    name = input("What is your name?")
    bid = int(input("What is your bid:$"))

    bids[name] = bid

    ask_user = input("Is there any other bidders?Type 'yes' or 'no'\n").lower()
    if ask_user == "no":
        new_bid  = False
        compare_highest_bid(bids)
    elif ask_user == 'yes':
        print("\n" * 20)
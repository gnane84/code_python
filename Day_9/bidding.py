

def find_highest_price(biding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in biding_dictionary:
        bind_amount = biding_dictionary[bidder]
        if bind_amount > highest_bid:
            highest_bid = bind_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")

bids = {}
continue_bidding  = True
while continue_bidding:
    name = input("Please enter your name: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue_bidding = input("Would you like to continue? (y/n) \n ").lower()
    if should_continue_bidding == "n":
        continue_bidding = False
        find_highest_price(bids)
    elif should_continue_bidding == "y":
        print("\n" * 25)

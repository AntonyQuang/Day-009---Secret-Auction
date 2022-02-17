#from replit import clear
import art
import os


print(art.logo)

any_other_bidders = True
bidder_exist = False
bidders = {}
winning_bid = 0
winner = ""

def bid_check(bidders) -> [winner, winning_bid]:
    winning_bid = 0
    for bids in bidders:
        if bidders[bids] > winning_bid:
            winning_bid = bidders[bids]
            winner = bids
    print(f"The winner is {winner} with a bid of ${winning_bid}")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while any_other_bidders == True:
    name = input("What is your name?: ")
    while name in bidders:
        print("A bid has already been made in that name!")
        name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid  
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "no":
        any_other_bidders = False
    elif other_bidders == "yes":
        cls()
        
bid_check(bidders)    


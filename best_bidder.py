from replit import clear
from art import logo

bidders = {}
is_there_any = "yes"
def add_member(name, bid):
    bidders[name] = bid
    print(bidders[name])

def maximum():
    max_value = ["",0]
    for key in bidders:
        if int(bidders[key]) > int(max_value[1]):
            max_value [1] = bidders[key]
            max_value[0] = key
    print(max_value)

print(logo)
while is_there_any == "yes":
    name = input("Please Enter your name: ")
    bid = input("Plese Enter the bid amount in dollar: $")
    add_member(name,bid)
    is_there_any = input("Is the any other opponent in auction(Yes or No): ").lower()
    clear()
maximum()    

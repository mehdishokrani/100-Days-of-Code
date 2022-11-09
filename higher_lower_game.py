from game_data import data
import random
from art import logo , vs

TEXT = ""
#make a random choice from data in dame_data
def random_number():
    index_number = random.randint(0, len(data)-1)
    return index_number


#make a record
def new_record():
    record = data[random_number()]
    global TEXT
    if TEXT == record['name'] +  " a " + record['description'] +", from " + record['country']:
        new_record()
    else:
        TEXT = record['name'] +  " a " + record['description'] +", from " + record['country']
    return(record["follower_count"])

right_answer = 0
flag = True

a_record = new_record()
while flag:
    print(logo)
    print(f"Compare A: {TEXT} , follower= {a_record}")
    b_record = new_record()
    print(vs)
    print(f"Against B: {TEXT} , follower= {b_record}")
    
    
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a" and a_record > b_record:
        print("You are right")
        right_answer += 1
    elif answer == "b" and b_record >= a_record:
        print("You are right")
        right_answer += 1
    else:
        print(f"You are WRONG !!!! But total correct answers was {right_answer}")
        flag = False

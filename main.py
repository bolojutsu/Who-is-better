from art import logo, vs
print(logo)
from game_data import data
import random 
score = 0



def data_format(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, {account_description}, {account_country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare 1: {data_format(account_a)}.")
  print(vs)
  print(f"Against 2: {data_format(account_b)}.")
  guess = input("who has more followers? type 'a' or 'b': ").lower()
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  if is_correct:
    score += 1
    print("you are right")
  else:
    game_should_continue = False
    print("game over")
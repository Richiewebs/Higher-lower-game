from art import data
from art import logo
from art import vs
import random
start_game = True
scores = 0
while start_game:
    for _ in range(len(data)):
        print(logo)
        person_one = random.randint(0, len(data)-1)
        print(f"Compare A: {data[person_one]['name']} a {data[person_one]['description']} from {data[person_one]['country']}")
        print(vs)
        person_two = random.randint(0, len(data)-1)
        print(f"Against B: {data[person_two]['name']} a {data[person_two]['description']} from {data[person_two]['country']}")

        followers_one = data[person_one]['follower_count']
        followers_two = data[person_two]['follower_count']

        if followers_one == followers_two:
            person_one = random.randint(0, len(data) - 1) - 5
            person_two = random.randint(0, len(data) - 1) + 10

        more_followers = input("Who has more followers? Type 'A' or 'B': ")
        more_followers = more_followers.upper()
        if more_followers == "A" and followers_one > followers_two:
            scores += 1
            print(f"You're right! Your current score is {scores}")

        elif more_followers == "A" and followers_two > followers_one and scores > 0:
            scores = scores
            print(f"You're wrong! Your Final score is {scores}")
            start_game = False
            break
        elif more_followers == "B" and followers_two > followers_one:
            scores += 1
            print(f"You're right! Your current score is {scores}")

        elif more_followers == "B" and followers_two < followers_one and scores > 0:
            scores = scores
            print(f"You're wrong! Your Final score is {scores}")
            start_game = False
            break
        else:
            scores = 0
            print(f"You're wrong! Your Final score is {scores}")
            start_game = False
            break

    if (more_followers == "A" and followers_two > followers_one and scores == 0) or (
            more_followers == "A" and followers_two > followers_one and scores > 0) or (
            more_followers == "B" and followers_two < followers_one and scores > 0) or (
            more_followers == "B" and followers_two < followers_one and scores == 0):
        start_game = False



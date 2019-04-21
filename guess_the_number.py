import datetime
import json
import random


def scores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def top_scores():
    score_list = scores()
    top_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return top_score_list


def guess_game(difficulty = "e"):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = scores()
    name = input("Your name: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"Name": name, "attempts": attempts, "date": str(datetime.datetime.now()), "difficulty": difficulty})

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it " + name + " - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and difficulty == "e":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and difficulty == "e":
            print("Your guess is not correct... try something bigger")
        else:
            print("Wrong guess")


while True:
    play_game = input ("Choose:\n\ta) Play new game\n\tb) See score list\n\tc) Quit game\n").lower()

    if play_game == "a":
        difficulty = input("Choose difficulty: (e)asy or (h)ard:\n").lower()
        guess_game(difficulty = difficulty)
    elif play_game == "b":
        for score_dict in top_scores():
            print(str(score_dict["Name"]) + ": " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ", difficulty: " + score_dict["difficulty"])
    else:
        break
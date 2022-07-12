import random
guesslist=["Tola", "Feranmi", "Yetunde", "Jeremy", "Frank"]
print(guesslist)

guessindex=random.randint(1,5)
num=int(guessindex) - 1
guessword=guesslist[num]

user = input("Guess a name from my list: ")
if user == guessword:
    print("You guessed right!")
else:
    user = input("Guess again...")

    if user == guessword:
        print("You guessed right!")
    else:
        user = input("Guess again...")

        if user == guessword:
            print("You guessed right!")
        else:
            print("hehe..")
            print("The right name is " + guessword)


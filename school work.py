import random


answer1 = ("Absolutely!")
answer2 = ("No way Jose!") 
answer3 = ("Go on then, Mate!")
print("Welcome to the Magic 8 Ball-game, use it to answer your questions.")
question = input("Ask me for any advice and i'll help you out. Type in your answer and then press Enter for an answer.")
print("shaking.../n" * 4)
choice = random.randint(1,3)
print(choice)
if choice == 1:
    answer=answer1
elif choice == 2:
    answer=answer2
else:
    answer=answer3

print(answer)

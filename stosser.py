import random

variants = ["stone", "scissors", "paper"]
bot = random.choice(variants)
player = input("Choice your variant(stone,scissors or paper -->")
print(f"Choice bot - {bot}")
if bot == "stone" and player == "stone":
    print("Nobody win!")
elif bot == "stone" and player =="paper":
    print("You win!")
elif bot == "stone" and player == "scissors":
    print("Bot win!") #end block "stone bot"
elif bot == "paper" and player == "paper":
    print("Nobody win!")
elif bot == "paper" and player == "scissors":
    print("You win!")
elif bot == "paper" and player =="stone":
    print("Bot win!") #end block "paper bot"
elif bot == "scissors" and player == "scissors":
    print("Nobody win!")
elif bot == "scissors" and player == "paper":
    print("Bot win!")
elif bot == "scissors" and player == "stone":
    print("You win!") #end block "scissors bot"

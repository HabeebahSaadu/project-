import random

def p():
    print("Color Expert: Wine, Emerald, Cream and burgundy!")
    user = input("Choose Wine, Emerald, Cream or burgundy: ").lower()
    
    computer = random.choice(["burgundy", "Cream", "Emerald","Wine" ])
    print(f"computer chose: {computer}")

    if computer == user:
        print("It's fascinating!")
        
    elif (user == "Wine" and computer == "Emerald") or\
         (user == "Cream" and computer == "burgundy") or\
         (user == "burgundy" and computer == "Cream"):
        
        print("You win!")
    else:
        print("You lose")

        

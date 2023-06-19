import random

words=["UMBRELLA","LAPTOP","VS CODE","JUPITER"]
think_word=random.choice(words)


total_chances=7

guessed_word="-"*len(think_word)
while total_chances!=0:
    print(guessed_word)

    guessed_letter=input("guess a letter").upper()
    if guessed_letter in think_word:
        for i in range(len(think_word)):
            if think_word[i]==guessed_letter:
                guessed_word=guessed_word[:i]+guessed_letter+guessed_word[i+1:]
                # print(guessed_word)
        if guessed_word==think_word:
            print("CONGRATULATON YOU WON!!")
            break
    else:
        total_chances-=1
        print("INCORRECT GUESS")
        print("REMAINING CHANCES = ",total_chances)

else:
    print("GAME OVER")
    print("YOU LOOSE!!")
    print("ALL THE CHANCES ARE EXHAUSTED")
    print("CORRECT WORD IS", think_word)




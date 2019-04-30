alpha = False
while alpha == False:
    ## Let the user guess a letter
    letterGuess = input("Guess a letter: ")
    ## If it's longer or shorter than 1 then re-guess
    if len(letterGuess) and letterGuess.isalpha()== 1:
        alpha = True
    else:
        print("Only guess one letter at a time")

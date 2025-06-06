secret_word="girl"
i=1
while i<=3:
    guess=input("Enter your guess:")
    if(guess!=secret_word):
         print("Wrong guess!You have",3-i,"tries left")
         i+=1
    else:
         print("Excellent!The secret word was",guess)
         break
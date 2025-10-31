import random

def guessing_game():
    # start the guessing number game

    print("Welcome to number Guessing Game!----")
    #set the boundaries where  number are limited
    upper_bound = 100
    lower_bound = 0 
     
    guess_count =0 
    guess = None 
    #find the random number between the bounds 
    Gn = random.randint(lower_bound,upper_bound)
    # check whether the ouput is correct according to numbers between bounds    

    while guess != Gn:
        # check whether the ouput is correct according to numbers between bounds 
       try:
        number = int(input(f"take a guess number between {lower_bound} and {upper_bound} : "))

        guess = number

        guess_count +=1

        
        if guess < Gn:
          print("way Too low! try again.")
        elif guess > Gn:
          print("way Too high! try again ")  
        else:
          pass  

       except ValueError as e:
         print(f"caught an valueError as {e} , Please an integer")
         exit()
       except:
        print(e)  

         

    print("Congratulations, you found the guess number\n")
    print(f"number of attempes to find the number is {guess_count}")
        
# ----- Run The Game ------ 
if __name__=='__main__' :
 guessing_game() 








   

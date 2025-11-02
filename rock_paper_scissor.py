import random 

def rps():
    """ make a game where user play against the computer"""

    print("welcome to rock----paper-------scissor!!!!..........")   
    

    attempt = 0

    while True:

        try: 
          choice = int(input("Enter between the choices:-\n 1 for rock\n 2 for papern\n 3 for scissor\n"))
          comp_value = random.randint(1,3)
   

          if choice != comp_value:
            attempt +=1 

          elif choice == comp_value:
            attempt +=1 
            break 

        except ValueError as e:
            print("Please! Enter the valid choice(rock,paper,scissor)........") 
        except TypeError as e :
            print("Please! Enter the valid choice(rock,paper,scissor)........") 
        except :
            print(e)    

         


    print("Congratulation you have won the game!!!!!...........")
    print(f"number of attempts to win against the computer is {attempt}")


if __name__=='__main__':
    rps()        


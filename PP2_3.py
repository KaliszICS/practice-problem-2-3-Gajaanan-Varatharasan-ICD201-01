
def q1(): 
  word = input("In: ")
  if word[-3:] == "ife":
        print("-ives")
  elif word[-2:] == "ey":
        print("-eys")
  elif word[-1] == "y":
        print("-ies")
  else:
        print("-s")

def q2(): 
  number = int(input("In: "))
  if  number > 0:
    print (f"{number} is positive")
  elif number < 0: 
    print (f"{number} is negative")
  elif number == 0:
    print ()
  

def q3():
  number1 = float(input("Input a number: "))
  number2 = float(input("Input a number: "))
  number3 = float(input("Input a number: "))
  if number1 == number2 and number3 == number1:
    print ("Equilateral")
  elif number1 == number2 or number2 == number3 or number1 == number3:
    print ("Isosceles")
  elif number1 + number3 < number2 or number2 + number3 < number1 or number2 + number1 < number3:
    print ("No Triangle") 
  else: 
    print ("Scalene")




#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()

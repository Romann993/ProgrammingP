################## HELLO MUSAT #############################
# print("Musat")
# print("Habab")
#########################################################

#################### VARIABLE #########################
# are like containers or boxes n which you can store information or the data.
## RULE NO 1: You never start with a number
## RULE NO 2: You never put spaces between variable instead _ or camel casing
# first_name or firstName
## RULE NO 3: You never start with a capital letter 
## RULE NO 4: You never use key words.
## Sytax variablename = value


################## DATATYPES ######################
######## INT , FLOAT , STRINGS , BOOLEAN ############



#################### INT ############################
# all non decimal numbers are intigers 
# ......-2,-1,0 , 1 ,2 ....
# Operations: + , - , / , // , * , % , **
# Comparisions: == ,  < , > , <= , >=


# num1 = int(input("Enter any number: "))
# num2 = int(input("Enter any number: "))

# ans = num1 + num2
# print(ans)

# age = int(input("What's your age:?"))
# var = int(input("What's your name:?"))

# arv = age * var
# print(arv)

# prv = int(input("Number: "))
# arv = int(input("Age: "))

# srv = prv / arv
# print(srv)
# arv = int(input("Age:?"))
# srv = int(input("Number:?"))

# irv = arv % srv
# print(irv)


########### FLOAT ######################
##### ALL NUMBERS WITH DECIMALS
##### OPERATION: Same as intigers
##### YOU can also compare them.

# num1 = float(input("Enter any number: "))
# num2 = float(input("Enter any number: "))

# ans = num1 + num2
# print(ans)


# ask for weight and height of the person and then calculate BMI and print the result.

# flormula is wight divideed by height squared

# weg = float(input("Weight in KG:"))
# heg = float(input("Height in Meters:"))

# bmi = weg / (heg ** 2)
# print(bmi)

################### STRING #############################
# anything that is inside '' or "" is a string
# strings are iterable
# size of string  len(variablename)
# len(variable) gives you number of character in string
# indexing variableName[address] 
# slicing 
# concatenation

# take data out of the data string using string slice operation and save it inside different variable first name , last name , Age, City, Salary , Country. Filter the data and print everything with the statement and also calculate the efficiency(salary*age).

#Answer looks like following
#"your name is Habab Idrees. You are 24 year old, you live in Karachi,Pakistan. your salary is 5000.34 and your Efficiency is 120008.16"

# city = Karachi
# Country = Pakistan

# data = "HababIdrees24Karac%hi5000.34Pakis_tan"

# first_name = data[0:5]
# last_name = data[5:11]
# age   = data[11:13]
# city  = data[13:18]+ data[19:21]
# salary = data[21:28]
# country = data[28:33]+ data[34:37]
# efficiency = float(salary) * int(age)
# print(efficiency)

# print("your name is "+first_name+" "+last_name+". You are "+age+" years old, you live in "+city+ " your salary is "+salary+ " your country is "+ country+" your efficiency is "+str(efficiency))


# ask for user name, user weight and user height(as inputs) calculate the bmi of the user and print the result like following

#"Habab your bmi is 21.345"


# name = input("name:")
# weight = float(input("weight:"))
# height = float(input("height:"))
# bmi = weight / height**2
# print(name + " your bmi is " + str(bmi))


# ask for the users name, user's exam total marks and user's exam obtained marks. calculate user percentage and print the result like following.

# Enter your name: Habab
# Enter you total marks: 100
# Enter your obtained marks: 80
# Habab you got 80% marks. 

# name = input("name:")
# x = input("total marks:")
# y = input("obtained marks:")
# p = int(y) / int(x)  * 100
# print(name + " you got " + str(p) + "%" + " marks")



################# CONDITIONS ############################
# import random
# bag = ["Red","Blue","Green","Yellow","Red","Blue","Green","Yellow","Red","Blue","Green","Yellow","Red","Blue","Green","Yellow"]
# ballNumber = random.randint(0,len(bag)-1)
# ball = bag[ballNumber]
# print(ball)
# ##############################################

# if ball == "Red":
#   print("put the ball in the red box")
# elif ball == "Blue":
#   print("put the ball in the blue box")
# elif ball == "Green":
#   print("put the ball in the Green box")
# elif ball == "Yellow":
#   print("put the ball in the  box")


# ask for 2 age input and print the youngest age between the two.
# age1 = int(input('Ask age:'))
# age2 = int(input("Ask age:"))

# if age1 < age2:
#   print(age1)
# else:
#   print(age2)


# ask for the name, weight and height of the person 1  and ask for for the name ,weight and height of person 2 calculate their BMIs and print who's bmi is more than the other one??
# name = input('ask name:')
# weight = float(input('ask weight:'))
# height = float(input("ask height:"))

# name2 = input("ask name:")
# weight2 = float(input("ask weight:"))
# height2 = float(input("ask height:"))

# bmi = (weight / height ** 2)
# bmi2 = (weight2 / height2 ** 2)

# print(bmi)
# print(bmi2)

# if bmi > bmi2:
#   print(name+ " has higher bmi then "+name2)
# elif bmi == bmi2:
#   print(name+ " has same bmi as "+name2)
# else:
#   print(name2+ " has higher bmi then "+name)


# Ask for the name , weight and height of a person calculate his BMI and print his health status.

# name = input("Enter you name name:")
# weight = float(input("Enter your weight in Kg:"))
# height = float(input("Enter your height in Meters:"))
# bmi = (weight / (height ** 2))

# if bmi <= 18.5:
#   print(name + " you are underweight your bmi is " + str(bmi))
# elif 18.5 < bmi <= 24.9:
#   print(name + " your weight is normal your bmi is " + str(bmi) )
# elif 24.9 < bmi < 30.0:
#   print(name + " you are overweight your bmi is " + str(bmi))
# else:
#   print(name + " you are obese your bmi is " + str(bmi))


# Ask for the width input from the user, ask for the height input from the user! print if the shape is square or rectangle based on width and height input.
# width = float(input("Enter width:"))
# height = float(input("Enter height:"))

# if width == height:
#   print("Square")
# else:
#   print("Rectangle")


# ask for the number(int) as user input if the number is divisble  by 5 print "it is divisble by 5" other wise print not divisible by 5
# number = int(input("Enter number:"))

# if number % 5 == 0:
#   print("it is divisible by 5")
# else:
#   print("not divisible by 5")



# ask for the user input(int) as an input print even if the entered number is even other wise print odd.
# number = input(int("Enter number:"))

# if number % 2 == 0:
#   print("even")
# else:
#   print("odd")


# write a simple python code that ask for 3 inputs each input represent the marks of the student in exam. your program should print only the heighest marks.

# mark1 = int(input("Enter mark:"))
# mark2 = int(input("Enter mark:"))
# #mark3 = int(input("Enter mark:"))

# if mark1 > mark2:
#   print("mark1 "+str(mark1))
# elif mark1 == mark2:
#   print("even "+str(mark1))
# else:
#  print("mark2 "+str(mark2))

# mark1 = int(input("Enter mark:"))
# mark2 = int(input("Enter mark:"))
# mark3 = int(input("Enter mark:"))

# if mark1 > mark3 and mark1 > mark2:
#   print("mark 1")
# elif mark2 > mark1 and mark2 > mark3:
#   print("mark 2")
# elif mark3 > mark1 and mark3 > mark2:
#   print("mark 3")

######################### Restricted
# import random
# countries = ["China","India","USA", "France","Brazil", "Pakistan","Canada", "Russia", "Australia"]
# countryName = random.randint(0,len(countries)-1)
# country = countries[countryName]
# # #############################################
# # ### CODE BELOW HERE ########################
# print(country)
# if country == "China" or country == "India" or country == "Pakistan":
#   print("Asia")
# elif country == "USA" or country == "Canada":
#   print("North America")
# elif country == "France":
#   print("Europe")
# elif country == "Brazil":
#   print("South America")
# elif country == "Russia":
#   print("Europe", "Asia")
# elif country == "Australia":
#   print("Australia")

################### FUNCTIONS ######################
### Input ------> Output
# n1 = int(input("Enter your num: "))
# n2 = int(input("Enter your num: "))

# def addition(num1 , num2):
#   result = num1 + num2 
#   return(result)
  

# ans = addition(n1,n2) 
# print(ans)


def substraction(a1,a2):
  result = a1 - a2
  return(result)
  
#ans = substraction(n1,n2)
#print(ans)

def multiplication(b1,b2):
  result = b1 * b2
  return(result)

# ans = multiplication(n1,n2)
# print(ans)

# define a function called division that takes two intiger inputs and divide them to return the result.


def division(c1,c2):
  result = c1 / c2
  return(result)

# ans = division(n1,n2)
# print(ans)

# define a function called math_calculator that takes 3 arguments. first two argument can be intiger or float but the third argument will be a string. for example if i call the function with math_calculator(3,4,"+") it should return 7 or if i call the function math_calculator(4,10,"/") it should return 0.4. Similarly function should be able to perform all the operations we learned in python.
# hint see the last topic and how it can be utilized ????

# num1 = int(input("Enter value:"))
# num2 = int(input("Enter value:"))
# symbol = input("Insert the sybol of opertaion you want to perform")

# def math_calculator(a1,a2,a3):
#   if a3 == "+":
#     return a1 + a2
#   elif a3 == "-":
#     return a1 - a2
#   elif a3 == "*":
#     return a1 * a2
#   elif a3 == "/":
#     return a1 / a2
#   else:
#     return "Invalid symbol"

# a = math_calculator(num1,num2,symbol)
# print(a)
#math_calculator(4,3,"+")  -----> 7

# make a function called BMI calculator that takes two float input calculate bmi and print the result.

# bmi_calculator(61,1.7) -----> 21.123
# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))

# def bmi_calculator(w,h):
#   bmi = w / h**2
#   return bmi

# person1 = bmi_calculator(weight,height)
# print(person1)


# percentage(8, 10) ----> your percentage is 80%
# percentage(15, 30) ----> your percentage is 50%

# percentage = (x / total) * 100


# def percentage(p,b):
#   percent = (p / b ) * 100
#   sent = "your percentage is "+str(percent)+"%"
#   return sent

# p1 = percentage(4,10)
# print(p1)


# discount_calculator(100,35) -----> 65$
# discount_calculator(35,10) -----> 31.5$

# product = float(input("Enter the total price of the product: "))
# discount = float(input("Enter the discount that is offered: "))

# def discount_calculator(product,discount):

#   discount_amount = (discount * product) / 100
#   new_price = product - discount_amount

#   return "your discount is " + str(new_price) + "%"
  
# d3 = discount_calculator(product,discount)
# print(d3)


# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return empty string. 

# firstTwoLastTwo('w3resource') -----> 'w3ce'
# firstTwoLastTwo('Habab') ------> 'Haab'
# firstTwoLastTwo('w3') -------> 'w3w3'
# firstTwoLastTwo('w') --------> ""

#var = input("Enter value:")

def firstTwoLastTwo(var):
  if len(var) > 1:
    f = var[0:2]
    l = var[-2:]     #or var[len(var)-2: ]
    return f + l
  else:
    return ''

#ans = firstTwoLastTwo(var)
#print(ans)

#variableName[startingPoint : EndingPoint]

# Write a function called swapstring which swaps the first and last character of string. 

# # swapString("Lolwa") -------> "aolwL"
# # swapString("Habab") -------> "babaH"
# # swapString("Information") -------> "nnformatioI"

# ans = input("Enter word:")

def swapstring(ans):
  if len(ans) >= 3:
    last = ans[-1]
    first = ans[0]
    middle = ans[1:len(ans)-1]
    return last + middle + first
  else:
    return ""

# d = swapstring(ans)
# print(d)


#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

# adding('abc') --------> 'abcing'
# adding('ab') --------> 'ab'
# adding('string') -----> 'stringly'

# add ing to the string when lenght is atleast 3
# if it ends with ing add ly.
# if it is less than 3 leave it unchanged.

# check length
# check the word ends with ing
# add ing or either ly

#a = input("Enter length of the word:")

def adding(word):
  if len(word) < 3:
    return word
  else:
    if word[-3:] == 'ing':
      return word + 'ly'
    else:
      return word + 'ing'

#ans = adding(a)
#print(ans)


# Write a Python program to remove the nth index character from a nonempty string
 
#deleteCharacter("Habab",2) ------> "Haab"
#deleteCharacter("Information",3) ------> "Infrmation"

#a = input("Enter word:")

# def python_program(word):
#   if len(word) == 4:
#     first = word[0:2]
#     second = word[:-2] + word[:-1]
#     return first + second
#   elif len(word) > 4:
#     number = word[0:3]
#     second = word[4:]
#     return number + second
#   else:
#     return ""

# a = input("Enter word: ")
# b = int(input("Enter position: "))

# def deleteCharacter(word, num):
#   if -1 < num < len(word):
#     firstHalf = word[0:num]
#     secondHalf = word[num+1:]
#     return firstHalf+secondHalf
#   else:
#     return "Error: index does not exist"

# newWord = deleteCharacter(a, b)
# print(newWord)


# greeting('Habab')   -----> "Hi Habab! How are you?"
# greeting('Roman')   -----> "Hi Roman! How are you?"


# name = input("Enter name: ")

# def greeting_people(n):
#   return("Hi " + name + "!" + " How are you?" )

# ans = greeting_people(name)
# print(ans)


# table(2 , 4)  -----> "2 times 4 = 8"
# table(3 , 10)  -----> "3 times 10 = 30"

# table = int(input("Enter number:"))
# table1 = int(input("Enter number:"))

# def multiplication(t,t1):
#    result = t * t1
#    ens = "times"
#    return str(t) +" "+  ens  +" "+  str(t1)  + " = "  +  str(result)

# ans = multiplication(table,table1)
# print(ans)
  
# write a function called specialEven that returns "SPECIAL EVEN" when the given number is even and also divisible by 4, the function returns "ODD" when the number is odd and it returns "EVEN" when the number is even.


# specialEven(18) ----> "EVEN"
# specialEven(4) ----> "SPECIAL EVEN"
# specialEven(9) -----> 'ODD'


# a = float(input("Enter number:"))

# def specialEven(s):
#   if s % 4 == 0 and s % 2 == 0:
#     return "SPECIAL EVEN"
#   elif s % 2 == 0:
#     return "EVEN"
#   elif s % 3 == 0:
#     return "ODD"

# ans = specialEven(a)
# print(ans)
  
# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz.
# Otherwise, it should return the same number.

# fizzbuzz(9) -----> Fizz
# fizzbuzz(5) -----> Buzz
# fizzbuzz(15) -----> FizzBuzz
# fizzbuzz(14) ---> 14

# b = float(input("Enter number:"))

# def fizz_buzz(a):
#   if a % 3 == 0 and a % 5 == 0:
#     return "FizzBuzz"
#   elif a % 3 == 0:
#     return "Fizz"
#   elif a % 5 == 0:
#     return "Buzz"
#   else:
#     return a

# ans = fizz_buzz(b)
# print(ans)


############################ LOOPS #################################

# whenever we know how many tmes have to repeat something we use for loops.
# FOR LOOP

# 1st way
# for variable_name in range(end_num)
#e.g
# for i in range(10):
#   print(i)

# 2nd way
# for variable_name in range(startnum,end_num)
# for i in range(8,10):
#   print(i)

# 3rd way
# for variable_name in range(start_num, end_num, jump)
#e.g

# for i in range(2,10,3):
#   print(i)



# write a function named countUp which takes one intiger input and print all the number from 1 till the given number.

# countUp(4)
# 1
# 2
# 3
# 4


# countUp(7)
# 1
# 2
# 3
# 4
# 5
# 6
# 7


# def countUp(num):
#   for i in range(1,num + 1):
#     print(i)

# countUp(100)


# countDown(4)
# 4
# 3
# 2
# 1

# countDown(7)
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# def countDown(num):
#   for i in range(num, 0, -1):
#     print(i)

# countDown(3)


# counting(3,10,2)
# 3
# 5
# 7
# 9

# counting(10,9,-1)
# 10
# 9

# counting(1,9,3)
# 1
# 4
# 7

# def counting(start_num,end_num,jump):
#   for i in range(start_num ,end_num,jump):
#     print(i)

# counting(40,100,3)


# table(2,5)
# 2
# 4
# 6
# 8
# 10

# table(3,2)
# 3
# 6

# table(15,3)
# 15
# 30
# 45

# def table(first_num , second_num):
#   for i in range(1,second_num+1):
#     print(first_num * i)

# table(15,3)


# power(2,5)
# 2
# 4 
# 8  
# 16  
# 32  

# power(3,2)
# 3
# 9

# power(5,3)
# 5
# 25
# 125

def power(first_num,second_num):
  for i in range(1,second_num+1):
    print(first_num ** i)

#power(5,3)

# table(2,5)

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10

# table(3,2)
# 3 x 1 = 3
# 3 x 2 = 6

# def table(first_num,second_num):
#   for i in range(1,second_num+1):
#     print  (str(first_num) + " x " + str(i) + " = " + str(i * first_num))

# table(2,5)


# numOdd(7)
# 1 number odd is 1
# 2 number odd is 3
# 3 number odd is 5
# 4 number odd is 7

# numOdd(9)
# 1 number odd is 1
# 2 number odd is 3
# 3 number odd is 5
# 4 number odd is 7
# 5 number odd is 9

# numOdd(3)
# 1 number odd is 1
# 2 number odd is 3

# def numOdd(first_num):
#   count = 1
#   for i in range(1,first_num+1):
#     if i % 2 != 0:
#       print(str(count) + ' number odd is ' + str(i))
#       count = count + 1

# numOdd(4)


# numOdd(4)
# 1 number odd is 1
# 2 number odd is 3
# 3 number odd is 5
# 4 number odd is 7

# numOdd(5)
# 1 number odd is 1
# 2 number odd is 3
# 3 number odd is 5
# 4 number odd is 7
# 5 number odd is 9

# numOdd(2)
# 1 number odd is 1
# 2 number odd is 3

def numOdd(first_num):
  data = 1
  for i in range(1,first_num+1):
      print(str(i) + " number odd is " + str(data))
      data = data + 2

# numOdd(5)

# for range loop tutorials + string tutorials + conditions


# check('Habab','a') ------> True
# check('Habab','z') ------> False



def check(word, letter):
  for i in word:
    if i == letter:
      return True
  return False

# ans = check("bcadef","b")
# print(ans)


# countLetter('Habab','a') --------> 2
# countLetter('aaaaaA','a') --------> 5
# countLetter('Habab','z') --------> 0

def countLetter(word,letter):
  count = 0

  for i in word:
    if i == letter:
      count = count + 1

  return count

#ans = countLetter("aaaaaAAAA", "a")
#print(ans)


# position("abcd","c") -----> 2
# position("Zebra","a") -----> 4
# position("Habab","w") -----> "Not present"

def position(word,letter):
  pos = 0
  for i in word:
    if i == letter:
      return pos
    pos = pos + 1
  return "Not present"
      
#ans = position("abcd","a")
#print(ans)


# write a function called Login which takes input user and password and returns Login Success full if the user input and password is same and return false if user and password are different.

# login("Habab", "Habab") ----> Login Successful
# login("Habab", "Habib") ----> Login Failed

def login(user,password):
  if user == password:
    return "Login succesfull"
  else:
    return "Login Failed"

# ans = login("Habab","Habib")
# print(ans)

# write a function called Login which takes input user and password and returns Login Success full if the total number of letters in user input and password is same. return false if the total number of letters user and password are different.

# login("Habab", "Habab") ----> Login Successful
# login("Habab", "Habib") ----> Login Successful

def login(user,password):
  if len(user) == len(password):
    return "Login Successful"
  else:
    return "Login Unsuccessful"

#ans = login("Habab","Habib")
#print(ans)
  
# write a function called Login which takes input user and password and returns Login Success full if the total number of letters in user input and password is same. return How many characters are missing in the password or user if the total number of letters user and password are different.

# login_new("Habab", "Habab") ----> Login Successful
# login_new("Habab", "Habb") ----> You miss by 1 character
# login_new("Habab", "H") ----> You miss by 4 character

def login_new(user,password):
  count = len(user) - len(password)
  s = len(password) - len(user)
  if len(user) == len(password):
    return "Login Successful"
  elif len(user) > len(password):
    return " You miss by " + str(count) + " character " 
  elif len(user) < len(password):
    return " You miss by " + str(s) + " character"


# login_new("Habab", "Habab") ----> Login Successful
# login_new("Habab", "Habibi") ----> You miss by 2 character
# login_new("Habab", "H") ----> You miss by 4 character

def login_new1(user,password):
  if user == password:
    return "Login Successful"
  else:
    count = 0
    if len(user) > len(password):
      s = len(user) - len(password)
      for i in range(0,len(password)):
        if user[i] != password[i]:
          count = count + 1

      return "You miss by "+ str(count + s) + ' letter'
    
    elif len(user) < len(password):
      a = len(password) - len(user)
      for i in range(0,len(user)):
        if password[i] != user[i]:
          count = count + 1

      return "You miss by "+ str(count + a) + ' letter'
    
    else:
      for i in range(0,len(user)):
        if password[i] != user[i]:
          count = count + 1
      
      return "You miss by "+ str(count) + ' letter'
    

  
    # get the difference between the lenghts and add it to coun

# ans = login_new1("Habibzzzz","Habib")
# print(ans)

# WHILE
# whenever we don't know how many tmes have to repeat something we use while loops but in this case we know the condition.


# i = 0

# while i < 10:
#   print(i)
#   i = i + 1


# countDown(10)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# countDown(3)
# 3
# 2
# 1

# def countDown(number):

#   while number >= 1:
#     print(number)
#     number = number - 1

    
    
# countDown(10)


# enterOne()
# kindly enter number 1: 4
# wrong!
# kindly enter number 1: 3
# wrong!
# kindly enter number 1: 2
# wrong!
# kindly enter number 1: 10
# wrong!
# kindly enter number 1: 1
# Good!

# WHEN DO I STOP MY WHILE LOOP?

# It should stop as soon as user enter desired number which is 1 in this specific case ( Base condition for while loop)

def enterOne():

  c = input("Kindly enter number 1:")

  while c != '1':
    print("Wrong!")
    c = input("Kindly enter number 1:")
  
  print("Good")



#enterOne()



# enterBetween1and100()
# kindly enter number 1 - 100: 101
# wrong!
# kindly enter number 1 - 100: -1
# wrong!
# kindly enter number 1 - 100: 1540
# wrong!
# kindly enter number 1 - 100: 101
# wrong!
# kindly enter number 1: 1
# Good!


# def enterBetween1and100():

#   a = int(input("Kindly enter number 1 - 100:"))

#   while a > 100 or a < 1:
#     print("Wrong")
#     a = int(input("Kindly enter number 1 - 100:"))
  
#   print("Good")

# enterBetween1and100()



# write a function called blah this functions takes one argument return true if that argument is divisble by 4 and divisble 6 oterwise the function returns false

# blah(4) ----> False
# blah(24) -----> True
# blah(6) -----> False
# blah(1)  -----> False

# def blah(n):
#   if n % 4 == 0 and n % 6 == 0:
#     return True
#   return False


# a = int(input("Enter value:"))
# ans = blah(a)
# print(ans)


# enterEvenNumber()
# kindly enter even number: 3
# 3 is not even
# kindly enter even number: 17
# 17 is not even
# kindly enter even number: 4
# Good! 4 is even

def enterEvenNumber():
  a = int(input("kindly enter even number:"))
  b = 2

  while a % b != 0 or a == 0:
    print(str(a) + "is not even")
    a = int(input("kindly enter even number:"))

  print("Good!" + str(a) + " is even")

enterEvenNumber(1)
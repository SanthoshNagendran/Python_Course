# this part is for the(Class Inheritance) base class - Inherited class
'''
this is used to use the functionalities of one class in another
which usually has base class and an inherited class
'''
from Base_Class import chef
from Inherited_Class import Chinese_Chef

Our_chef = chef()
Our_chef.Special_Dish()

Our_chef_1 = Chinese_Chef()
Our_chef_1.Special_Dish()



# this is just a practise quiz

from MCQ import Questions

question_prompts = [
    "what is the color of the sky?\n(a) Red\n(b) Blue\n(c) Green\n\n",
    "What is the color of an apple\n(a) Red\n(b) Blue\n(c) Green\n\n",
    "What is the color of a leaf\n(a) Red\n(b) Blue\n(c) Green\n\n"
    ]
questions = [
    Questions(question_prompts[0], "b"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "c"),
    ]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("you got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

# this part is called Class and object in python
'''
first we have to create a seperate file for the class with the definitions
and then we can use it in the main python file using the keyword Import,
from - keywords
'''
from Class import Student


student1 = Student("Santhosh","Engineer",3.7,False)
print(student1.gpa)
print(student1.on_honor_roll())

# this part is called modules in python which is used to import python file in another
'''
this part is really cool in python which is used to use the python file into
the other python file just with one keyword "import" followed by the python
file name which we have to import inn

there are so many module available inter, and external as well
we are also allowed to download the third party modules and use it
This module in python is siilar to the libraries in some other softwares
'''
import Useful_tool
print(Useful_tool.roll_dice(10))


# this is for Files, open, close, read, write
Employee_file = open("Employer.txt","r")
''' print(Employee_file.read()) #this is for reading entire file 
print(Employee_file.readline()) #this is to read one line
print(Employee_file.readline()) #this is to read a line after
print(Employee_file.readlines()) #this is to read the file in a a single word '''
for employee in Employee_file.readlines():
    print(employee)
Employee_file.close()

# this is to write in the file
'''in here instead file open in a - append or w - write mode will add on
to the existing file and create a new file with a name'''
Employee_file = open("Employer.txt","a")
Employee_file.write("\nShwetha Venkatalakshmi")
print('New txt added to the specified file')
Employee_file.close()



# this for "try and except"
'''
if something goes wrong in the program like an error,
instead of showing a blind error this part would help us what the
actual problem going on is!!
'''
try:
    number = int(input("Enter an integer value"))
    print(number)
except ZeroDivisionError as err :
    print(err)
except ValueError:
    print("i told you to  type integer da venna")
    print("be the way its an value error")

#this is for the topic "For loop"
'''
this part in here is really a cool program that really explains about the
different ways in using the indexing in looping
'''
def Crazy_Translator(phrase):
    translator = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translator = translator + "XX"
        elif letter in "Bb":
            translator = translator + "YY"
        else:
            translator = translator + letter
    return translator


print(Crazy_Translator(input("Enter a phrase: ")))

for letter in "santhosh":
    print(letter)
    
#this part is really amazing in the for loop statement
Mates = ["sandy", "yendi", "vedi"] 
for M in Mates:
    print(M)
for i in range(10):
    print(i)
friends = ["m","e","o"]
for i in range(len(friends)):
    print(friends[i])

#this is for topic "While" loop
secret_word = "santhosh"
guess = ""
i =1
while i<=10:
    print(i)
    i+=1.25
print("done with the loop")


while guess != secret_word:
    guess = str(input("Enter a password"))
    

print("You Win!")

#this part is for the topic 'Dictionary'
Value = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    5: "Five"
}
print(Value["4"])
print(Value.get(5))


#this is for IF else statement
is_male = False
is_tall = False

if is_male and is_tall:
    print("you are either male or tall or both")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are a tall female")
else:
    print("you are neither male, nor small")


# this is an example of a topic "Function"
def Copy_Msg(name , age):
    print('Hello' + name + ', you are' + age)
    return 'Bye bye'

name = input('Enter a name')
age = input('Enter your age')
print("meet you later ,", Copy_Msg(name , age))


#this part is called Tuples <which can't be changed or modified>
coordinates = (4, 5)
print(coordinates)
print(coordinates[1])


#this part is called List
Friends = ['santhosh','ramesh', 'suresh' , 'MALA']
print(Friends)
Friends[2]= 'kaala'
print(Friends)
Friends.sort()
print(Friends)
print(Friends[1:3])
print(Friends[-1])
Num = [1,2,3,4,5]
Friends.append(Num[0:3])
Friends.insert(0,'Shwetha')
Friends.extend(Num)
Friends.remove('santhosh')
print(Friends)
print(Friends.index('MALA'))
print(Friends.count('ramesh'))


#this is just for drawing 
print("       /\       ")
print("      /  \     ")
print("     /    \   ")
print("    /      \    ")
print("   /________\           ")

print(3/2)


# this is just to convert a number to a string
My_Num = 9
print(My_Num)
print(str(My_Num) + " is my favourite number")

# simple maths functions
print(abs(-5.6))
print(round(5.6))
print(max(0,2,4,5,5))

# this is just to get an inputs from the user and do some operations
name = input('enter your name')
age = input('enter your age')
print("hello" + name + 'you are' + age + 'years old')
num1 = input('enter a vslue')
num2 = input ('enter b value')
result = float(num1)+float(num2)
print(result)




#Day 1- 01 Jan 2021
print('*'*25, 'Start of Day 1', "*"*25)
print('We will learn about the following functions: print(), type(), len(), input(), str(), int()')
print('We will also learn about string concatenation, string replication.')

print('Hello World!!!!!') #print function

name = input('Please enter your name: ') #prompt the user to enter their name using input function
print('Welcome to the world of Python '+ name) #String Concatenation
print('The length of your name is: ', len(name)) #len function
print('The data type of name is: ', type(name)) #type function

age = input('Please enter your age: ') #Prompt the user to enter their age using input function
print('The data type of age is: ', type(age))
print("Oh No"+'!'*10 + " age can't be a string. It needs to be an integer.") #string replication
age = int(age) #Converting age to integer using type conversion
print(name + ', you will be ' + str(age+1) + ' in one year') #Converting age to string using type conversion

print('*'*25, 'End of Day 1', "*"*25)

# Day 2- 02 Jan 2021
# Multiline statements- Statements in Python can be extended to one or more lines using () {} [] ; \

#Declared using \
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print('The value of s is:', s)

#Declared using ()
n = (5*6*2
     +1+2+3)
print('The value of n is:', n)
import math
import datetime

def kmToMiles(kilometers):
    return kilometers * 0.621371
def isDivisibleBy11(num):
    return num%11==0
def getHighest(num1,num2):
    if num1>num2:
        return num1
    return num2
def hexagonArea(length):
    return (3*math.sqrt(3)/2*length**2)
def sleepsUntilXmas():
    now = datetime.datetime.now()
    christmas = datetime.datetime.strptime('25-12-2024','%d-%m-%Y')
    until = christmas-now
    return until.days
def isPalindrome(text):
    text = text.lower()
    return text[::-1]==text
def fuelCost(distance, mpg, fuelCost):
    return distance/mpg*fuelCost
def mostCommonChar(sentence):
    #the list below is sourced from the Concise Oxford Dictionary
    lettersSortedByFrequency = ['e','a','r','i','o','t','n','s','l','c','u','d','p','m','h','g','b','f','y','w','k','v','x','z','j','q']
    for letter in lettersSortedByFrequency:
        if letter in sentence.lower():
            return [letter,lettersSortedByFrequency.index(letter)]
def isPrime(num):
    return math.sqrt(num)

print("Here the challenges I was able to complete in one class period:")#I woulda put this all in one print statement with \n new lines but thats too hard to read the code with
print("Kilometers to miles: 0")
print("Is the number divisible by 11?: 1")
print("Get the highest of 2 numbers: 2")
print("Find the area of a hexagon using the length of one side: 3")
print("How many sleeps til christmas 2024?: 4")
print("Is the string a palindrome?: 5")
print("How much itll cost you to go a distance: 6")
print("The most common character in a string: 7\n")

choice = int(input("which one would you like to test: "))

if choice==0:
    print(kmToMiles(float(input("Enter Kilometers: "))))
elif choice==1:
    print(isDivisibleBy11(int(input("Enter number: "))))
elif choice==2:
    print(getHighest(int(input("First number: ")),int(input("Second number: "))))
elif choice==3:
    print(hexagonArea(int(input("Input length of a side: "))))
elif choice==4:
    print(f"you will have {sleepsUntilXmas()} sleeps until christmas...")
elif choice==5:
    print(isPalindrome(input("Put in a word to test if it's a palindrome: ")))
elif choice==6:
    print(f"It will cost you ${fuelCost(int(input("How far are you going?: ")),int(input("What's you're miles per gallon?: ")),int(input("How much does fuel cost?: ")))}")
    #i dont drive a car, so i don't know if this is correct :D
elif choice==7:
    result = mostCommonChar(input("Let me find the most common character in a string you write: "))
    print(f"The letter {result[0]} is the most common letter in your string. It is ranked {result[1]+1} in the most common letters")
elif choice==8:
    print(isPrime(int(input("Enter a number: "))))
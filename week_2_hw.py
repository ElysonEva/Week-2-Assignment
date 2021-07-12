# Evangelista, Elyson
from collections import namedtuple


# problem 1
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


print(factorial(10))


# problem 2
def palindrome(word: str):
    return word == word[::-1]


print(palindrome("racecar"))


# problem
def listmult(f: list):
    new_list = []
    for value in f:
        new_value = (value * max(f) / min(f))
        new_list.append(new_value)
    return new_list


print(listmult([4,6,2,5,7,3]))

# problem 4

Employee = namedtuple("worker", "name position salary full_time")
Employee("Elyson Evangelista", "Retail", 50000, True)


def employeemanager(employee):
    monthly_income = employee.salary // 12
    print("Name: " + employee.name + "\n" +
          "Position: " + employee.position + "\n" +
          "Monthly Pay: " + str(monthly_income))
    if employee.full_time is True:
        print("Full Time: Yes")
    else:
        print("Full Time: No")


employeemanager(Employee("Elyson Evangelista", "Retail", 50000, True))


# problem 5
def issublist(a, b):
    check = []
    for val_b in b:
        for val_a in a:
            if val_a == val_b:
                check.append(val_a)
    if check.sort() == a.sort():
        print(True)
    else:
        print(False)


issublist([2, 4], [5, 2, 7, 4, 9, 6])


# problem 6
def translator(sentence: str):
    word_split = sentence.split()
    final_sentence = ""
    for word in word_split:
        final_word = word[1:len(word)+1] + word[0].lower() + "ay"
        final_sentence = final_sentence + final_word + " "
    return final_sentence


print(translator("the quick brown fox"))


# problem 7
def hangman(word: str):
    strike = 0
    word_split = list(word)
    final = []
    print("Welcome to Hangman!")
    while strike != 8:
        guess = input("Enter a letter: ")
        if guess in word_split:
            print("'{}' is in the word".format(guess))
            print("You have {} strikes.".format(strike))
            final.append(guess)
            if sorted(final) == sorted(word_split):
                print("You have won! The word was {}!".format(word))
                break
        else:
            strike += 1
            print("'{}' is not in the word".format(guess))
            print("You have {} strikes.".format(strike))
    else:
        print("You have 8 strikes and have lost. The word was {}.".format(word))


hangman("cat")

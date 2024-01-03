
from random import randint

def main():
    correct = 0
    incorrect = 0
    userInput = 0
    while userInput != -1:
        level = int(input ("Enter difficulty level (1 or 2): "))
        selection = menu()
        num1, num2, answer = numbers(selection, level)
        userInput = int(input())
        if userInput == -1:
            continue
        if userInput == answer:
            correct += 1
            print(feedback("correct"))
        else:
            incorrect += 1
            print(feedback("incorrect"))
        print()
    print()
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Thank you for playing!")

def menu():
    print()
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Random Operation")
    selection = input("Enter the operation (1 to 5): ")
    print()
    return selection

def numbers(selection, level):
    lesser = 0
    higher = 0
    if level == 1:
        lesser = 0
        higher = 9
    if level == 2:
        lesser = 10
        higher = 99
    num1 = randint(lesser, higher)
    num2 = randint(lesser, higher)
    signs = ["+", "-", "*", "//"]
    sign = ""
    answer = 0
    if selection == "1":
        sign = signs[0]
    elif selection == "2":
        sign = signs[1]
    elif selection == "3":
        sign = signs[2]
    elif selection == "4":
        sign = signs[3]
    elif selection == "5":
        sign = signs[randint(0,3)]
        
    if sign == "-" and num2 > num1:
        num1, num2, num2, num1
    if sign == '/' and num2 == 0:
        num2 = 1
    expression = str(num1) + " " + sign + " " + str(num2)
    answer = eval(expression)
    print ("How much is " + expression + "?",)
    print ("Enter your Answer(-1 to exit): ",end=" ")
    return num1, num2, answer

def feedback(answer: str):
    correctFeedback = ["Keep up the good work!", "Excellent!", "Nice work!", "Very good! "]
    incorrectFeedback = ["No, keep trying.", "Dont give up!", "Wrong, try once more", "No, Please try again."]
    index = int()
    rlist = list()
    if answer == "correct":
        rlist = correctFeedback
    elif answer == "incorrect":
        rlist = incorrectFeedback
    index = randint(1, len(rlist))
    return rlist[index-1]
    
main()

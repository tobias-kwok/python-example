# Prefect Square Test
import random
import numpy

num_of_correct = 0

for i in range(10):
    square_or_squareroot = random.randint(0, 1)
    number = random.randint(1, 39)
    number_square = numpy.square(number)
    
    #print("The number picked is", number)
    if square_or_squareroot == 0:
        answer = input("What is the square of " + str(number) + "? ")
        answer = int(answer)    
        #print("The square of", number, "is", number_square, ".")
        if answer == number_square:
            print(" That is the correct answer.")
            num_of_correct = num_of_correct + 1
        else:
            print("That is the wrong answer.")
            print("The correct answer is", number_square)
    else:
        answer = input("What is the square root of " + str(number_square) + "? ")
        answer = int(answer)            
        #print("The square root of", number_square, "is", number, ".")
        if answer == number:
            print(" That is the correct answer.")
            num_of_correct += 1
        else:
            print("That is the wrong answer.")
            print("The correct answer is", number)
    
    print(" ")

print ("You have answered correctly", num_of_correct, "times.")  
       
    
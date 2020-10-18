import random

print ("Try to guess the number the computer has generated (1 to 100)")


#Step one find a number between 1 and 100, call this variable secret
#Step two loop until the user guessed the secret
#Step three print out the number of times they gave an input


secret = random.randint(1, 100)
#print (secret)
guess = -1
min = 1
max = 100
num_of_guesses = 0

while guess != secret: 
    guess = input("Please input a number between " + str(min) + " and " + str(max) + " ")
    guess = int(guess)
#    print ("you have entered ", guess)

    if guess == secret:
        print ("You have found the secret.")
    elif guess > secret:
        print ("The number you have entered is to large.")
        max = guess
    else:
        print ("The number you have entered is too small.")
        min = guess
    num_of_guesses = num_of_guesses + 1
    print (" ")


print ("You have guessed",num_of_guesses, "times.")  
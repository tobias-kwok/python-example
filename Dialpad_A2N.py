the_word = input("Please give a word. ")
print ("Now I shall change", the_word," into a number on the dialpad")
    
character2number={'a' : '2', 
         'b' : '2',
         'c' : '2', 
         'd' : '3', 
         'e' : '3', 
         'f' : '3', 
         'g' : '4', 
         'h' : '4', 
         'i' : '4', 
         'j' : '5', 
         'k' : '5', 
         'l' : '5', 
         'm' : '6', 
         'n' : '6', 
         'o' : '6', 
         'p' : '7', 
         'q' : '7', 
         'r' : '7', 
         's' : '7', 
         't' : '8', 
         'u' : '8', 
         'v' : '8', 
         'w' : '9', 
         'x' : '9', 
         'y' : '9', 
         'z' : '9'}

the_number = ''

for each_character in the_word:
    the_number += character2number[each_character.lower()]
    
print (the_number)

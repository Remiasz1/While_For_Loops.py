# while loops = execute some code WHILE some conditions remains true
# while loops and for loop
# are forms of iteration
# iteration is the process of
# repeating or looping through
# a set of steps or instructions
# to iterate is the verb
# form of iteration
# be careful of infinite loops
# they will crash your program
# and you will have to restart it
# infinite loops are loops that never end




# name = input("Enter you name. ") # this is all apart of while loop

# while name == "": 
#     print("You did not enter your name") # this causes an infinite loop
    # name = input("Enter your name")

# print(f"Hello {name}") 
# No longer in loop



# age = int(input("Enter your age"))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age"))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}. ")
#     food = input("Enter another food you like (q to quit)")

# print("bye")



# num = int(input("Enter a number from 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid. ")
#     num = int(input("Enter a number between 1 - 10: "))

# print(f"Your num is {num}. ")




# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc



# for x in reversed(range(1, 11)): # reverses the numbers
#     print(x)

# print("HAPPY NEW YEAR")

# for x in range(1, 11, 2): # the 2 makes it so it counts by two
#     print(x)

# print("HAPPY NEW YEAR")



# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)



# for x in range(1, 21):
#     if x == 13 or x == 15 or x == 19:
#         continue # continues the program
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break # stops the program
#     else:
#         print(x)



# horror_movies = ["The Exorcist" , "The Shining" , "The Conjuring" , "The Ring"]

# for movie in horror_movies:
#     if movie == "The Shining":
#         print("The Shining")
#         break
#     else:
#         print("The Shining was not found")
#         print(movie)


# horror_char = ["Jason" , "Micheal Miers" , "Freddy Fazbear" , "Nolan North"]

# for x in horror_char: 
#     if x == "Nolan North":
#         continue
#     else:
#         print(x)


horror_monsters = ["Alien" , "Predator" , "The Thing" , "Swamp Thing"]

for x in horror_monsters:
    if x == "Swamp Thing": 
        x = "Nemesis"
        print(x)
    else:
        print(x)


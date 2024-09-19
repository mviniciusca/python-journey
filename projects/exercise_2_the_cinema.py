'''
3 movies for different ages.
------------------------------
The first one, is for under 12 years old. 
The second one, is for over or equal 12 and under 18 years old. 
The third one is for over 18 years old.
'''

age = int(input("Enter your age: "))

if(age < 12):
    print("Your movie is the first one")
elif (age >= 12 and age < 18):
    print("Your movie is the second one")
else:
    print("Your movie is the third one")

'''
The second point is the available of the tickets. 
'''

tickets = 30
quantity = int(input("Enter the quantity of tickets: "))

if(quantity <= tickets):
    print("There are tickers available! You can buy it!")
else:
    print("There are no tickets available")
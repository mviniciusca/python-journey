'''
Loops in Python
'''

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

'''
Example 2: listing fruits
'''
fruits = ['banana', 'strawberry', 'cherry', 'blueberry', 'orange']
for fruit in fruits:
    print(fruit)

'''
Example 3: Find the word 
'''

search = input('Search for a product: ')
products = ['ball', 't-shirt', 'paint', 'shoes']
for product in products:
    if(product == search):
        print(product)
        break
'''

'''
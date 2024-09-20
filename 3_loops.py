'''
Loops in Python
### For
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
found = False
for product in products:
    if(product == search):
        print(product)
        found = True
        break
if not found:
    print("Product not Found")

    
    '''
    ### While
    '''
    i = 1
    while i < 10:
        print(i)
        i += 1

    number = int(input("Enter a number (0 to stop)"))
    while number != 0:
        if number % 2 == 0:
            print("Even")
        else:
            print("odd")
        number = int(input("Enter a number (0 to stop)"))
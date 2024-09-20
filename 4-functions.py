'''
### Functions
'''

a = float(input("Number 1: "))
b = float(input("Number 2:"))
def sum(a, b):
    result = a + b
    return result
print(sum(a, b))

def odd():
    number = int(input("Enter a valid number: "))
    if number % 2 == 0:
        print("Even")       
    else:
       print("Odd")

odd()

'''
Lambda fn
'''

sum = lambda a,b: a+b
result = sum(3,8)
print(result)
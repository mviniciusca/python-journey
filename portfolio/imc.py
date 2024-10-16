'''
IMC Calculator
'''

def imc():
    ## Input
    height = float(input("Enter your height (m): "))
    weight = float(input("Enter your weight (Kg): "))
    ## Check if the value is not zero
    if height <= 0 or weight <= 0:
        print("Enter a valid value")
        height = float(input("Enter your height (m): "))
        weight = float(input("Enter your weight (Kg): "))
    ## Get the result
        result = weight / (height ** 2) ## ** square
        result = round(result, 2)    
    ## Classification
    if result <= 18.5:
            level = 'Under Normal'
    elif 18.6 <= result <= 24.99:
            level = 'Normal' 
    elif 25 <= result <= 29.99:
            level = 'Overweight'
    elif 30<= result <= 34.99:
            level = 'Obesity Level 1'
    elif 35 <= result <= 39.99:
            level = 'Obesity Level 2'
    else:
            level = 'Obesity Level 3' 
    ## Final
    print(f'Your IMC is: {result} and it\'s mean that your level is {level} according to OMS')

## Calling the fn
imc()
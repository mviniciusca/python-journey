'''
IMC with functions
'''

def validate(weight, height):
        while weight <= 0 or height <= 0:
                print(input("Enter a valid value! "))
                weight = float(input("Enter your Weight (m): "))
                height = float(input("Enter your Height (Kg): "))
        return weight, height      

def imc_calc(weight,height):
    return weight / (height ** 2)
    
def classification(result):
    if result <= 18.5:
            level = 'Under Normal'
    elif 18.6 <= result <= 24.9:
            level = 'Normal' 
    elif 25 <= result <= 29.99:
            level = 'Overweight'
    elif 30 <= result <= 34.99:
            level = 'Obesity Level 1'
    elif 35 <= result <= 39.99:
            level = 'Obesity Level 2'
    else:
            level = 'Obesity Level 3' 
    return level

def imc():
        height = float(input("Enter your height: (m) "))
        weight = float(input("Enter your weight: (Kg) "))

        weight, height = validate(weight, height)
        imc = round(imc_calc(weight, height), 2)
        result = classification(imc)
        print(f"Your IMC is: {imc} and your level is {result}") 

imc()
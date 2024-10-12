'''
IMC with functions
'''

def validate(weight, height):
        while weight <= 0 or height <= 0:
               return "Enter a valid value!"               
        return weight, height      

def imc_calc(weight,height):
    return weight / (height ** 2)
    
def classification(result):
    if result <= 18.5:
            level = 'Under Normal'
    elif 18.6 <= result <= 24.9:
            level = 'Normal' 
    elif 25.0 <= result <= 29.9:
            level = 'Overweight'
    elif 30.0 <= result <= 34.9:
            level = 'Obesity Level 1'
    elif 35.0 <= result <= 39.9:
            level = 'Obesity Level 2'
    else:
            level = 'Obesity Level 3' 
    return level

def imc(weight, height):
        weight = float(weight)
        height = float(height)

        weight, height = validate(weight, height)
        imc = round(imc_calc(weight, height), 2)
        result = classification(imc)
        return (f"Your IMC is: {imc} and your level is {result}")

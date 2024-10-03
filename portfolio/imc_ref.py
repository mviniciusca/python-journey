'''
IMC
'''

def validate(x,y):
    if x <= 0 or y <= 0:
        print("Please, enter a valid value")
        y = float(input("Enter your heigh: "))
        x = float(input("Enter your weight: "))
        validate(x,y)
    else:
          return x,y
    
def imc():
    y = float(input("Enter your heigh: "))
    x = float(input("Enter your weight: "))

    validate(x,y)
    imc = round(imc_calc(x,y),2)
    result = classification(imc)
    print(f"Your IMC is: {imc} and your level is {result}")

def imc_calc(x,y):
    result = x /(y ** 2)
    return result
 
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





imc()
 
   



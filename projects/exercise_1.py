media1 = int(input("Note 1: "))
media2 = int(input("Note 2: "))
media3 = int(input("Note 3: "))
media4 = int(input("Note 4: "))
media = (media1 + media2 + media3 + media4)/4

if(media >= 6):
    result = 'Approved'
else:
    result = 'Reproved'
    
print(f"Your final media is: {media} and you are: {result} ")
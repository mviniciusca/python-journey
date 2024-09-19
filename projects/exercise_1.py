## Media

media1 = float(input("Note 1: "))
media2 = float(input("Note 2: "))
media3 = float(input("Note 3: "))
media4 = float(input("Note 4: "))

media = (media1 + media2 + media3 + media4) / 4
approved = 6

if(media >= approved):
    status = 'approved'  
else:
    status = 'reproved'

print(f"Your media is: {media} and your status is: {status}")
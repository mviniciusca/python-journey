def media():
    a = int(input("Enter note 1: "))
    b = int(input("Enter note 2: "))
    c = int(input("Enter note 3: "))
    d = int(input("Enter note 4: "))

    media = int((a + b + c + d) / 4)

    return print((f"Your media is: {media}"))

media()
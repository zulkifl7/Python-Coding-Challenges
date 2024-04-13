sufix = {

        2 : "B",
        8 : "O",
        10 : "D",
        16 : "H"
}

# creating a list to handle with hexa decimal representation
signs = []
for i in range(0,10):
    signs.append(str(i))
signs = signs + ["A","B","C","D","E","F"]

def decimal_to(dec,system):
    
    signs = []
    for i in range(0,10):
        signs.append(str(i))
    signs = signs + ["A","B","C","D","E","F"]

    rem = 0
    value = ""
    while dec != 0:
        rem = dec % system
        dec = dec // system
        value = signs[rem] + value
    print(f"{value}-{sufix[system]}")

def to_decimal(num,system):
    err = 0
    # Seperation induvidual digits in the number to conversion
    values = list(reversed((" ".join(str(num))).split(" "))) # here we are adding a space between all letters
    # values = values.split(" ") # spliting in the space
    # values = list(reversed(values))
    
    # Conversion 
    k = 0
    dec_value = 0
    while len(values) > k:
        # chech if the number is valid
        if system == 16:
            if (str(values[k]) not in signs):
                print(f"Invalid number! {values[k]} cannto be used in {system} based number system!")
                err = 1
                
        else:
            if (int(values[k]) >= system):
                print(f"Invalid number! {values[k]} cannto be used in {system} based number system!")
        n = 0
        while n < 16:
            if str(values[k]) == str(signs[n]):
                dec_value += (system**k)*n
            n += 1
        k += 1
    if err == 0:
        print(f"{dec_value}-D") 


to_decimal("143",8)
decimal_to(234,10)


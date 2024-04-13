def decimal_to_hex(dec):
    signs = []
    for i in range(0,10):
        signs.append(str(i))
    signs = signs + ["A","B","C","D","E","F"]

    rem = 0
    hex_value = ""
    while dec != 0:
        rem = dec % 16
        dec = dec // 16
        hex_value = signs[rem] + hex_value
    print(hex_value)

def hex_to_decimal(hexa):
    signs = []
    for i in range(0,10):
        signs.append(i)
    signs = signs + ["A","B","C","D","E","F"]
    values = list(reversed((" ".join(str(hexa))).split(" "))) # here we are adding a space between all letters
    # values = values.split(" ") # spliting in the space
    # values = list(reversed(values))
    
    k = 0
    dec_value = 0
    while len(values) > k:
        n = 0
        while n < 16:
            if str(values[k]) == str(signs[n]):
                dec_value += (16**k)*n
            n += 1
        k += 1

    print(dec_value) 

print("Hello World")



# decimal_to_hex(23423742)
hex_to_decimal("A2B6")
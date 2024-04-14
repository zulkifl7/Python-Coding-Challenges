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

def decimal_to(dec,num_system):
    
    signs = []
    for i in range(0,10):
        signs.append(str(i))
    signs = signs + ["A","B","C","D","E","F"]

    rem = 0
    value = ""
    while dec != 0:
        rem = dec % num_system
        dec = dec // num_system
        value = signs[rem] + value
    print(f"{value}-{sufix[num_system]}")

def to_decimal(num,num_system):
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
        if num_system == 16:
            if (str(values[k]) not in signs):
                print(f"Invalid number! {values[k]} cannto be used in {num_system} based number system!")
                err = 1
                
        else:
            if (int(values[k]) >= num_system):
                print(f"Invalid number! {values[k]} cannto be used in {num_system} based number system!")
        n = 0
        while n < 16:
            if str(values[k]) == str(signs[n]):
                dec_value += (num_system**k)*n
            n += 1
        k += 1
    if err == 0:
        print(f"{dec_value}-D") 

# Octal to binary conversion

def octal_hex_to_binary(num,num_system):
    bin_value = "" # this is the place where the answer goes
    err = 0 # To find if the number user entered is an octal/hexa number and record the output 
    
    # main loop to go through the digits
    for i in str(num):
        value_hold = ""
        m = 0 # to detect the equevelent value for hexa decimal signs
        while i != signs[m]:
            m += 1
        k = 0 # to maintain 3-bit for octal and 4-bit for hexa
        # Checking if the number is an octal number 
        if num_system == 8:
            
            k = 3
            if m > 7:
                err = 1
                break
        elif num_system == 16:
            k = 4
            
        
        # converting the digit to binary 
        while m > 0:
            value_hold = str(m % 2) + value_hold
            m = m // 2
        #  making sure the octal digit is converted to 3-bit binary equevelant
        while len(value_hold ) < k:
            value_hold = "0" + value_hold
        # updating the final answer
        bin_value = bin_value + value_hold
    if err == 0:
        print(bin_value)


# to_decimal("143",8)
# decimal_to(234,10)
octal_to_binary("A2",16)


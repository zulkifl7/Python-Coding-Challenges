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
    pass





decimal_to_hex(23423742)
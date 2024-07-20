def binary_to_decimal(bin):
    decimal = 0
    bin = str(bin)
    length = len(bin)
    
    for i in range(length):
        digit = int(bin[length - 1 - i])
        decimal += digit * (2 ** i)
        
    return decimal

def decimal_to_binary(dec):
    binary = ""
    dec = int(dec)  
    if dec == 0:
        return "0"
    while dec > 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    return binary

def test_convertions(): # Casos de teste
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("1111") == 15
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(15) == "1111"
    print("All tests passed!")

test_convertions()
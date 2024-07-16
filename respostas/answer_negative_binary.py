def binary_to_decimal(bin):
    is_negative = bin[0] == '-'
    if is_negative:
        bin = bin[1:]
    
    decimal = 0
    bin = str(bin)  
    for digit in bin:
        decimal = decimal * 2 + int(digit)
    
    if is_negative:
        return -decimal
    return decimal

def decimal_to_binary(dec):
    is_negative = dec < 0
    if is_negative:
        dec = -dec
    
    binary = ""
    dec = int(dec)  
    if dec == 0:
        return "0"
    while dec > 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    
    if is_negative:
        return '-' + binary
    return binary

def test_conversions():
    # Casos de teste para converter de binário para decimal
    assert binary_to_decimal("0") == 0
    assert binary_to_decimal("1") == 1
    assert binary_to_decimal("10") == 2
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("1111") == 15
    assert binary_to_decimal("10000") == 16
    assert binary_to_decimal("1100100") == 100
    assert binary_to_decimal("-1") == -1
    assert binary_to_decimal("-10") == -2
    assert binary_to_decimal("-1010") == -10
    assert binary_to_decimal("-1111") == -15
    assert binary_to_decimal("-10000") == -16
    assert binary_to_decimal("-1100100") == -100

    # Casos de teste para converter decimal para binário
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(15) == "1111"
    assert decimal_to_binary(16) == "10000"
    assert decimal_to_binary(100) == "1100100"
    assert decimal_to_binary(-1) == "-1"
    assert decimal_to_binary(-2) == "-10"
    assert decimal_to_binary(-10) == "-1010"
    assert decimal_to_binary(-15) == "-1111"
    assert decimal_to_binary(-16) == "-10000"
    assert decimal_to_binary(-100) == "-1100100"
    
    print("All tests passed.")

# Execute os testes
test_conversions()

def decimal_to_binary(decimal_number):
    binary_number = "" #use a string to avoid reversing the sequence
    
    if decimal_number == 0:
        return "0"

    while decimal_number > 0:
        remainder = decimal_number % 2  
        binary_number = str(remainder) + binary_number  
        decimal_number //= 2  

    return binary_number


decimal = int(input("Enter a decimal number for conversion: "))
binary = decimal_to_binary(decimal)
print(f"The converted binary number is: {binary}")

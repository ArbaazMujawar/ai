def perform_operations(input_string):
    # Initialize empty strings for storing results
    and_result = ''
    xor_result = ''

    # Perform AND and XOR operations on each character
    for char in input_string:
        # Convert character to ASCII value
        ascii_value = ord(char)
        
        # Perform AND operation with 127
        and_result += chr(ascii_value & 127)
        
        # Perform XOR operation with 127
        xor_result += chr(ascii_value ^ 127)

    return and_result, xor_result

# Define the input string
input_string = "Hello World"

# Perform operations and display results
and_result, xor_result = perform_operations(input_string)
print('Original String:', input_string)
print('AND Result:', and_result)
print('XOR Result:', xor_result)




"""Let's break down the output based on the provided code:

Original String: Hello World
This line simply displays the original input string, which is "Hello World".
AND Result: Hello World
The AND operation (ascii_value & 127) with 127 for each character in the input string "Hello World" does not change the characters because bitwise ANDing any character with 127 will not affect its ASCII representation for typical printable characters. Therefore, the AND result is the same as the original string.
XOR Result: 7→‼‼►_(►
The XOR operation (ascii_value ^ 127) with 127 for each character in the input string "Hello World" performs a bitwise XOR operation, resulting in a different character for each original character. This is because XORing a character with 127 flips its bits.
Here's the breakdown of the XOR operation for each character:
'H' XOR 127 = 7
'e' XOR 127 = →
'l' XOR 127 = ‼
'l' XOR 127 = ‼
'o' XOR 127 = ►
' ' XOR 127 = _
'W' XOR 127 = (
'o' XOR 127 = ►
'r' XOR 127 = ►
'l' XOR 127 = ‼
'd' XOR 127 = ►
So, the XOR result "7→‼‼►_(►" is obtained by applying the XOR operation with 127 to each character in the input string "Hello World".
"""
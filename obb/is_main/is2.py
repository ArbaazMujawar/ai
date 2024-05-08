import math


def Encrypt(key: int, string: str) -> str:
    matrix = [[chr(0) for i in range(key)] for j in range(math.ceil(len(string) / key))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (key * i + j) >= len(string):
                break
            matrix[i][j] = string[(key * i + j)]
    return "".join(
        [
            "".join(i)
            for i in [
                [matrix[i][j] for i in range(len(matrix))]
                for j in range(len(matrix[0]))
            ]
        ]
    )


Key_Size: int = int(input("Give Key Size "))
encrypting_String: str = input("Give Encrypting String ")
print(Encrypt(Key_Size, encrypting_String))

"""
Encrypt Function (Encrypt(key, string))
This function takes two parameters: key, which is the size of the transposition key, and string, which is the plaintext to be encrypted.
It calculates the number of rows required in the transposition grid based on the key and the length of the string.
It creates an empty matrix (2D list) filled with null characters (chr(0)) to represent the transposition grid.
It then populates this grid with characters from the plaintext in a row-major order.
The final encrypted text is obtained by reading the grid column-wise and concatenating the characters.

Example Usage
The script prompts the user to enter the key size (Key_Size) and the plaintext to be encrypted (encrypting_String).
It then calls the Encrypt function with these inputs and prints the encrypted text."""
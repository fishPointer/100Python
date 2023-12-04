alphabet = [chr(ord("A") + i) for i in range(26)]
cipher = []


def shiftfix(index):
    while index > 25:
        index -= 26
    while index < 0:
        index += 26
    return index


def caesar(plaintext, shiftvalue, direction):
    if direction == "D":
        shiftvalue *= -1

    for x in range(len(plaintext)):
        index1 = alphabet.index(plaintext[x])
        index1 += shiftvalue
        index2 = shiftfix(index1)
        cipher.append(alphabet[index2])

    final = "".join(cipher)
    return final


def program():
    direction = input("Type 'E' to Encode and 'D' to Decode\n")
    text = input("Type your message:\n").upper()
    shift = int(input("Type the shift number:\n"))
    output = caesar(text, shift, direction)
    print(output)
    loop = input("Go again? Y/N:\n")
    if loop == "Y":
        cipher.clear()
        output = ""
        program()


program()

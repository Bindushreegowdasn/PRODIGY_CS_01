def caesar_cipher(text, shift, mode):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char  # Keep spaces, punctuation, etc.

    return result


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (e.g., 3): "))
            break
        except ValueError:
            print("Please enter a valid integer for shift.")

    mode = ''
    while mode.lower() not in ['encrypt', 'decrypt']:
        mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode.title()}ed): {result}")


if __name__ == "__main__":
    main()

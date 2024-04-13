# Jahmal Smith
def encode(password):
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Input must be an 8-digit password containing only integers.\n")

    encoded_password = []
    for char in password:
        # Shift digits by adding 3 and wrapping around if necessary
        encoded_digit = str((int(char) + 3) % 10)
        encoded_password.append(encoded_digit)

    # Join the list of characters into a string to form the encoded password
    return ''.join(encoded_password)


def main():
    while True:
        print_menu()
        option = input("Please enter an option: ")
        if option == '1':
            password = input("Please enter your password to encode: ")
            try:
                encoded_password = encode(password)
                print("Your password has been encoded and stored!\n")
            except ValueError as e:
                print(f"Error: {e}")

        elif option == '2':
            if 'encoded_password' not in locals():
                print("Error: No password has been encoded yet.\n")
            else:
                try:
                    decoded_password = decode(encoded_password)
                    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
                except ValueError as e:
                    print(f"Error: {e}")
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.\n")


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


if __name__ == "__main__":
    main()

def mirror_string(string):
    return string[::-1]

def is_palindrome(string):
    return string == string[::-1]

def handle_input(string):
    print("Bonjour")
    if is_palindrome(string):
        print(string)
        print("Bien dit")
    else:
        print(mirror_string(string))
    print("Au revoir")

input_string = input("Enter a string: ")
handle_input(input_string)

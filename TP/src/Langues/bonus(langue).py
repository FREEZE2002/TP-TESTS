def check_palindrome(string):
    return string == string[::-1]

def greet_user(language):
    greetings = {
        "french": "bonjour",
        "english": "hello",
        "spanish": "hola",
        # Add more languages as needed
    }
    return greetings.get(language.lower(), "hello")

def farewell_user(language):
    farewells = {
        "french": "au revoir",
        "english": "goodbye",
        "spanish": "adios",
        # Add more languages as needed
    }
    return farewells.get(language.lower(), "goodbye")

def main(input_string, language):
    if check_palindrome(input_string):
        return input_string

    greeting = greet_user(language)
    farewell = farewell_user(language)

    return f"{greeting} {input_string} {farewell}"

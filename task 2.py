from collections import deque

def is_palindrome(input_string):

    # Normalize the string: remove spaces and convert to lowercase
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Add characters to a deque
    char_deque = deque(normalized_string)

    # Compare characters from both ends
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Example usage
if __name__ == "__main__":
    test_strings = [
        "Madam, in Eden, I'm Adam",
        "Able was I, I saw Elba",
        "Not a palindrome",
        "12321",
        "Step on no pets",
        "Palindrome? No way!"
    ]

    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {'Palindrome' if result else 'Not a palindrome'}")

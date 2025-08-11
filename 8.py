import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
string = "A man, a plan, a canal: Panama"
print(is_palindrome(string))  # Output: True

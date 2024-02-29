def is_valid(s):
    # All vanity plates must start with at least two letters.
    if not s[:2].isalpha():
        return False
    
    # Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a '0'.
    has_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not has_number and i > 1:
                return False
            if i == 2 and char == '0':
                return False
            has_number = True
    
    # No periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False
    
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

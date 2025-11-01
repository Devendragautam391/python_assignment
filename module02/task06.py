
import random

def generate_3_digit_code():
    # each digit 0-9
    digits = [str(random.randint(0,9)) for _ in range(3)]
    return "".join(digits)

def generate_4_digit_code():
    # each digit 1-6
    digits = [str(random.randint(1, 6)) for _ in range(4)]
    return "".join(digits)

if __name__ == "__main__":
    code3 = generate_3_digit_code()
    code4 = generate_4_digit_code()
    print("3-digit code (0-9 each):", code3)
    print("4-digit code (1-6 each):", code4)

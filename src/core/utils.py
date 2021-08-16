from random import randrange, seed
from datetime import datetime
from typing import AnyStr



def get_coupon_code(code_length: int) -> AnyStr:
    try:
        count = 0
        seed = datetime.now()
        coupon = ""
        alphas = "abcdefghijklmnopqrstuvwxyz1234567890"
        while count < code_length:
            coupon = alphas[randrange(0, len(alphas))]
            count += 1
        return coupon
    except:
        print("Enter a valid intergerr")

def generate_password() -> str:
    password = ""
    letters = "a#$w\cde546fgij@&*klmo^pqt7uyz12h3n8brs90!()xv"
    seed = datetime.now()
    count = 0
    while count < 15:
        password += letters[randrange(0, len(letters))]
        count += 1
    return password
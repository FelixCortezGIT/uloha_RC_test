from datetime import datetime
# import random

def validate(rc: str) -> bool:
    if not rc.isdigit():
        return False
    if len(rc) != 10:
        return False
    if int(rc) % 11 != 0:
        return False
    year = int(rc[:2])
    month = int(rc[2:4])
    day = int(rc[4:6])
    if month > 50:
        month -= 50
    try:
        datetime(1900 + year, month, day)
    except ValueError:
        return False
    return True


# def generate() -> str:
#     while True:
#         rc = "".join(str(random.randint(0, 9)) for _ in range(10))
#         print("skusam: ", rc)
#         if validate(rc) and int(rc[2:4]) > 50:
#             return rc
#
#
# rc = generate()
# print("zenske rc: ", rc)

print(validate("0101010000"))
print(validate("9913320000"))
print(validate("7952098374"))
print(validate("abcd123456"))
print(validate("8004309412"))
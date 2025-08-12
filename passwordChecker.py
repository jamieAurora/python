import re

try:
    pwRegex = re.compile(r'\S{8}')
    password = input()
    check1 = 0
    print(pwRegex.search(password))
    check1 = pwRegex.search(password)
    print(check1.group())
    pwRegex2 = re.compile(r'\d+')
    check2 = pwRegex2.search(password)
    print(check2.group())
    pwRegex3 = re.compile(r'[A-Z]+[a-z]+')
    if re.match(pwRegex,password) and re.search(pwRegex2, password) and re.search(pwRegex3, password):
        print("True")
    else:
        print("False")
except AttributeError:
    print("Your password fails.")

# 8 characters long
# both uppercase and lowercase
# at least one number
#[a-z]

name = input("Enter your name: ")
password = input("Enter your password: ")
if len(password) < 8:
    print("Weak : Password must be atleast 8 characters long.")
has_upper = False
has_lower = False
has_digit = False
has_special = False
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

issues = []
if len(password) < 8:
    issues.append("Password must be atleast 8 characters long.")
if name.lower() in password.lower():
    issues.append("Password should not contain your name.")
if not has_upper:
    issues.append("Password must include an UpperCase Letter.")
if not has_lower:
    issues.append("Password must include an LowerCase Letter.")
if not has_digit:
    issues.append("Password must contain an digit.")
if not has_special:
    issues.append("Password must contain an Special Character.")

if issues:
    print("Weak Password.")
    for issue in issues:
        print("-",  issue)
else:
    print("Strong Password.")
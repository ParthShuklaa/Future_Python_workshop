# Define a function for
# for validating an Email
import re
def check(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, s):
        print("Valid Email")
    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':
    # Enter the email
    email = "parthshukla19896@gmail.com"

    # calling run function
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "parthshukla.com"
    check(email)
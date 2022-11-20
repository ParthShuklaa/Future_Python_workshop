from email_validator import validate_email, EmailNotValidError


def check(email):
    try:
        # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v["email"]
        print("True")
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))

check("parthShukla@gmail.com")
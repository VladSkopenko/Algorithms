from email_validator import validate_email, EmailNotValidError

email_for_test = "skopirka2k17@gmail.com"

try:
    v = validate_email(email_for_test)
    print("Email is valid.")
except EmailNotValidError as e:
    print(str(e))

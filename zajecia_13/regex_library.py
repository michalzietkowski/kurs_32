import re

pattern = r"^[\S]+@[\w]+.[\S]{2,}$"

def match_email_address(email):
    if re.match(pattern, email):
        return True
    return False

check = match_email_address("michalzietkowski@gmail.com")
check_2 = match_email_address("michałzietkowski@gmail.com")
print(check)
print(check_2)

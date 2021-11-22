from passlib.context import CryptContext


# Password - This class stores hash of password that is valid(meets the passed standards
# requirements). A password and the standard settings are passed during initialization
# the sha256 hash is stored as 'self.hash' if the password is valid.
# password : The user's inputted password
# caps : The required number of capital letters
# symbol : The required number of symbols
# length : The required password length
class Password:

    def __init__(self, password, caps=1, num=1, symbol=1, length=8):
        self.encrypt = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=50000
        )
        self.hash = ""
        if self.standards(password, caps=caps, num=num, symbol=symbol, length=length):
            self.hash = self.encrypt.hash(password)
        else:
            self.hash = ""

    # verify - checks if the passed password matches the hash that is stored
    # in self.hash
    # password : passed password to be checked against stored hash
    def check(self, password):
        if self.hash == "":
            return False
        else:
            return self.encrypt.verify(password, self.hash)

    # standards - checks whether inputted password meets defined password standards
    # Parameters - password : The user's inputted password
    # caps : The required number of capital letters
    # symbol : The required number of symbols
    # length : The required password length
    def standards(self, password, caps=1, num=1, symbol=1, length=8):
        symbols = ['@', '*', '*', '=', '(', ')', '+', '-', '_', '!', '?']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        space = ' '
        valid_flag = False
        caps_count = 0
        symbol_count = 0
        low_count = 0
        num_count = 0
        space_count = False
        for i in password:
            if i.isupper():
                caps_count += 1
            if i.islower():
                low_count += 1
            if i in symbols:
                symbol_count += 1
            if i in nums:
                num_count += 1
            if i == space:
                space_count = True
        if num_count >= num and symbol_count >= symbol and caps_count >= caps and len(
                password) >= length and not space_count:
            valid_flag = True
        else:
            valid_flag = False
        return valid_flag

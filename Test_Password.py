from Secure import Password

# Test different passwords?
print("Try my password: Password")
wrongPwd = Password("Password")
print(wrongPwd.check("Password"))
print("Try my password: P55wd?")
wrongPwd2 = Password("P55wd?")
print(wrongPwd2.check("P55wd?"))
print("Try my password: P@ssw0rd")
myPwd = Password("P@ssw0rd")
print(myPwd.check("P@ssw0rd"))

pwd_in = ''
pwd_hash = ''
print("\nEnter 'done' when finished")
while pwd_in != 'done':
    if pwd_in != 'done':
        pwd_in = input("Try a Password: ")
        pwd_hash = Password(pwd_in)
        print("Validity: ", pwd_hash.check(pwd_in))

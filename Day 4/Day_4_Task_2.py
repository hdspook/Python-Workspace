# Making a bank balance secure by decorators

username = "admin"
password = "admin"
bank_balance = 25000

def check_balance(func):
    def authorize(entered_username,entered_password):
        if entered_username == username and entered_password == password:
            print(bank_balance)
            return
        print("Sorry Not Authorized To view balance")
        return

    return authorize

print("Please Enter UserName :")
entered_username = input()
print("Please Enter Password :")
entered_password = input()

@check_balance
def preCheck(entered_username,entered_password):
    print("Success")

preCheck(entered_username, entered_password)

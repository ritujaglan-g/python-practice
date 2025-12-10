

bank_accountnumber = input("enter your bank account number ")
withdraw = input("enter the amount to withdraw ")
deposit = input("enter the amount to deposit ")
balance = input("enter your current balance ")

newbalance = float(balance) - float(withdraw) + float(deposit)


bank_accountnumber = bool(bank_accountnumber)

print (f"bank account number:{bank_accountnumber}")
print (f"withdraw ammount:{withdraw}")
print (f"deposit ammount:{deposit}")

print(f"your new balance is : {newbalance}")


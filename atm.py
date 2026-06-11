print("-"*30)
print("Welcome to the Kumail bank")
print("-"*30)
transaction_history=[]
account_name=input("What is your account name ")
account_balance=int(input("What is balance in your account "))
while True :
    dis=input("1. Withdraw\n2. Summary\n3. deposit\n4. transaction\n5. exit\n")
    if dis=="1":
        withdraw_money=int(input("how many amount do you want to withdraw"))
        if withdraw_money <= account_balance :
            account_balance -= withdraw_money
            print(f"Now you have {account_balance}")
            trans=input("do you want to save it in transactions \n1. yes \n2. no")
            if trans== '1':
                tr=(f"you  withdraw {withdraw_money}")
                transaction_history.append(tr)
            else:
                print("ok have a good day")
        elif withdraw_money >= account_balance:
            print (f"you dont have enough money to withraw {withdraw_money}. you have only {account_balance}")
    elif dis=="3":
        deposit_money=int(input("how many amount do you want to Deposit"))
        account_balance += deposit_money
        print(f"Now you have amount {account_balance}")
        trans=input("do you want to save it in transactions \n1. yes \n2. no\n")
        if trans== '1':
            tr=(f"you deposit {deposit_money}")
            transaction_history.append(tr)
        else:
            print("ok have a good day")
        
    elif dis=="2":
        print("-"*30)
        print("     ACCOUNT SUMMARY")
        print("-"*30)
        print(f"Account Name: {account_name}\nAccount balance: {account_balance}  ")
    elif dis== "5":
        break 
    elif dis== "4":
        print("-"*30)
        print("      TRANSACTION HISTORY")
        print("-"*30)
        
        for i in range(len(transaction_history)):
            print(f"{i+1}.{transaction_history[i]}")
        print("-"*30)    
        
print("We hope that you enjoy to use our bank")   
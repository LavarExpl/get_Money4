class Bank_account:
    def account(self,name,account_num,balance):
        self.name = name
        self.account_num = account_num
        self.balance =balance


    def deposit(self,amount):
        self.balance += amount
        print(amount)

    def withdraw(self,amount):

        if amount >0:
            print('Not enough money in account!')
        else:
            self.balance -= amount
            print(amount)
    def get_balance(self):
        print(f"you have {self.balance} left to spend today.")
    def cust_details(self):
        print( f"Name: {self.name}")
        print(f"Account Number: {self.account_num}")
        print(f"Your balance is ${self.balance}")


m  = Bank_account()
m.account('lavar',2342,4354)



m.cust_details()

m.balance

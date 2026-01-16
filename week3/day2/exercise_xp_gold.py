class  BankAccount():
    def __init__(self, balance, user_name, password, authentication = False):
        self.balance = balance
        self.user_name = user_name
        self.password = password
        self.authentication = authentication

    def authenticate(self, user_name, password):
        if self.user_name == user_name and self.password == password:
             self.authentication = True
             return self.authentication
        else :
            self.authentication = False

     
    def deposit(self, amount, user_name, password):
          if self.authenticate(user_name, password) != True:
               raise Exception("wrong details")
          if amount > 0:
               self.balance += amount
               return self.balance   
          else:
            raise Exception('amount must be positive')
       

    def withdraw(self, amount, user_name, password):
       if self.authenticate(user_name, password) != True:
               raise Exception("wrong details")
       if amount > 0:
         self.balance -= amount
         return self.balance   
       else:
          raise Exception('amount must be positive')
      


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance = 0):
        super().__init__(self, balance)
        self.minimum_balance = minimum_balance
        
    

    def withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
             self.balance -= amount   
             return self.balance
        else:
            raise Exception("insufficient balance")
         
class ATM():
    def __init__(self,account_list, try_limit):
       self.account_list = account_list
       self.try_limit = try_limit
       for account in account_list:
           if account is not isinstance(account,(BankAccount, MinimumBalanceAccount)):
               raise Exception("the list must only contain Bank Acxount instances")
       try:
           if try_limit< 0:
               raise ValueError
       except (ValueError,TypeError,Exception): 
        print("value must be positive")
        self.try_limit = 2
    current_tries = 0

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                self.show_account_menu()
            else:   
                current_tries += 1
            if self.try_limit == current_tries:
                raise Exception("you've reached your log in limit")
        

    def show_main_menu(self):
         while True:
            choice = input("select a number(1 or 2): ")
            if choice == 1:
                user_name =input ("username: ")
                password = input("password: ")
                self.log_in(user_name, password)  

            elif choice  == 2:
                break   
    

    
    def show_account_menu(self):
        print("1. deposit ")
        print("2. withdraw")    
        print("3. exit")        
        choice =input("choose an option: ")
        if choice == 1:
            self.amount = int(input("how much to deposit: "))
            self.account.depsit()
            
        elif choice == 2:
            self.amount = int(input("amount to withdraw: "))
        elif choice == 3:
            exit()
my_account = BankAccount(200,"Abdallah", 1993, True)
my_account.deposit(2000, "Abdallah",1993)
my_account = MinimumBalanceAccount(200, 10)
print(my_account)
#Accepts a username and a password.
#Checks the username and the password against all accounts in account_list.
#If there is a match (ie. use the authenticate method), call the method show_account_menu.
#If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

#show_account_menu:
#Accepts an instance of BankAccount or MinimumBalanceAccount.
#The method will start a loop giving the user the option to deposit, withdraw or exit.

        
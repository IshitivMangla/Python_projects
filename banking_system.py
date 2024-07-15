class User:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class BankAccount(User):
    
    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance


    def show_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nBalance: ${self.balance}"
    
    def deposit(self):
        dpAmount = float(input("Enter the amount to be deposited: "))
        print("Amount Deposited")
        self.balance += dpAmount
        return f"New balance: ${self.balance}"
    
    def withdraw(self):
        wdAmount = float(input("Enter the amount to you like to withdraw: "))

        if self.balance < wdAmount:
            print("Insufficient Balance")
        else:
            print("Money Withdrawn")
            self.balance -= wdAmount
            return f"New balance: ${self.balance}"
        
def account_operations(user):

    print("\nEnter the number for the corrosponding operation you want to perform")
    while True:
        print("\nEnter the number for the corrosponding operation again")
        option= int(input("1 See Account Information \n2 Deposit\n3 Withdraw \n4 Quit\n"))

        if option == 1:
            print(user.show_info()) 
        
        elif option == 2:
            print(user.deposit())

        elif option == 3:
            print(user.withdraw())

        elif option == 4:
            break

        else:
            print("Please Enter a Value between 1,2,3,4")
        



while True:
    make_account = input("Do you want to create a new account(yes/no): ").lower()
    
    if make_account == 'yes':
        user_name = input("Enter you Name: ")
        user_age = int(input("Enter your Age: "))
        initBalance = int(input("Enter the initial Balance you want to deposit: "))
        user = BankAccount(user_name, user_age, initBalance)
        account_operations(user)
        break

    elif make_account == 'no':
        print("Thanks for visiting our site")
        break

    else:
        print("Plese enter yes or no only")


        


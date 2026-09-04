class Bankaccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.account_number = 1001

    def deposite(self, amount):
        print("Amount to deposit:", amount)
        self.balance += amount
        print("Balance after deposit is:", self.balance)

    def withdraw(self, amount):
        print("Amount to withdraw:", amount)

        if amount > self.balance:
            print("Error: Insufficient balance")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")
            print("Balance after withdraw is:", self.balance)

    def transfer(self, amount, other_account):
        print("Amount to transfer:", amount)

        if amount > self.balance:
            print("Error: Insufficient balance")
        else:
            self.balance -= amount
            other_account.balance += amount
            print("Amount transferred successfully.")
            print("Balance after transfer is:", self.balance)

    def display(self):
        print("Account holder name:", self.name)
        print("Account number:", self.account_number)
        print("Balance:", self.balance)


name1 = input("Enter first account holder name: ")
name2 = input("Enter second account holder name: ")

p1 = Bankaccount(name1)
p2 = Bankaccount(name2)

p1.deposite(1000)
p1.withdraw(500)
p1.transfer(200, p2)

print("\nFirst Account:")
p1.display()

print("\nSecond Account:")
p2.display()
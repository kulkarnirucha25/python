class bankaccount {
    double balance;

    bankaccount(double balance) {
        this.balance = balance;
    }

    void deposite(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdraw: " + amount);
        } else {
            System.out.println("Insufficient Balance!");
        }
    }

    void display() {
        System.out.println("Current Balance: " + balance);
    }
}

class savingsaccount extends bankaccount {

    savingsaccount(double balance) {
        super(balance);
    }

    void withdraw(double amount) {
        if ((balance - amount) < 100) {
            System.out.println("Withdrawal denied! Minimum balance required.");
        } else {
            super.withdraw(amount);
        }
    }
}

class banktest {
    public static void main(String[] args) {
        savingsaccount acc = new savingsaccount(500);

        acc.deposite(500);
        acc.withdraw(500);
        acc.display();
    }
}

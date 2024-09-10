class account:
    def __init__(self, bal , acc):
        self.balance = bal
        self.account_no = acc
    #Debit Method
    def debit(self, amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("total balance =",self.get_balance())
    #Credit method
    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"is Credited")
        print("total balance =",self.get_balance())

    #for Balance
    def get_balance(self):
        return self.balance
        
acc1 = account(855436,1007)
print(acc1.account_no)
print(acc1.balance) 
acc1.debit(200000)
acc1.credit(10000)       
acc1.credit(855436)  
acc1.debit(50000)
acc1.debit(100000)
acc1.debit(200000)
acc1.debit(50000)
acc1.debit(50000)
acc1.debit(30000)
# Day 8 of practicing git
# This would go the Day5 branch and later merged to the main itself.

# Encapsulation : Wrapping data and functions into a single unit (object). (data + function)

class Account:
  def __init__(self, bal,acc):
    self.balance = bal
    self.account_no = acc
  def debit(self,amount):
    self.balance -= amount
    print("Rs.",amount,"was debited.")
    print("Total balance: ",self.get_balance())
  def credit(self, amount):
    self.balance += amount
    print("Rs.",amount,"was credited.")
    print("Total balancce: ",self.get_balance())
  def get_balance(self):
    return self.balance
 
acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)

acc1.credit(50000)
acc1.debit(10000)
acc1.get_balance()   

#Thus we created a banking update system. This proves encapsulation as we only showed what was neccessary and hid everything else in function and object.
 
# This code is know pushed to branch Day5 and would be merged to main branch by switching to main branch and using (git merge Day5) and then (git push origin main).Let's do it.        
  
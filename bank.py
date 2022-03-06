class bank_account:
      def __init__(self):
          print('welcome to the xyz bank account')

      def open_account(self,balance):
          name=input('enter your name:')  
          self.balance=balance
          a=('name:',name,'balance:',balance)
          print('your account number is :123456')

      def deposit(self):
          amount=int(input('enter the amount to be deposited:'))
          self.balance+=amount
          print ('your total balance is :', amount)

      def withdraw(self):
          draw_amount=int(input('enter the amount to be withdraw:'))  
          self.draw_amount=draw_amount
          if self.draw_amount<self.balance:
             b=self.balance-self.draw_amount
             print('current balance:',b)
          else:
               print('Insufficient balance')
                 
     
x=bank_account()
balance=0
x.open_account(balance)
x.deposit()
x.withdraw()
print('Thank you for using our banking service')

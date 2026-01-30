from models.Bankaccount import BankAccount

my_account = BankAccount(1000)
your_account = BankAccount(500)

out_account = my_account + your_account

out_account -= your_account
print(out_account)
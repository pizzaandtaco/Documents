class Bank:
    def __init__(self):
       self.accounts = {}

       def create_account(self, account_number, initial_balance):
           if account_number not in self.accounts:
               self.accounts[account_number] = initial_balance
               print(f"Akun [account_number] berhasil dibuat dengan saldo")
           else:
               print("Akun dengan nomor tersebut sudah ada. Silahkan pilih yang lain")
    
       def deposit(self, account_number, amount):
           if account_number in self.accounts:
               self.accounts[account_number] += amount
               print(f"Berhasil menambahkan {amount} ke akun {account_number}")
           else:
               print("Akun tidak ditemukan")
    
       def withdraw(self, account_number, amount):
           if account_number in self.accounts:
               if amount <= self.accounts[account_number]:
                   self.accounts[account_number] -+ amount
                   print(f"Berhasil mengambil {amount} dari akun {account_number}")
               else:
                   print("Saldo tidak mencukupi untuk transfer")
           else:
               print("Salah satu atau kedua akun tidak ditemukan")

       def check_balance(self, account_number):
           if account_number in self.accounts:
               print(f"Saldo akun {account_number}: {self.accounts[account_number]}")
           else:
               print("Akun tidak ditemukan")
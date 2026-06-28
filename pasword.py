import tkinter as tk
class passwordmanager:
     def _init_(self, master):
          self.master = master
          self.master.title("password manager")

          self.account_label = tk.Label(master, text="Account:")
          self.account_label.grid(row=0, coulumn=0, padx=10, pady=5)

          self.account_entry= tk.Entry(master)
          self.account_entry.grid(row=0, column=1, padx=10, pady=5)

          self.password_label= tk.label(master, text="password:")
          self.password_label.grid(row=1, column=0, padx=10, pady=5)

          self.password_entry= tk.Entry(master, show="*")
          self.password_entry.grid(row=1, column=1, padx=10, pady=5)

          self.add_button= tk.Button(master, text="add password", command=self.add_password)
          self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

          self.update_button=tk.Button(master, text="update password", command=self.update_password)
        
          self.update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")


          self.retrieve_button= tk.Button(master, text="retrieve password", command=self.retrieve_password)
          self.retrieve_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

          self.delete_button=tk.button(master, text=" delete password", command=self.delete_password)
          self.delete_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

          self.delete_button=tk.button(master, text=" display all passwords", command=self.display_)
          self.delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

          self.output_label= tk.Label(master, text="")
          self.output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
            
          self.manager= passwordmanager()



     def  add_password(self):

          account=self.account_entry.get()
          password= self.password_entry.get()
          if account and password:
               self.manager.add_password(account, password)
               self.output_label.config(text=f"password for{account} added successfully")
          else:
               self.output_label.config(text="Please enter both account and password")

def update_password(self):
     account= self.account_entry.get()
     new_password= self.password_entry.get()
     if account and new_password:
          self.manager.update_password(account, new_password)
          self.output_label.config(text=f"password for {account} updated successfully")
     else:
          self.output_label.config(text="Please enter both account and newpassword")


          def retrieve_password(self):
               account= self.account_entry.get()
     
     if account:
          password= self.manager.get_password(account)
          if password:
           self.output_label.config(text=f"password for {account} updated successfully")
     else:
          self.output_label.config(text="Please enter both account and newpassword")


def delete_password(self)
     account = self.account_entry.get()
     if account:
          self.manager.delete_password(account)
          self.output_label.config(text=f"password for {account} updated successfully")
     else:
          self.output_label.config(text="Please enter both account and newpassword")

def display_password(self):
     passwords= self.manager.display_all_password()
     if passwords:
          self.output_label.config(text=passwords)
     else:
          self.output_label.config(text="No passwords stored")

          class Passwordmanager:
               def  __init__(self):
                    self.passwords ={}

               def add_password(self, account, password):
                         self.password[account]= password

               def update_password(self, account, new_password):
                              if account in self.password:
                                   self.password[account]= new_password

               def get_password(self, account):
                    return self.password.get(account)
               def delete_password(self,account):
                    if account in self.password:
                         del self.password[account]

               def display_all_password(self):      
                    return self.password   

          def main():
              root= tk.Tk()
              app =PasswordManagerUI(root)
              root.mainloop()

          if __name__ =="__main__":
               main()
























































































































































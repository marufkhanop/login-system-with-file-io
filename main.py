import csv
import re
import os

def main():
  print("-----------")
  print("1. Sign Up")
  print("2. Log in")
  print("-----------")
  option = ask_option()
  print("-----------")
  print()
  print("----------------")
  while True:
    if option == 1:
      username = ask_username()
      password = ask_pass()
      print(password)
      valid = file_exist(username)
      if valid == True:
        signup_done(username, password)
        break
      else:
        continue
      
    elif option == 2:
      username = ask_username()
      password = ask_pass()
      valid = match_user_and_pass(username, password)
      if valid:
        print("----------------")
        print()
        print("You Logged in")
        break
      else:
        print("Wrong information")
        print()
      

def ask_option():
  while True:
    try:
      num = int(input("select 1 or 2: "))
      if num == 1 or num == 2:
        return num
    except ValueError:
      print("not an option")
      continue
def ask_username():
  while True:
    name = input("Username: ")
    if len(name) == 0:
      exit()
    if 4 <= len(name) <= 12:
      match = re.search(r"^[a-z]+$", name)
      if match:
        return name
      else:
        print("use only letters")
        continue
    else:
      print("keep it between 4-12 letter")
      continue
def ask_pass():
  while True:
    pas = input("Password: ").strip()
    if 6 <= len(pas):
      return pas
    else:
      print("Should contain atleast 6 character")
      continue
    
def file_exist(username):
  with open("data.csv", "a") as file:
    pass
  with open("data.csv") as file:
      files = csv.DictReader(file)
      for dicts in files:
        if dicts["username"] == username:
          print("username already exists")
          print()
          return False
        else:
          pass
      return True
    
def signup_done(username, password):
  file_exist = os.path.isfile("data.csv") and os.path.getsize("data.csv")
  with open("data.csv", "a") as file:
    files = csv.DictWriter(file, fieldnames=["username", "password"])
    if not file_exist:
      files.writeheader()
    files.writerow({"username" : username, "password" : password})
  print("----------------")
  print()
  print("Signed up Successfully")
  
def match_user_and_pass(name, pas):
  with open("data.csv", "a") as file:
    pass
  with open("data.csv") as file:
    files = csv.DictReader(file)
    for dicts in files:
      if dicts["username"] == name and dicts["password"] == pas:
        return True
      else:
        pass
    return False
if __name__ == "__main__":
  main()
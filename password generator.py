import secrets

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*_+:?"

password_length = int(input("Enter the length of the password you want :  "))
value = int(input("how much : "))

for password in range(value):
  password = " "
  for c in range(password_length):
    password = password + secrets.choice(alpha)
  print(password)



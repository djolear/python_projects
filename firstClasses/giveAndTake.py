from customer import Customer

custOne = Customer("Bob", 1000000.89)

print(custOne.name)
print(custOne.balance)
custOne.withdraw(1000000.89)
print(custOne.balance)


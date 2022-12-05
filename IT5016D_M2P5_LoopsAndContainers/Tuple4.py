# Tuple4.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 42: #2

# Tuple.py
#
# @ author: A. N. Other
# date: September 2016

# (Name, Balance, Address, Number)
bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))

# print the total number of accounts
print("The number of bank accounts is ", len(bank_accounts), "\n")

# show names and balances
for i in bank_accounts:
    print("The name is ", i[0], " and the balance is $", i[1])
print("\n")

# show only names with addresses
for i in bank_accounts:
    if len(i) > 2:
        print("The name is ", i[0], " and the address is ", i[2])
print("\n")

# show customers with less than $100 balance
low_balance = 100
for i in bank_accounts:
    if i[1] < low_balance:
        print("A customer with less than ${0} is {1}".format(
              low_balance,
              i[0]))
print("\n")

# show only customers with no phone number or no addresses
for i in bank_accounts:
    if len(i) <= 2:
        print("A customer with either no number or address is ", i[0])
    # index <=2 because 3rd and 4th item is the address and number
print("\n")

# showing the highest and lowest balances
# get a list of the balances
balances_list = []
for i in bank_accounts:
    balances_list.append(i[1])
print("The highest balance is ${0}.".format(max(balances_list)))
print("The lowest balance is ${0}.".format(min(balances_list)))
print("The sum of all balances is ${0}.".format(sum(balances_list)), "\n")

# showing all details for all customers
print("Showing details for all customers...")
for i in bank_accounts:
    print("\n")
    for customer_detail in i:
        print(customer_detail, end=" ")
print("\n")

# showing only customers with more than $5k or less than $0
print("\nShowing details for our rich and poor customers...", end="")
for i in bank_accounts:
    if 0 > i[1] or i[1] > 5000:
        print("\n")
        for customer_detail in i:
            print(customer_detail, end=" ")
# IfStatementPractice3.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 34 : Challenge 3: Cell Phone Bill

print("Let us calculate your bill")

# let user input variables
minutes_used = int(input("Number of minutes used:"))
text_message = int(input("Number of messages sent:"))

# assign prices in cents and then convert to dollars in the end
base_charge = 1500
additional_charge = 44


print("Base charge : $", base_charge / 100)
print("Additional flat charge: $", additional_charge/100)

# compute for extra minutes cost
if minutes_used > 50:
    minutes_used = minutes_used - 50
else:
    minutes_used = 0

extra_minutes_charge = minutes_used * 25
print("Additional minutes charge: $",
      extra_minutes_charge / 100)

# compute for extra text cost
if text_message > 50:
    text_message = text_message - 50

else:
    text_message = 0

extra_message_charge = text_message * 15
print("Additional text message charge: $",
      extra_message_charge / 100)

# calculate for total bill
gross_bill = (base_charge
              + additional_charge
              + extra_minutes_charge
              + extra_message_charge) / 100
tax = gross_bill * 0.05
net_bill = gross_bill + tax

print("Total before tax: $", gross_bill)
print("Tax (5%): $", round(tax, 2))
print("Net bill: $", round(net_bill, 2))

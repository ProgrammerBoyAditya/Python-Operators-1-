# Taking the total amount as input from the user
amount=int(input("Please enter the total amount required for withdrawl :"))

# Denominations for different notes
note1 =  amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("Notes of 100 rupees are :",note1)
print("Notes of 50 rupees are :",note2)
print("Notes of 10 rupees are :",note3)
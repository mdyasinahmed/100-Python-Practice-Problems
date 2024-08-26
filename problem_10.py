# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

costPrice = int(input('Enter Cost Price: '))
sellingPrice = int(input('Enter Selling Price: '))

print("Its a Profit!") if sellingPrice>costPrice else print("Its a Loss!")
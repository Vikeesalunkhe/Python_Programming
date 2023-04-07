# program 7: calculate profit or loss ,write a program that takes the cost price and selling price (take it hardcoded)and  calculate its profit or loss


sellingprice = float(input("Enter your number:"))
costprice = float(input("Enter your number:"))

if sellingprice > costprice:
    print("Profit is ", sellingprice - costprice)
elif sellingprice < costprice:
    print("Loss is ", costprice - sellingprice)
else:
    print("No profit no loss")

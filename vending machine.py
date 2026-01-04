# Define the list of products with their prices
Products = {
1:{"name":"Pepsi", "price":5},
2:{"name":"Water", "price":3},
3:{"name":"7up", "price":2},
4:{"name":"Miranda", "price":4}, 
5:{"name":"Hot Chocolate", "price":8}, 
6:{"name":"Coffee", "price":10}, 
7:{"name":"Tea", "price":7.5}, 
8:{"name":"Ice Tea", "price":8}, 
9:{"name":"Biscuit", "price":4.5}, 
10:{"name":"Chocolate", "price":3.5}, 
}
#print welcome message 
print("=== Welcome to the Vending Machine ===\n ")
# Display all products 
for key, value in Products.items():
    print(f"{key}. {value['name']} -{value['price']} SAR")
# Get the user,s product choice
choice = int(input("\n Enter the number of product:"))
# Check if the product exists
if choice in Products:
# Ask the user to insert money
     money =float(input("insert money (SAR): "))
     price = Products[choice]["price"]
# If money is more than the price 
     if money  > price:
         change = money - price
         print(f"\n You bought {Products[choice]['name']}")
         print(f" change: {change} SAR")
# If miney equals the price 
     elif money == price: 
         print(f"\n You bought {Products[choice]['name']}")
         print("No change")
# If money us less than the price 
     else:
         print("\n Not enough money")
# If the product number is invalid 
else:
# Loop to allow buying another product
    print("\nInvalid choice")  
while True:
    another = input("\n Do you want to buy another product ? (yes/no): ")
# If user wants to buy again
    if another .lower() == "yes":
        print("\n=== Products ===")
# Display products again
        for key, value in Products. items():
            print(f"{key}. {value['name']} - {value['price']}SAR")
# Get new choice 
        choice = int(input("\n Enter the number of product:"))
# Check valid choice 
        if choice in Products :
            money = float(input("insert money (SAR): "))
            price = Products[choice]['price']
# Same payment logic 
            if money > price:
                change = money - price
                print(f"\n You bought {Products[choice]['name']}")
                print(f"change: {change} SAR")
            elif money == price:
                  print(f"\n You bough {Products[choice]['name']}")
                  print(" Not change")
            else: 
                 print("\n Not enough money")
        else:
             print("\n Invalid choice")
# If user dose not want to continue 
    elif another.lower() == "no":
         print("\n Thank you for using the vending machine")
         break
# If user enters something else 
    else:
         print("please enter 'yes' or 'on'  ")
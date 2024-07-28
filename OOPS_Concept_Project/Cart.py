import re


class Cart:

    def __init__(self, items, qty):
        self.Quantity = qty
        self.FoodItems = self.__AddtoCart(items)

    def __AddtoCart(self, items):
        foodDict = {}

        for i in self.Quantity:
            if i > len(items) or i <= 0:
                print(f"Invalid choice: {i}")
                return {}
            if i in foodDict:
                foodDict[i] += 1
            else:
                foodDict[i] = 1
        return foodDict

    def ProcessOrder(self, fooditems):
        Total = 0

        for item in self.FoodItems:
            price = self.FoodItems[item]*fooditems[item - 1].Price
            Total += price
            print(f"{fooditems[item - 1].Name} X {self.FoodItems[item]} = {price} ")
        print(f"Total: {Total}")

        self.ProcessPayment(Total)


    def ProcessPayment(self, amount):
        print("Payment Options:")
        print("1. Cash on Delivery")
        print("2. UPI (GPay, PhonePe, Paytm)")
        choice = input("Choose payment method (1 or 2): ")

        if choice == '1':
            print("Cash on Delivery selected")
            print("Your Order is on the Way....")
        elif choice == '2':
            upi_id = input("Enter UPI ID: ")
            if not re.match(r"^[a-zA-Z0-9.\-]{2,256}@[a-zA-Z]{2,64}$", upi_id):
                print("Invalid UPI ID")
                return
            print("UPI Payment selected")
            print("Your Order is on the Way....")
        else:
            print("Invalid payment method")


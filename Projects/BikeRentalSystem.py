# Bike Rental System

class BikeShop:
    def __init__(self, stock):
        self.stock = stock   # initial stock

    def displaybike(self):
        print("Total bikes available:", self.stock)

    def rentforbike(self, q):
        if q <= 0:
            print("Enter positive value")
        elif q > self.stock:
            print("Enter value less than available stock")
        else:
            cost = q * 100
            self.stock -= q   # reduce stock after renting
            print("Total cost:", cost)
            print("Remaining bikes:", self.stock)


# Create object ONCE (not inside loop)
obj = BikeShop(1000)   # initial stock = 10 bikes

while True:
    uc = int(input('''
1. Display stock
2. Rent a bike
3. Exit
Enter choice: '''))

    if uc == 1:
        obj.displaybike()

    elif uc == 2:
        n = int(input("Enter quantity: "))
        obj.rentforbike(n)

    elif uc == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
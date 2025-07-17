'''class employee:

    currentYear = 0
    startYear = 0
    name = ""
    iD = 0

    def experience (self):
        yearOfExp = self.currentYear - self.startYear
        print(f"Year of experince: {yearOfExp}")


employee1 = employee()
employee1.currentYear = 2025
employee1.startYear = int(input("Which year were you hired? "))

employee1.experience()
'''
# Detergent Company Sales Application

class DetergentProduct:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class DetergentCompany:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Available Detergent Products:")
        for product in self.products:
            print(f"ID: {product.product_id} | Name: {product.name} | Price: ${product.price:.2f}")

def main():
    company = DetergentCompany()

    # Add sample products
    company.add_product(DetergentProduct(1, "Premium Laundry Detergent", 12.99))
    company.add_product(DetergentProduct(2, "Eco-Friendly Dish Soap", 8.49))
    company.add_product(DetergentProduct(3, "Stain Remover Spray", 6.99))

    while True:
        print("\nDetergent Company Sales System")
        print("1. View available products")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            company.display_products()
        elif choice == '2':
            print("Thank you for using our system. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()

number_of_items = int(input("Enter number of food items: "))
total_sales = 0
meet = 0
below = 0

for i in range(number_of_items):
    sales = int(input(f"Enter sales for Item {i + 1}: "))
    total_sales += sales

    if sales >= 500:
        meet += 1
    else:
        below += 1

def calculate_average(total_sales, number_of_items):
    average = total_sales / number_of_items
    return average


print("CANTEEN SALES REPORT")
average = calculate_average(total_sales, number_of_items)
print(f"Average Sales: {average:.2f} | Meeting Target: {meet} | Below Target: {below}")


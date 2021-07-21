# Here i will be making a billing system

list_of_items = []
cost_of_items = []


def print_bill():
    total_cost = 0
    for i in range(0, len(list_of_items)):
        total_cost = total_cost + cost_of_items[i]
    print("Items\tCost")
    for i in range(0, len(list_of_items)):
        print("{0}\t{1}".format(list_of_items[i], cost_of_items[i]))
    print("Total bill generated: {}".format(total_cost))


def print_cost_only():
    total_cost = 0
    for i in range(0, len(list_of_items)):
        total_cost = total_cost + cost_of_items[i]
    print("Total bill generated: {}".format(total_cost))


def billing():
    n = int(input("Enter the number of items: "))
    for i in range(0, n):
        item_name = input("Enter the name of the item {}: ".format(i))
        list_of_items.append(item_name)
        cost = float(input("Enter the cost of the item {}: ".format(i)))
        cost_of_items.append(cost)


if __name__ == '__main__':
    billing()
    while True:
        bill_req = int(input("Do you want the bill for your purchase press 0 for No and 1 for Yes: "))
        if bill_req == 0:
            print_cost_only()
            print("Thanks for your purchase, please visit again!")
            break
        elif bill_req == 1:
            print_bill()
            print("Thanks for your purchase, please visit again!")
            break
        else:
            print("Please type 1 or 0")
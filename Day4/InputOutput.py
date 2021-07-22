# Here i am extending the billing system that i did in Day3,
# The system will get the item name and quantity and automatically
# Generated the bill
# Here i assume that each item has the same price of $20


def make_item_list():
    item_lists = []
    item_qty = []
    while True:
        stop = input("Do you want to add items in your list, type yes or no: ").lower()
        if stop == "yes":
            item_name = input("Enter the item name: ")
            quantity = int(input("Quantity of the item: "))
            item_lists.append(item_name)
            item_qty.append(quantity)
        elif stop == "no":
            break
        else:
            print("Please enter yes or no")
    with open("itemsLists.txt", 'w') as item_list:
        length_of_list = len(item_lists)
        item_list.write(str(length_of_list))
        item_list.write("\r")
        for item in item_lists:
            print(item, file=item_list)
        for quantity in item_qty:
            print(quantity, file=item_list)


def read_items_from_file(item_read_list):
    list2 = open("itemsLists.txt", 'r')
    for line in list2:
        item_read_list.append(line.strip('\n'))
    print(item_read_list)
    list2.close()


def billing(item_lists):
    no_of_items = int(item_lists[0])
    list_of_items = []
    for i in range(1, no_of_items+1):
        list_of_items.append(item_lists[i])
    quantity_list = []
    for i in range(no_of_items+1, len(item_lists)):
        quantity_list.append(int(items_list[i]))
    total_cost = 0
    cost_per_item_list = []
    for i in quantity_list:
        cost_per_item_list.append(i*20)
        total_cost = total_cost + (20*i)
    print("Total Cost: {}".format(total_cost))
    is_bill_required = input("Do you want a bill?\n").lower()
    if is_bill_required == "yes":
        give_bill(list_of_items, quantity_list, total_cost,cost_per_item_list)
    else:
        print("Thanks for shopping with us please come again!")


def give_bill(items_list1, quantity, cost_total,cost_per_item):
    n = len(items_list1)
    with open("bill.txt", 'w') as bill:
        bill.write("********************BILL********************\n")
        bill.write("Item Purchased\t\tQuantity\t\tCost\r")
        for i in range(0, n):
            bill.write("\t{0}\t\t\t\t{1}\t\t\t{2}\r".format(items_list1[i], quantity[i], cost_per_item[i]))
        bill.write("Total payable amount: {}\r".format(cost_total))
        bill.write("Thanks for shopping with us, please come again!\r")
        bill.write("********************END********************\r")


if __name__ == '__main__':
    items_list = []
    read_items_from_file(items_list)
    billing(items_list)

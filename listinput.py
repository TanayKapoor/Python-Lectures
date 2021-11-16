list_ip = []

size = int(input("Enter the size of the list: "))

for i in range(0, size):
    element = input("Enter element: ")
    list_ip.append(element)

choice = input("Do you want to add another list to it?")
if choice.upper() == "YES":
    size = int(input("Enter the size of the list: "))

    for i in range(0, size):
        element = input("Enter element: ")
        list_ip.append(element)
    print("list is", list_ip)

else:
    print("list is", list_ip)

res = [int(ele) if ele.isdigit() else ele for ele in list_ip]

res1 = len(list(i for i in res if isinstance(i, int)))
res2 = len(list(i for i in res if isinstance(i, str)))
print("number of integers in list", res1)
print("number of string in list", res2)




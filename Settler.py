input_list = []
i = 0
while True:
    item = input(f"Enter your {i}th item (!! to exit): ")
    if item == "!!":
        break
    input_list.append(item)
    i += 1

priority_list = []

def priority_append(item):
    for i in range(len(priority_list)):
        print("Which one is most important?")
        print(f"1. {priority_list[i]}") # desirable situation
        print(f"2. {item}")
        ans = input()
        if ans == "1":
            priority_list.insert(i, item)
            return
    priority_list.append(item)
        
for item in input_list:
    priority_append(item)

priority_list.reverse()
print("Priority list is: ")
for item in priority_list:
    print(item)
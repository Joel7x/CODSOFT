todo_list = []

def add_item(item):
    todo_list.append(item)
    print("Item added to the todo list.")

def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print("Item removed from the todo list.")
    else:
        print("Item not found in the todo list.")

def display_list():
    print("Todo List:")
    for item in todo_list:
        print("- " + item)

while True:
    print("\n1. Add item to todo list")
    print("2. Remove item from todo list")
    print("3. Display todo list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        display_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

file = "todo.list.txt"
print("Todo List")


file = open("todo.list.txt","w")
file.write("todo list")

while True:
  choice = input("add task\n2.view\n3.exit\nEnter Here:")


  if choice == "1":
    file = open("todolist.txt","a")
    task = input("enter your  task")
    file.write("\n")
    file.close()

  if choice == "2":
    file = open("todolist.txt","r")
    print(file.read())

  if choice == "3":
    break 


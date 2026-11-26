
from tasks import *
from menu import *
from queue import taskQueue, addQueue, deleteQueue, showQueue
from stack import *
from linkedList import *


def startApp():
    while True:
        showMenu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter task name: ").strip()

                if not name:
                    print("Task name cannot be empty!")
                    continue

                push(tasks, taskQueue)
                addTask(name)

            elif choice == 2:
                taskID = int(input("Enter task ID: "))
                task = findTask(taskID)

                if task:
                    name = input("Enter new task name: ").strip()

                    if name:
                        push(tasks, taskQueue)
                        updateTask(taskID, name)
                    else:
                        print("Task name cannot be empty!")
                else:
                    print("Task not found!")

            elif choice == 3:
                taskID = int(input("Enter task ID: "))

                if findTask(taskID):
                    push(tasks, taskQueue)
                    removeTask(taskID)
                else:
                    print("Task not found!")

            elif choice == 4:
                showTask()

            elif choice == 5:
                taskID = int(input("Enter task ID: "))
                task = findTask(taskID)

                if task:
                    if task["status"] == "pending":
                        push(tasks, taskQueue)
                        addQueue(taskID)
                    else:
                        print("Task is already completed!")
                else:
                    print("Task not found!")

            elif choice == 6:
                if taskQueue:
                    push(tasks, taskQueue)

                    taskID = deleteQueue()
                    task = findTask(taskID)

                    if task:
                        task["status"] = "completed"
                        addCompleted(task)
                        print("Task completed successfully!")
                else:
                    print("Queue is empty!")

            elif choice == 7:
                undo(tasks, taskQueue)

            elif choice == 8:
                showQueue()

            elif choice == 0:
                print("Exiting Task Management System...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

        except Exception as e:
            print("Error:", e)


startApp()

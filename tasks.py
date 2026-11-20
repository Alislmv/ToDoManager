tasks = []
nextID = 1

def addTask(name):
    global nextID

    task = {
        "id": nextID,
        "name": name,
        "status": "pending"
    }

    tasks.append(task)
    nextID += 1

    print("Task added successfully!")


def showTask():
    if not tasks:
        print("Task list is empty!")
        return

    for task in tasks:
        print(f"ID: {task["id"]}")
        print(f"Name: {task["name"]}")
        print(f"Stuatus: {task["status"]}")


def findTask(taskID):
    for t in tasks:
        if t["id"] == taskID:
            return t

def updateTask(taskID, taskName):
    task = findTask(taskID)

    if task:
        task["name"] = taskName
        print("task uptaded successfully!")
    else:
        print("Task not found")

def removeTask(taskID):
    task = findTask(taskID)

    for t in tasks:
        if t["id"] == taskID:
            task.remove(t)
            return True

    print("Not found")
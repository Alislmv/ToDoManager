completedTask = []


def addCompletedTask(task):

    node = {}

    node["data"] = task.copy()
    node["next"] = None

    if completedTask is None:
        completedTask.append(node)
        return

    current = completedTask
    while current["next"] is not None:
        current = current["next"]

    current["next"] = node


def showCompletedTasks():
    if completedTask is None:
        print("No completed tasks!")
        return

    current = completedTask
    while current is not None:
        task = current["data"]
        print(f"ID: {task["id"]}, Name: {task["name"]} ")
queue = []


def addTaskToQueue(taskID, tasks):
    task = None
    for item in tasks:
        if item["id"] == taskID:
            task = item
            break

    if task is None:
        print("Task not found!")
        return

    if task["status"] != "pending":
        print("Only pending tasks can be added to the queue!")
        return

    for queuedTask in queue:
        if queuedTask["id"] == taskID:
            print("Task is already in the queue!")
            return

    queue.append(task)
    print("Task '{}' added to queue!".format(task["name"]))


def completeNextTask():
    if not queue:
        print("Queue is empty!")
        return None

    task = queue.pop(0)
    task["status"] = "completed"
    print("Task '{}' completed!".format(task["name"]))
    return task


def showQueue():
    if not queue:
        print("Queue is empty!")
        return

    print("Task queue:")
    position = 1
    for task in queue:
        print(position, ". ID:", task["id"], "| Name:", task["name"])
        position += 1
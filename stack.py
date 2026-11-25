stack = []


def push(task):
    stack.append(task.copy())


def undo(tasks):
    if not stack:
        print("Undo history is empty!")
        return

    lastTask = stack.pop()

    for index, task in enumerate(tasks):
        if task["id"] == lastTask["id"]:
            del tasks[index]
            print("Undo: '{}' deleted.".format(lastTask["name"]))
            return

    print("Task was already deleted")
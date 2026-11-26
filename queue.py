from tasks import *

taskQueue = []


def addQueue(taskID):
    try:
        if taskID in taskQueue:
            print("task is already in queue")
            return False

        taskQueue.append(taskID)
        print("task added to queue")
        return True

    except Exception as e:
        print(e)
        return False


def deleteQueue():
    if not taskQueue:
        print("queue is empty")
        return None
    return taskQueue.pop(0)


def showQueue():
    try:
        if not taskQueue:
            print("queue is empty")
            return

        for taskID in taskQueue:
            task = findTask(taskID)
            print(f"ID: {taskID} - {task['name']} ({task['status']})")

    except Exception as e:
        print("Error:", e)
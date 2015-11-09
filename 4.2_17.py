import sys

class Task(object):
    def __init__(self, name, time, precedence):
        super(Task, self).__init__()
        self.name = name
        self.time = time
        self.precedence = precedence

class Procesor(object):
    def __init__(self):
        super(Task, self).__init__()
        self.task = []

    def lastEndTime(self):
        return len(self.task)

    def addWork(task):
        for x in range(task.time):
            self.task.append(task.name)
        
class Procesors(object):
    def __init__(self, number):
        super(Task, self).__init__()
        self.num = number
        self.procs = []
        for i in range(number):
            procs.append(Procesor())

    def getNext(self):
        min = sys.maxint
        last = Procesor()
        for proc in delf.procesors:
            currentTime = proc.lastEndTime()
            if currentTime < min:
                min = currentTime
                last = proc

        return last


    def getLast(self):
        max = 0
        last = Procesor()
        for proc in delf.procesors:
            currentTime = proc.lastEndTime()
            if currentTime > max:
                min = currentTime
                last = proc

        return last

def heur(procesors, tasks):
    taskTotalTime = 0
    for task in tasks:
        taskTotalTime += task.time

    lastProcesorsEndTime = 0
    for procesor in procesors:
        lastProcesorsEndTime += procesors.lastEndTime()

    h = (taskTotalTime + lastProcesorsEndTime) / procesors.num

    maxF = (procesors.getLast()).time

    if h > maxF:
        return maxF - h
    return 0


def solve(tasks, prereqizits, result = [[], [], []], step = 0, proces = 0):
    if proces == len(tasks):
        return result
    if prereqizits[proces] == []:
        for x in range(len(result)):
            if len(result[x]) > step:
                if (result[x])[step] != None:
                    step = step +1
                    print(proces)
                    print(result)
            else:
                for q in range(tasks[proces]):
                    result[x].append(proces)
                for i in range(len(prereqizits)):
                    for j in range(len(prereqizits[i])):
                        if prereqizits[i][j] == proces:
                            prereqizits[i].pop(j)
                break
    print(prereqizits)
    result = solve(tasks, prereqizits, result, step, proces+1)
    return result


def main():

    taskstime = [4, 2, 2, 20, 20, 11, 11]
    prereqizits = [[], [], [], ["T1"], ["T1"], ["T4"], ["T1", "T3"]]

    tasks = []

    for x, i in enumerate(taskstime):
        tasks.append(Task("T"+str(x), i, prereqizits[x]))

    for x in tasks:
        print(x.name, x.time, x.precedence)
 

if __name__ == '__main__':
    main()
import sys

class Task(object):
    def __init__(self, name, time, precedence):
        super(Task, self).__init__()
        self.name = name
        self.time = time
        self.precedence = precedence

    def getPossibleTasks(tasks):
        for task in tasks:
            #if len(task.precedence) == 0:
            return task
        return None


class Procesor(object):
    def __init__(self, i = -1):
        super(Procesor, self).__init__()
        self.name = i
        self.task = []

    def lastEndTime(self):
        return len(self.task)

    def addWork(self, task):
        for x in range(task.time):
            self.task.append(task.name)
        
class Procesors(object):
    def __init__(self, number):
        super(Procesors, self).__init__()
        self.num = number
        self.procs = []
        for i in range(number):
            self.procs.append(Procesor(i))

    def getNext(self):
        min = self.procs[0].lastEndTime()
        last = self.procs[0]
        for proc in self.procs:
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


def solve(procesors, tasks):
    #while len(tasks) == 0:
    #    for task in tasks:
    #        if testPrecedence(task, procesors) == True:
    #            for procesor in procesors:
    #                pass

    while len(tasks) > 0:
        nextProc = procesors.getNext()
        nextTask = Task.getPossibleTasks(tasks)
        if nextTask != None:
            nextProc.addWork(nextTask)
            tasks.remove(nextTask)


def main():
    taskstime = [4, 2, 2, 20, 20, 11, 11]
    prereqizits = [[], [], [], ["T1"], ["T1"], ["T4"], ["T1", "T3"]]

    tasks = []

    for x, i in enumerate(taskstime):
        tasks.append(Task("T"+str(x), i, prereqizits[x]))

    for x in tasks:
        print(x.name, x.time, x.precedence)

    procesors = Procesors(3)

    solve(procesors, tasks)

    for proc in procesors.procs:
        print(proc.task)
 

if __name__ == '__main__':
    main()

'''
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
'''
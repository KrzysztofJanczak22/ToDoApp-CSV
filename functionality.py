import csv
import os

class Task:
    def __init__(self, id,title,date,status,note):
        self.id = id
        self.title = title
        self.date = date
        self.status = status
        self.note = note
    def opennote(self):
        self.path = os.getcwd() + f'/notes/{self.id}.txt'
        print(self.path)
        os.startfile(self.path)
    def createnote(self):
        with open(f'notes/{self.id}.txt','w'):
            pass
        self.opennote()
    def editTitle(self,newTitle):
        self.title = newTitle

    def editStatus(self,status):
        self.status = status






def Readcsv(filepath='tasks.csv') -> list:
    tab = []
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter =';')
        for row in reader:
            tab.append(row)
    return tab

def Savecsv(tab,filepath='tasks.csv'):
    with open(filepath,'w', encoding='UTF8', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        for i in range(len(tab)):
            task = tab[i]
            row = [task.id , task.title, task.date, task.status, task.note]
            csv_writer.writerow(row)


def InitTasksFromTab(tab,Task) -> list:
    tab_task = []
    for record in tab:
        task_id = int(record[0])
        title = record[1]
        date = record[2]
        status = record[3]
        note= record[4]
        task = Task(task_id,title,date,status,note)
        tab_task.append(task)
    return tab_task

def addTask(Task,check_date,title,date, tab_task):
    if check_date == True:
        task = Task(len(tab_task),title,date,'0','false')
    else:
        task = Task(len(tab_task), title, 'None', '0', 'false')
    tab_task.append(task)





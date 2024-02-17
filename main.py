from PyQt5 import QtCore, QtGui, QtWidgets
import functionality
import csv
from datetime import date
import os

# UI
tab_Tasks = functionality.Readcsv()
tab_Tasks = functionality.InitTasksFromTab(tab_Tasks,functionality.Task)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, tab):
        MainWindow.setObjectName("ToDo")
        MainWindow.resize(800, 600)
        self.status = '0'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(5, 110, 786, 451))
        self.listWidget.setObjectName("listWidget")
        self.addItemButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add(tab))
        self.addItemButton.setGeometry(QtCore.QRect(10, 70, 141, 28))
        self.addItemButton.setObjectName("addItemButton")
        self.deleteItemButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.holdStatus(tab))
        self.deleteItemButton.setGeometry(QtCore.QRect(150, 70, 161, 28))
        self.deleteItemButton.setObjectName("deleteItemButton")
        self.endItemButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.editStatus(tab))
        self.endItemButton.setGeometry(QtCore.QRect(310, 70, 161, 28))
        self.endItemButton.setObjectName("endItemButton")
        self.editItemButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.edit(tab))
        self.editItemButton.setGeometry(QtCore.QRect(470, 70, 161, 28))
        self.editItemButton.setObjectName("editItemButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 601, 31))
        self.lineEdit.setObjectName("lineEdit")


        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(640, 20, 151, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 1)))
        self.dateEdit.setMaximumDate(QtCore.QDate(9999, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2023,10,1))
        self.dateEdit.setObjectName("dateEdit")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(640, 70, 110, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Nieskończone')
        self.comboBox.addItem('Skończone')
        self.comboBox.addItem('Wstrzymane')
        self.comboBox.currentIndexChanged.connect(lambda: self.showTasks(tab))

        self.noteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.opnote(tab))
        self.noteButton.setGeometry(QtCore.QRect(755, 68, 35, 35))
        self.noteButton.setObjectName("noteButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.datecheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.datecheckbox.setGeometry(QtCore.QRect(615, 10, 50, 50))
        self.datecheckbox.setObjectName("datecheckbox")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateStatus(self):
        if self.comboBox.currentText() == 'Nieskończone':
            self.endItemButton.setText('Zakończ zadanie')
            self.status = '0'
        elif self.comboBox.currentText() == 'Skończone':
            self.endItemButton.setText('Przywróć zadanie')
            self.status = '1'
        elif self.comboBox.currentText() == 'Wstrzymane':
            self.endItemButton.setText('Przywróć zadanie')
            self.status = '2'
        else: print('error')

    def showTasks(self,tab):
        self.listWidget.clear()
        self.updateStatus()
        for i in range(len(tab)):
            task = tab[i]
            if task.status == self.status:
                if task.date == 'None': text = f'{task.id}: {task.title}'
                else: text = f'{task.id}: {task.title}   {task.date}'
                self.listWidget.addItem(text)
    def getTask(self,tab):
        text = self.listWidget.currentItem().text()
        text = text.split(':')
        task_id = text[0]
        task = tab[int(task_id)]
        return task
    def add(self,tab):
        task_id = len(tab)
        title = self.lineEdit.text()
        if self.datecheckbox.isChecked():
            date = self.dateEdit.text()
            task = functionality.Task(task_id,title,date,'0','false')
            tab.append(task)
        else:
            task = functionality.Task(task_id,title,'None','0','false')
            tab.append(task)
        self.showTasks(tab)
    def edit(self,tab):
        task = self.getTask(tab)
        task.editTitle(self.lineEdit.text())

        self.showTasks(tab)
    def editStatus(self, tab):
        task = self.getTask(tab)
        status = ''
        if self.endItemButton.text() == 'Zakończ zadanie': status = '1'
        elif self.endItemButton.text() == 'Przywróć zadanie': status = '0'
        task.editStatus(status)
        self.showTasks(tab)
    def holdStatus(self, tab):
        task = self.getTask(tab)
        task.editStatus('2')
        self.showTasks(tab)
    def opnote(self, tab):
        task = self.getTask(tab)
        if task.note == 'true': task.opennote()
        elif task.note == 'false':
            task.createnote()
            task.note = 'true'










    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoApp"))

        self.addItemButton.setText(_translate("MainWindow", "Dodaj zadanie"))
        self.deleteItemButton.setText(_translate("MainWindow", "Wstrzymaj zadanie"))
        self.endItemButton.setText(_translate("MainWindow", "Zakończ zadanie"))
        self.editItemButton.setText(_translate("MainWindow", "Edytuj"))
        self.noteButton.setText(_translate("MainWindow", "N"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, tab_Tasks)
    ui.showTasks(tab_Tasks)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass
    functionality.Savecsv(tab_Tasks)

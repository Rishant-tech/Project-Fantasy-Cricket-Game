from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox as msgb
from PyQt5.QtWidgets import QDialog as dlgb
import sqlite3 as sq
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 550)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Lb8 = QtWidgets.QLabel(self.centralwidget)
        self.Lb8.setObjectName("Lb8")
        self.verticalLayout.addWidget(self.Lb8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Lb2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Lb2.setFont(font)
        self.Lb2.setObjectName("Lb2")
        self.horizontalLayout_2.addWidget(self.Lb2)
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        self.Lb1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Lb1.setFont(font)
        self.Lb1.setObjectName("Lb1")
        self.horizontalLayout_2.addWidget(self.Lb1)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.t2.setFont(font)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Lb5 = QtWidgets.QLabel(self.centralwidget)
        self.Lb5.setObjectName("Lb5")
        self.horizontalLayout_5.addWidget(self.Lb5)
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setEnabled(True)
        self.t5.setObjectName("t5")
        self.horizontalLayout_5.addWidget(self.t5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout.addWidget(self.rb2)
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setIconSize(QtCore.QSize(10, 16))
        self.rb1.setObjectName("rb1")
        self.horizontalLayout.addWidget(self.rb1)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout.addWidget(self.rb4)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout.addWidget(self.rb3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.List1 = QtWidgets.QListWidget(self.centralwidget)
        self.List1.setObjectName("List1")
        self.verticalLayout.addWidget(self.List1)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Lb3 = QtWidgets.QLabel(self.centralwidget)
        self.Lb3.setObjectName("Lb3")
        self.horizontalLayout_4.addWidget(self.Lb3)
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setEnabled(True)
        self.t3.setObjectName("t3")
        self.horizontalLayout_4.addWidget(self.t3)
        self.Lb4 = QtWidgets.QLabel(self.centralwidget)
        self.Lb4.setObjectName("Lb4")
        self.horizontalLayout_4.addWidget(self.Lb4)
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setEnabled(True)
        self.t4.setObjectName("t4")
        self.horizontalLayout_4.addWidget(self.t4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Lb6 = QtWidgets.QLabel(self.centralwidget)
        self.Lb6.setObjectName("Lb6")
        self.horizontalLayout_6.addWidget(self.Lb6)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        self.t6.setEnabled(True)
        self.t6.setObjectName("t6")
        self.horizontalLayout_6.addWidget(self.t6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Lb7 = QtWidgets.QLabel(self.centralwidget)
        self.Lb7.setObjectName("Lb7")
        self.horizontalLayout_3.addWidget(self.Lb7)
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        self.t7.setEnabled(True)
        self.t7.setObjectName("t7")
        self.horizontalLayout_3.addWidget(self.t7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.List2 = QtWidgets.QListWidget(self.centralwidget)
        self.List2.setObjectName("List2")
        self.verticalLayout_2.addWidget(self.List2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 24))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.var=[0,0,0,0] ##varible for storing the value of text feilds
        

## for new team----------------
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.manageTeam)
        self.List1.itemDoubleClicked.connect(self.removelist1)
        self.List2.itemDoubleClicked.connect(self.removelist2)
        self.rb1.toggled.connect(self.radio1)
        self.rb2.toggled.connect(self.radio2)
        self.rb3.toggled.connect(self.radio3)
        self.rb4.toggled.connect(self.radio4)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantacy Cricket Game"))
        self.Lb8.setText(_translate("MainWindow", "Your Selection"))
        self.Lb2.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.Lb1.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.Lb5.setText(_translate("MainWindow", "Points Available"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb4.setText(_translate("MainWindow", "AR"))
        self.rb3.setText(_translate("MainWindow", "WK"))
        self.Lb3.setText(_translate("MainWindow", "AllRounders(AR)"))
        self.Lb4.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.Lb6.setText(_translate("MainWindow", "Points Used"))
        self.Lb7.setText(_translate("MainWindow", "Team Name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))

## menubar and action method------------------
    def manageTeam(self,action):
        if action.text()=="New":
            self.newTeam()
        elif action.text()=="Open Team":
            self.openTeam()
        elif action.text()=="Save Team":
            self.saveTeam()
        elif action.text()=="Evaluate Team":
            self.evaluateTeam()

    def newTeam(self):
        self.msg1=msgb()
        self.msg1.setIcon(msgb.Question)
        self.msg1.setText("Are you Sure You want to create New Team")
        self.msg1.setStandardButtons(msgb.Ok|msgb.Cancel)
        self.res1=self.msg1.exec_()        
        if self.res1==msgb.Ok:
            self.t1.clear()
            self.t2.clear()
            self.t3.clear()
            self.t4.clear()
            self.t5.setText("1000")
            self.t6.setText("0")
            self.t7.clear()
            self.List1.clear()
            self.List2.clear()
        try:
            conn=sq.connect('Project.db')
            curs=conn.cursor()
            curs.execute("CREATE TABLE if not exists players (Name CHAR (30) NOT NULL, Points INTEGER (20) );")
            curs.execute("DELETE FROM PLAYERS")
            curs.execute('''INSERT INTO  players ( Name , Points ) VALUES ( 'KOHLI', 80),('YUVRAJ', 90),('RAHNE', 95),('DHAWAN', 75),
('DHONI', 100),('AXAR', 90),('PANDYA', 80),('JADEJA' , 70),('KEDAR', 80),('ASHWIN', 85),('UMESH', 75),
('BUMRAH', 70),('BHUWANESHWAR', 85),('ROHIT', 80),('KARTIK', 90);''')
            conn.commit()
            curs.execute("select * from players")
            record=curs.fetchall()
            self.dict1={}
            
            
            for i in range(15):
                self.List1.addItem(record[i][0])
                r=record[i][0]
                self.dict1[r]=record[i][1]
            
            conn.close()   
        except:
            conn.rollback()
            conn.close()
    def removelist1(self,item):
        if int(self.t5.text()) > 0:
            temp=int(self.dict1[item.text()])
            if (int(self.t5.text()) - temp)>0:
                self.List1.takeItem(self.List1.row(item))
                self.List2.addItem(item.text())
                temp=int(self.dict1[item.text()])
                t=str(int(self.t5.text()) - temp)
                self.t5.setText(t)
                t=str(int(self.t6.text())+temp)
                self.t6.setText(t)
            else:
                self.msg3=msgb()
                self.msg3.setIcon(msgb.Critical)
                self.msg3.setWindowTitle("Error")
                self.msg3.setText("No enough points! \nYou can not select more players\nTry to deselect the player and select another player ")
                self.res3=self.msg3.exec_()
    def removelist2(self,item):
        self.List2.takeItem(self.List2.row(item))
        self.List1.addItem(item.text())
        temp=int(self.dict1[item.text()])
        t=str(int(self.t6.text())-temp)
        self.t6.setText(t)
        t=str(int(self.t5.text())+temp)
        self.t5.setText(t)

    def radio1(self):
        if self.rb1.isChecked()== True:
            self.var[0]+=1
            self.t2.setText(str(self.var[0]))
        else:
            self.t2.setText(str(self.var[0]))
        self.ctg="BAT"
    def radio2(self):
        if self.rb2.isChecked()==True:
            self.var[1]+=1
            self.t1.setText(str(self.var[1]))
        else:
            self.t1.setText(str(self.var[1]))
        self.ctg="BOW"
    def radio3(self):
        if self.rb3.isChecked()==True:
            self.var[2]+=1
            
            if (self.var[2])<=1:
                self.t4.setText(str(self.var[2]))
            else:
                self.msg3=msgb()
                self.msg3.setIcon(msgb.Critical)
                self.msg3.setWindowTitle("Warning")
                self.msg3.setText("You can not select more than 1 wicket keeper")
                self.msg3.exec_()
                self.var[2]=1
        else:
            self.t4.setText(str(self.var[2]))
        self.ctg="WK"
    def radio4(self):
        if self.rb4.isChecked()==True:
            self.var[3]+=1
            self.t3.setText(str(self.var[3]))
        else:
            self.t3.setText(str(self.var[3]))
        self.ctg="AR"
       
    def openTeam(self):
        try:
            self.dlg3=dlgb()
            self.dlg3.setWindowTitle("Open Team")
            self.Lb13=QtWidgets.QLabel(self.dlg3)
            self.Lb13.setText("Team:")
            self.t9=QtWidgets.QLineEdit(self.dlg3)
            self.B3=QtWidgets.QPushButton("Open",self.dlg3)
            self.vBox3=QtWidgets.QVBoxLayout(self.dlg3)
            self.vBox3.addWidget(self.Lb13)
            self.vBox3.addWidget(self.t9)
            self.vBox3.addWidget(self.B3)
            self.B3.clicked.connect(self.open)
            self.dlg3.exec_()           
            
        except:
            self.msg3=msgb()
            self.msg3.setIcon(msgb.Critical)
            self.msg3.setWindowTitle("Error")
            self.msg3.setText("Error While Fetching the Team Data")
            self.res3=self.msg3.exec_()
            if self.res3==msgb.Ok:
                conn.rollback()
                conn.close()
            else:
                return
    def open(self):
        try:
            query="select * from teams where name = '"+self.t9.text()+"'"
            conn=sq.connect('Project.db')
            curs=conn.cursor()
            curs.execute('''CREATE TABLE if not exixts teams (
    NAME    CHAR (20),PLAYERS CHAR (30),VALUE   INTEGER (20) );''')
            curs.execute(query)
            record=curs.fetchall()
            self.t7.setText(str(record[0][0]))
            dict3={}
            temp=0
            for i in range(15):
                self.List1.addItem(record[i][1])
                r=record[i][1]
                self.dict3[r]=record[i][2]
                temp=temp+int(self.dict3[r])
            self.t6.setText(str(temp))
            temp1=str(1000-temp)
            self.t5.setText(temp1)
        except:
            conn.rollback()
            conn.close
            
    def saveTeam(self):
        self.dlg1=dlgb()
        self.dlg1.setWindowTitle("Save")
        self.t8=QtWidgets.QLineEdit(self.dlg1)
        self.t8.setText(self.t7.text())
        self.B1=QtWidgets.QPushButton("Save",self.dlg1)
        self.Lb9=QtWidgets.QLabel(self.dlg1)
        self.Lb9.setText("Team:")
        self.vBox1=QtWidgets.QVBoxLayout(self.dlg1)
        self.vBox1.addWidget(self.Lb9)
        self.vBox1.addWidget(self.t8)
        self.vBox1.addWidget(self.B1)
        self.B1.clicked.connect(self.save)
        self.dlg1.exec_()
    def save(self):
        try:
            conn=sq.connect("Project.db")
            curs=conn.cursor()
            curs.execute('''CREATE TABLE if not exists teams (
    NAME    CHAR (20),PLAYERS CHAR (30),VALUE   INTEGER (20));''')
            i=0
            while i<self.List2.count():
                item=self.List2.item(i)
                curs.execute("INSERT INTO teams VALUES ('"+self.t8.text()+"','"+item.text()+"','"+str(self.dict1[item.text()])+"')")
                conn.commit()
                i=i+1
            conn.close()
            
        except:
            conn.rollback()
            conn.close()            
    def evaluateTeam(self):
        self.dlg2=dlgb()
        self.dlg2.setWindowTitle("Evaluation")
        self.vBox2 = QtWidgets.QVBoxLayout(self.dlg2)
        self.Lb10 = QtWidgets.QLabel(self.dlg2)
        self.Lb10.setText("Evaluate the performance of the Fantacy Team")
        self.vBox2.addWidget(self.Lb10)
        self.hBox1 = QtWidgets.QHBoxLayout()
        self.Cb1 = QtWidgets.QComboBox(self.dlg2)
        self.hBox1.addWidget(self.Cb1)
        self.Cb2 = QtWidgets.QComboBox(self.dlg2)
        self.Cb2.addItem("Match 1")
        self.Cb2.addItem("Match 2")
        self.hBox1.addWidget(self.Cb2)
        self.vBox2.addLayout(self.hBox1)
        self.hBox2 = QtWidgets.QHBoxLayout()
        self.Lb11 = QtWidgets.QLabel(self.dlg2)
        self.Lb11.setText("Players:")
        self.hBox2.addWidget(self.Lb11)
        self.Lb12 = QtWidgets.QLabel(self.dlg2)
        self.Lb12.setText("Points:")
        self.hBox2.addWidget(self.Lb12)
        self.vBox2.addLayout(self.hBox2)
        self.hBox3 = QtWidgets.QHBoxLayout()
        self.List3 = QtWidgets.QListWidget(self.dlg2)
        self.hBox3.addWidget(self.List3)
        self.List4 = QtWidgets.QListWidget(self.dlg2)
        self.hBox3.addWidget(self.List4)
        self.vBox2.addLayout(self.hBox3)
        self.B2 = QtWidgets.QPushButton(self.dlg2)
        self.B2.setText("Evaluate")
        self.vBox2.addWidget(self.B2)
        self.B2.clicked.connect(self.eval)
        self.List3.clear()
        self.List4.clear()
        try:
            conn=sq.connect("Project.db")
            curs=conn.cursor()
            curs.execute("select Name from teams")
            result=curs.fetchall()
            col=set()
            for ele in result:
                col.add(ele[0])
            for ele in col:
                self.Cb1.addItem(ele)
            curs.execute("select * from teams where name='"+str(self.Cb1.currentText())+"'")
            result=curs.fetchall()
            dic={}
            for i in range(15):
                self.List3.addItem(result[i][1])
                r=result[i][1]
                dic[r]=result[i][2]
                self.List4.addItem(str(dic[r]))   
            conn.close()
        except:
            conn.rollback()
            conn.close()
        self.Cb1.activated.connect(self.combo)
        self.dlg2.exec_()
    def combo(self):
        self.List3.clear()
        self.List4.clear()
        try:
            conn=sq.connect("Project.db")
            curs=conn.cursor()
            curs.execute("select * from teams where name='"+str(self.Cb1.currentText())+"'")
            result=curs.fetchall()
            dic={}
            for i in range(15):
                self.List3.addItem(result[i][1])
                r=result[i][1]
                dic[r]=result[i][2]
                self.List4.addItem(str(dic[r]))   
            conn.close()
        except:
            conn.rollback()
            conn.close()
    def eval(self):
        try:
            conn=sq.connect('Project.db')
            curs=conn.cursor()
            curs.execute('''CREATE TABLE if not exists [match] (PLAYER CHAR (30),SCORED INTEGER (15),FACED INTEGER (15),
                            FOURS INTEGER (15),SIXES INTEGER (15),BOWLED INTEGER (15),MAIDEN INTEGER (15),GIVEN INTEGER (15),
                            WKTS INTEGER (15),CATCHES INTEGER (15),STUMPING INTEGER (15),RUN_OUT  INTEGER (15));''')
            curs.execute('''CREATE TABLE if not exists stats (PLAYER CHAR (30),MATCHES INTEGER (15),RUNS INTEGER (15),[100s]  INTEGER (15),
                            [50s] INTEGER (15),VALUE INTEGER (20),CTG CHAR (20));''')
            l=[]
            for i in range(self.List3.count()):
                l.append((self.List3.item(i)).text())
            ball=120
            facelist=["true","false","catch","wicket","run","stump"]
            rlist=[0,2,4,6]
            for ele in l:
                point=0
                run=0
                Hc=0
                Fc=0
                four=0
                six=0
                f=0
                g=0
                maidn=0
                wkt=0
                cth=0
                r=0
                s=0
                for i in range(ball):
                    faced=random.choice(facelist)
                    rpoint=random.choice(rlist)
                    if faced == "true":
                        if run<=(ball*6):
                            
                            run = run + rpoint
                            
                            if rpoint == 2:
                                point = point + 1
                                
                            elif rpoint == 4:
                                point = point + 1
                                four = four + 1 
                            elif rpoint == 6:
                                point = point + 2
                                six = six + 1
                            elif run>=50 and run <100:
                                point = point + 5
                                Hc = Hc + 1
                                
                            elif run>=100:
                                point = point + 4*(run/100)
                                Fc = Fc +1
                            
                            elif run>0:
                                if (run/i) >=80 :
                                    point = point + 2
                                elif (run/i)>100:
                                    point = point + 4
                        f = f + 1
                        g = g + 1
                        
                    elif faced == "false":
                        run = run + 0
                        maidn = maidn + 1
                    elif faced == "catch":
                        point = point + 10
                        cth = cth + 1
                        break
                    elif faced == "wicket":
                        point = point + 10
                        temp0=[3,5,6]
                        temp=random.choice(temp0)
                        if temp == 3:
                            point = point + 5
                        
                        elif temp == 5 or temp == 6:
                            point = point + 10
                        elif run>0:
                            if ((run*6)/i)>=3.5 or ((run*6)/i)<4.5:
                                point = point + 4
                            elif ((run*6)/i)>=2 or ((run*6)/i)<3.5:
                                point = point + 7
                            elif ((run*6)/i)<10:
                                point = point + 10
                        wkt = wkt + 1
                        
                        break
                    elif faced == "run":
                        point = point + 10
                        r = r + 1
                        break
                    elif faced == "stump":
                        point = point + 10
                        s = s + 1
                        break
                q="'"+ele+"',"+str(run)+","+str(f)+","+str(four)+","+str(six)+","+str(i)+","+str(maidn)+","+str(g)+","+str(wkt)+","+str(cth)+","+str(s)+","+str(r)+");"
                #print(q)
                curs.execute('''insert into [match](PLAYER ,SCORED ,FACED ,FOURS ,SIXES ,BOWLED ,MAIDEN ,GIVEN ,
                                WKTS ,CATCHES ,STUMPING ,RUN_OUT )
                                values('''+q)
                
                q1="'"+ele+"',"+"1"+","+str(run)+","+str(Fc)+","+str(Hc)+","+str(point)+",'"+"NA"+"');"
                #print(q1)
                
                curs.execute('''insert into stats (PLAYER ,MATCHES ,RUNS ,[100s] ,[50s] ,VALUE ,CTG )
                                values('''+q1)
            conn.commit()
            conn.close()
        except:
            print("error")
            conn.rollback()
            conn.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

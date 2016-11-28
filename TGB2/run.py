from time import sleep  
import sys, serial
from PyQt4.QtCore import QThread, QMutex
from PyQt4 import QtCore, QtGui, uic
from main import Ui_MainWindow
#sets up serial comunication
ser =  serial.Serial('/dev/ttyACM0')
ser.baudrate = 115200

class MyMainwindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tempd = self.ui.temp
        self.pressd = self.ui.pressure
        self.quantd = self.ui.quant
        self.flowd = self.ui.flow
        self.tmaxled = self.ui.tmax_led
        self.tminled = self.ui.tmin_led
        self.ui.startb.clicked.connect(self.update)
        self.ui.tmax_set.valueChanged.connect(lambda:self.set_temp('max'))
        self.ui.tmin_set.valueChanged.connect(lambda:self.set_temp('min'))
        self.ui.comboBox.currentIndexChanged.connect(self.set_receita)
        self.tmax = self.ui.tmax_set
        self.tmin = self.ui.tmin_set
        self.box = self.ui.textEdit


    def set_receita(self, index):

        if index==1:
            self.ui.tmin_set.setValue(0)
            self.ui.tmax_set.setValue(45)
            ser.write(str(chr(69)))
            ser.write("#T#45#t#0#S#86#")
            
        elif index ==2:
        
            self.ui.tmin_set.setValue(15)
            self.ui.tmax_set.setValue(50)
            ser.write(str(chr(69)))
            ser.write("#T#50#t#15#S#70#")

        elif index ==3:
        
            self.ui.tmin_set.setValue(30)
            self.ui.tmax_set.setValue(65)
            ser.write(str(chr(69)))
            ser.write("#T#65#t#30#S#30#")


        elif index ==4:
        
            self.ui.tmin_set.setValue(0)
            self.ui.tmax_set.setValue(30)
            ser.write(str(chr(69)))
            ser.write("#T#30#t#0#S#86#")

        else:
            self.ui.tmin_set.setValue(0)
            self.ui.tmax_set.setValue(70)
            ser.write(str(chr(69)))
            ser.write("#T#30#t#0#S#86#")
            
          
# checks out temperature values
    def test_temp(self, temp):
        if temp > self.tmax.value():
            self.set_led('red', 'on')
            self.set_led('blue', 'off')
        elif temp < self.tmin.value():
            self.set_led('red', 'off')
            self.set_led('blue', 'on')
        else:
            self.set_led('red', 'off')
            self.set_led('blue', 'off')
            
    #changes led status
    def set_led(self,led,status):
        if led == 'red':
            if status == 'on':
                self.tmaxled.on()
            else:
                self.tmaxled.off()
        else:
            if status == 'on':
                self.tminled.on()
            else:
                self.tminled.off()
                
    # changes temperature setup            
    def set_temp(self, temp):
        """global tmax,tmin
        if temp =='max':
            tmax = self.ui.tmax_set.value()
        else:
            tmin = self.ui.tmin_set.value()
           """ 
    def get_data(self, data):
        # splits data and output it to LCDs displays
        self.data = data.split('#')
        count = 0; 
        for value in self.data:
            if value == 'T':
                self.tempd.display(int(self.data[count+1]))
                self.test_temp(int(self.data[count+1]))
            elif value == 'P':
                self.pressd.display(int(self.data[count+1]))
            elif value == 'V':
                self.flowd.display(int(self.data[count+1])) 
            elif value == 'Q':
                self.quantd.display(int(self.data[count+1]))
            elif value == 'R':
                #self.quantd.display(int(self.data[count+1]))
                self.box.setText("Tempo restante %s" %self.data[count+1])

            elif value == 'F':
                #self.quantd.display(int(self.data[count+1]))
                self.box.setText("Processo Finalizado")
            else:
                pass
            count = count+1

    def update(self, data):
        self.serthread = Threadser()
        self.connect(self.serthread, QtCore.SIGNAL("update"), self.get_data)
        self.serthread.start()
        #self.get_data(data)

class Threadser(QThread):
    def __init__(self):
        QThread.__init__(self) 

    def __del__(self):
        self.wait()

    def run(self):
        while(1):
            sleep(0.1)
            ser.write(str(chr(76)))
            data  = ser.readline()
            self.emit(QtCore.SIGNAL("update"),data)
            
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainwindow()
    myapp.show()
    sys.exit(app.exec_())

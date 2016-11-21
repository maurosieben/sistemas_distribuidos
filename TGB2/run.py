from time import sleep  
import sys, serial
from PyQt4.QtCore import QThread, QMutex
from PyQt4 import QtCore, QtGui, uic
from main import Ui_MainWindow
#sets up serial comunication
#ser =  serial.Serial('/dev/ttyACM0')
#ser.baudrate = 115200

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
        self.tmax = self.ui.tmax_set
        self.tmin = self.ui.tmin_set

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
            data  = "#T#31#P#12#V#57#Q#5000#"
            self.emit(QtCore.SIGNAL("update"),data)
            
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainwindow()
    myapp.show()
    sys.exit(app.exec_())

# 푸시버튼

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self) 
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2') ## &2 => alt + 2 누르면 버튼 선택됨

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False) # => 안눌러지는 조건,, 조건이 충족하면 활성화될 수 있게 만들 수 있음 

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('버튼')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
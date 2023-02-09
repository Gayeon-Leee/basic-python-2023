# 레이아웃 절대적 배치

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOK = QPushButton('OK')
        btnCancel = QPushButton('Cancle')

        hbox = QHBoxLayout() # 버튼 두개를 가로로 배치한 것
        hbox.addStretch(1) #stretch는 여백 공간으로 생각하면 됨
        hbox.addWidget(btnOK)
        hbox.addWidget(btnCancel)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
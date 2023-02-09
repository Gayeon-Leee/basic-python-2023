# 레이아웃 절대적 배치

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        grid.addWidget(QLabel('Title'), 0, 0) # row, clo = 0, 0
        grid.addWidget(QLabel('Author'), 1, 0)
        grid.addWidget(QLabel('Title'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1) # 0행 1렬
        grid.addWidget(QLineEdit(), 1, 1) 
        grid.addWidget(QTextEdit(), 2, 1) 

        btnOK = QPushButton('OK')
        btnCancel = QPushButton('Cancle')
        
        grid.addWidget(btnOK, 3, 1)
        grid.addWidget(btnCancel, 4, 1)

    

        # 필수설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
# 체크박스 => 다중선택 가능, 라디오버튼 => 다중선택 불가

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblOption = QLabel('선택값 : ', self)   
        # lblOption 이라고만 하면 initUI에만 속하는 지역변수라서 initUI 밖에서 못씀 => self.lblOption 으로 클래스에 속하는 전역변수로 만들어 주는 것!
        self.lblOption.move(20, 20)

        cbOption = QComboBox(self) #cbOption 은 외부에서 접근 안하고 initUI 안에서만 쓸거라 지역변수로 놔둬도 됨
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.addItem('Option5')
        cbOption.move(20, 40)
        cbOption.activated[str].connect(self.onActivated) # 여기서 str은 위의 Optin1~5 가르킴

        # 필수설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onActivated(self, text):
        self.lblOption.setText('선택값 :' + text)
        self.lblOption.adjustSize()
        #adjustSize 는 글자수 만큼 라벨의 넓이를 조정해주는 것 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
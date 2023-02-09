import sys
from PyQt5.QtWidgets import QApplication, QWidget
## import * 하면 PyQt5.QtWidgets 모듈 전체 불러오겠다는 것

class MyApp(QWidget): # QWidget을 상속받는 MyApp 클래스를 만들겠다는 것
    

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):   
        # GUI 화면 설정
        self.setWindowTitle('Simple Window') # 기본 타이틀 Python -> Simple Window 로 변경
        # self.move(1920 - 400, 0) 
        # 처음 실행되는 위치값 변경 / 없으면 정중앙에 생성 / 화면의 왼쪽 위 모서리가 0,0 임
        # move 함수 인자에 연산자 사용 할 수 있음. 화면의 오른쪽 끝에 생성하고 싶으면 해상도 - 팝업 가로 사이즈
        self.resize(400, 200)
        self.show() # 핵심 ! 이거 있어야 화면상으로 보임
    

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

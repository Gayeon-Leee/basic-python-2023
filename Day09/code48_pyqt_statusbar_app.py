import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

## import * 하면 PyQt5.QtWidgets 모듈 전체 불러오겠다는 것

class MyApp(QMainWindow): # QWidget을 상속받는 MyApp 클래스를 만들겠다는 것
    

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메뉴바 부분 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q') # 단축기 지정
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar') # 문자열은 툴바 타이틀임.. 없어도 됨
        toolbar.addAction(actSave)      
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate()   # 현재일자
        time = QTime.currentTime()   # 현재시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd')+ ' ' + time.toString())
        self.setWindowIcon(QIcon('./Day09/iot.png')) 
        # GUI 화면 설정
        self.setWindowTitle('Bar window') # 기본 타이틀 Python -> Simple Window 로 변경
        # self.move(1920 - 400, 0) 
        # 처음 실행되는 위치값 변경 / 없으면 정중앙에 생성 / 화면의 왼쪽 위 모서리가 0,0 임
        # move 함수 인자에 연산자 사용 할 수 있음. 화면의 오른쪽 끝에 생성하고 싶으면 해상도 - 팝업 가로 사이즈
        self.resize(400, 200)
        self.setCenter()
        self.show() # 핵심 ! 이거 있어야 화면상으로 보임
    
    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값 설정
        cp = QDesktopWidget().availableGeometry().center() # 현재 모니터화면의 중심을 찾는것
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

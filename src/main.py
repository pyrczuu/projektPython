import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QGridLayout, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Planer treningów')
        self.setGeometry(600, 300, 700, 500)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.menu = self.createMenuPage()
        self.titlePage = self.createTitlePage()
        self.pplPage = self.createPPLPage()
        self.informacjePage = self.createInformacjePage()
        self.central_widget.addWidget(self.titlePage)
        self.central_widget.addWidget(self.menu)
        self.central_widget.addWidget(self.pplPage)
        self.central_widget.addWidget(self.informacjePage)
        self.setStyleSheet("background-color: #f2f2f0")
        self.setWindowIcon(QIcon('C:\python\projektPython\media\icon.jpg'))


    def createMenuPage(self):
        page = QWidget()
        grid = QGridLayout()
        tytul = QLabel("Wybierz plan")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        ppl = QPushButton("Push Pull Legs", self)
        ppl.setFixedSize(200, 300)
        ppl.setFont(QFont('Bauhaus 93', 20))
        ppl.setStyleSheet("color: white; background-color: #5e0811")
        ppl.clicked.connect(self.showPPLPage)
        ul = QPushButton("Upper Lower", self)
        ul.setFixedSize(200, 300)
        ul.setFont(QFont('Bauhaus 93', 20))
        ul.setStyleSheet("color: white; background-color: #5e0811")
        fb = QPushButton("Fullbody", self)
        fb.setFixedSize(200, 300)
        fb.setFont(QFont('Bauhaus 93', 20))
        fb.setStyleSheet("color: white; background-color: #5e0811")
        grid.addWidget(tytul, 0 ,1, 1 ,1 )
        grid.addWidget(ppl, 1 , 0, 1, 1)
        grid.addWidget(ul, 1, 1, 1, 1)
        grid.addWidget(fb, 1, 2,1,1)
        page.setLayout(grid)
        return page

    def createPPLPage(self):
        page = QWidget()
        grid = QGridLayout()
        tytul = QLabel("Push Pull Legs")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        grid.addWidget(tytul, 0, 1, 1, 1)
        page.setLayout(grid)
        return page

    def createTitlePage(self):
        page = QWidget()
        grid = QGridLayout()
        tytul = QLabel("Co chcesz zrobić?")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        bPrzegladaj = QPushButton("Przegladaj \n zapisane", self)
        bPrzegladaj.setFixedSize(200, 300)
        bPrzegladaj.setFont(QFont('Bauhaus 93', 20))
        bPrzegladaj.setStyleSheet("color: white; background-color: #5e0811")
        bNowyPlan = QPushButton("Dodaj \n nowy plan", self)
        bNowyPlan.setFixedSize(200, 300)
        bNowyPlan.setFont(QFont('Bauhaus 93', 20))
        bNowyPlan.setStyleSheet("color: white; background-color: #5e0811")
        bNowyPlan.clicked.connect(self.showMenuPage)
        bInformacje = QPushButton("Informacje", self)
        bInformacje.setFixedSize(200, 300)
        bInformacje.setFont(QFont('Bauhaus 93', 20))
        bInformacje.setStyleSheet("color: white; background-color: #5e0811")
        bInformacje.clicked.connect(self.showInformacjePage)
        grid.addWidget(tytul, 0, 1, 1, 1)
        grid.addWidget(bPrzegladaj, 1, 0, 1, 1)
        grid.addWidget(bNowyPlan, 1, 1, 1, 1)
        grid.addWidget(bInformacje, 1, 2, 1, 1)
        page.setLayout(grid)
        return page

    def createInformacjePage(self):
        page = QWidget()
        grid = QGridLayout()
        info = QLabel()
        info.setText( 'Aplikacja stworzona w ramach projektu dla dr hab. Jana Kozaka.\n'
                    'Autor: Damian Pyrcz\n'
                    'Repozytorium: https://github.com/pyrczuu/projektPython')
        info.setOpenExternalLinks(True)
        info.setAlignment(Qt.AlignCenter)
        info.setFont(QFont('Bahnschrift Semibold', 10))
        info.setStyleSheet("color: #5e0811")
        info.adjustSize()
        grid.addWidget(info, 0, 0, 1, 2)
        page.setLayout(grid)
        return page

    def showPPLPage(self):
        self.central_widget.setCurrentWidget(self.pplPage)

    def showTitlePage(self):
        self.central_widget.setCurrentWidget(self.titlePage)

    def showMenuPage(self):
        self.central_widget.setCurrentWidget(self.menu)

    def showInformacjePage(self):
        self.central_widget.setCurrentWidget(self.informacjePage)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


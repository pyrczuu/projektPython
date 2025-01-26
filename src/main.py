import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QGridLayout, QStackedWidget, \
    QCheckBox, QLineEdit, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import src.classes

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.plans = {}
        self.limitedEquipment = False
        self.setWindowTitle('Planer treningów')
        self.setGeometry(600, 300, 700, 500)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.przegladaj = self.createPrzegladajPage()
        self.menu = self.createMenuPage()
        self.titlePage = self.createTitlePage()
        self.pplPage = self.createPPLPage()
        self.ulPage = self.createULPage()
        self.fbPage = self.createFBPage()
        self.informacjePage = self.createInformacjePage()
        self.central_widget.addWidget(self.titlePage)
        self.central_widget.addWidget(self.przegladaj)
        self.central_widget.addWidget(self.menu)
        self.central_widget.addWidget(self.informacjePage)
        self.central_widget.addWidget(self.pplPage)
        self.central_widget.addWidget(self.ulPage)
        self.central_widget.addWidget(self.fbPage)
        self.setStyleSheet("background-color: #f2f2f0")
        self.setWindowIcon(QIcon('C:\python\projektPython\media\icon.jpg'))

    # main pages

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
        bPrzegladaj.clicked.connect(self.showPrzegladajPage)
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

    def createPrzegladajPage(self):
        page = QWidget()
        layout = QVBoxLayout()
        tytul = QLabel("Twoje zapisane plany")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        self.zawartosc_planow = ""
        if not self.plans:
            self.zawartosc_planow = "Brak zapisanych planów."
        else:
            for nazwa_planu, plan in self.plans.items():
                self.zawartosc_planow += f"{nazwa_planu}\n"
                self.zawartosc_planow += f"{plan}\n\n"
        self.label_plany = QLabel(self.zawartosc_planow)
        self.label_plany.setFont(QFont('Bahnschrift Semibold', 20))
        self.label_plany.setStyleSheet("color: black")
        self.label_plany.setWordWrap(True)
        self.label_plany.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.export_button = QPushButton("Zapisz w pliku txt", self)
        self.export_button.setFixedSize(200, 30)
        self.export_button.setFont(QFont('Bahnschrift Semibold', 10))
        self.export_button.clicked.connect(self.export_button_click)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.label_plany)
        layout.addWidget(tytul)
        layout.addWidget(scroll_area)
        layout.addWidget(self.export_button)
        page.setLayout(layout)
        return page

    def createMenuPage(self):
        page = QWidget()
        grid = QGridLayout()
        tytul = QLabel("Wybierz plan")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        tytul.adjustSize()
        checkEquipment = QCheckBox("Czy twój sprzęt \njest ograniczony?")
        checkEquipment.setFont(QFont('Bahnschrift', 15))
        checkEquipment.stateChanged.connect(self.checkbox)
        ppl = QPushButton("Push Pull Legs", self)
        ppl.setFixedSize(200, 300)
        ppl.setFont(QFont('Bauhaus 93', 20))
        ppl.setStyleSheet("color: white; background-color: #5e0811")
        ppl.clicked.connect(self.showPPLPage)
        ul = QPushButton("Upper Lower", self)
        ul.setFixedSize(200, 300)
        ul.setFont(QFont('Bauhaus 93', 20))
        ul.setStyleSheet("color: white; background-color: #5e0811")
        ul.clicked.connect(self.showULPage)
        fb = QPushButton("Fullbody", self)
        fb.setFixedSize(200, 300)
        fb.setFont(QFont('Bauhaus 93', 20))
        fb.setStyleSheet("color: white; background-color: #5e0811")
        fb.clicked.connect(self.showFBPage)
        grid.addWidget(tytul, 0 ,1)
        grid.addWidget(checkEquipment, 1 ,1)
        grid.addWidget(ppl, 2 , 0)
        grid.addWidget(ul, 2, 1)
        grid.addWidget(fb, 2, 2)
        page.setLayout(grid)
        return page

    def createInformacjePage(self):
        page = QWidget()
        grid = QGridLayout()
        home = QPushButton(self)
        home.setIcon(QIcon('C:\python\projektPython\media\home-icon-png-31.png'))
        home.clicked.connect(self.showTitlePage)
        home.adjustSize()
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

    # training programme pages

    def createPPLPage(self):
        page = QWidget()
        layout = QVBoxLayout()
        self.plan_ppl = src.classes.PPL(self.limitedEquipment)
        tytul = QLabel("Push Pull Legs")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        self.nazwa_ppl = QLineEdit()
        self.nazwa_ppl.setFont(QFont('Bahnschrift Semibold', 15))
        self.nazwa_ppl.setStyleSheet("color: black")
        self.nazwa_ppl.setPlaceholderText("Chcesz zapisać ten plan? Nadaj mu nazwę!")
        self.nazwa_ppl.adjustSize()
        self.bNazwa = QPushButton("Zapisz", self)
        self.bNazwa.setFixedSize(self.nazwa_ppl.width(), 30)
        self.bNazwa.clicked.connect(self.bNazwa_ppl_click)
        self.bPowtorz = QPushButton("Jeszcze raz", self)
        self.bPowtorz.setFixedSize(self.nazwa_ppl.width(), 30)
        self.bPowtorz.clicked.connect(self.bPowtorzPPL_click)
        self.plan_label_ppl = QLabel()
        self.plan_label_ppl.setStyleSheet("color: black")
        layout.addWidget(tytul)
        layout.addWidget(self.nazwa_ppl)
        layout.addWidget(self.bNazwa)
        layout.addWidget(self.bPowtorz)
        layout.addWidget(self.plan_label_ppl)
        page.setLayout(layout)
        return page

    def createULPage(self):
        page = QWidget()
        layout = QVBoxLayout()
        self.plan_ul = src.classes.UL(self.limitedEquipment)
        tytul = QLabel("Upper Lower")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        self.nazwa_ul = QLineEdit()
        self.nazwa_ul.setFont(QFont('Bahnschrift Semibold', 15))
        self.nazwa_ul.setStyleSheet("color: black")
        self.nazwa_ul.setPlaceholderText("Chcesz zapisać ten plan? Nadaj mu nazwę!")
        self.nazwa_ul.adjustSize()
        self.bNazwa = QPushButton("Zapisz", self)
        self.bNazwa.setFixedSize(self.nazwa_ul.width(), 30)
        self.bNazwa.clicked.connect(self.bNazwa_ul_click)
        self.bPowtorz = QPushButton("Jeszcze raz", self)
        self.bPowtorz.setFixedSize(self.nazwa_ul.width(), 30)
        self.bPowtorz.clicked.connect(self.bPowtorzUL_click)
        self.plan_label_ul = QLabel()
        self.plan_label_ul.setStyleSheet("color: black")
        layout.addWidget(tytul)
        layout.addWidget(self.nazwa_ul)
        layout.addWidget(self.bNazwa)
        layout.addWidget(self.bPowtorz)
        layout.addWidget(self.plan_label_ul)
        page.setLayout(layout)
        return page

    def createFBPage(self):
        page = QWidget()
        layout = QVBoxLayout()
        self.plan_fb = src.classes.FB(self.limitedEquipment)
        tytul = QLabel("Fullbody")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        tytul.adjustSize()
        self.nazwa_fb = QLineEdit()
        self.nazwa_fb.setFont(QFont('Bahnschrift Semibold', 15))
        self.nazwa_fb.setStyleSheet("color: black")
        self.nazwa_fb.setPlaceholderText("Chcesz zapisać ten plan? Nadaj mu nazwę!")
        self.nazwa_fb.adjustSize()
        self.bNazwa = QPushButton("Zapisz", self)
        self.bNazwa.setFixedSize(self.nazwa_fb.width(), 30)
        self.bNazwa.clicked.connect(self.bNazwa_fb_click)
        self.bPowtorz = QPushButton("Jeszcze raz", self)
        self.bPowtorz.setFixedSize(self.nazwa_fb.width(), 30)
        self.bPowtorz.clicked.connect(self.bPowtorzFB_click)
        self.plan_label_fb = QLabel()
        self.plan_label_fb.setStyleSheet("color: black")
        layout.addWidget(tytul)
        layout.addWidget(self.nazwa_fb)
        layout.addWidget(self.bNazwa)
        layout.addWidget(self.bPowtorz)
        layout.addWidget(self.plan_label_fb)
        page.setLayout(layout)
        return page

    # interactive stuff

    def checkbox(self, state):
        if state == Qt.Checked:
            self.limitedEquipment = True
        elif state == Qt.Unchecked:
            self.limitedEquipment = False

    def bNazwa_ppl_click(self):
        try:
            name = self.nazwa_ppl.text()
            plan = self.plan_label_ppl.text()
            if name in self.plans:
                raise Exception("Ta nazwa jest zajęta!")
            else:
                self.plans[name] = plan
                self.aktualizujPrzegladajPage()
        except Exception as e:
            self.nazwa_ppl.setText(str(e))

    def bNazwa_ul_click(self):
        try:
            name = self.nazwa_ul.text()
            plan = self.plan_label_ul.text()
            if name in self.plans:
                raise Exception("Ta nazwa jest zajęta!")
            else:
                self.plans[name] = plan
                self.aktualizujPrzegladajPage()
        except Exception as e:
            self.nazwa_ul.setText(str(e))

    def bNazwa_fb_click(self):
        try:
            name = self.nazwa_fb.text()
            plan = self.plan_label_fb.text()
            if name in self.plans:
                raise Exception("Ta nazwa jest zajęta!")
            else:
                self.plans[name] = plan
                self.aktualizujPrzegladajPage()
        except Exception as e:
            self.nazwa_fb.setText(str(e))

    def bPowtorzPPL_click(self):
        self.plan_ppl = src.classes.PPL(self.limitedEquipment)
        self.plan_label_ppl.setText(str(self.plan_ppl.__str__()))

    def bPowtorzUL_click(self):
        self.plan_ul = src.classes.UL(self.limitedEquipment)
        self.plan_label_ul.setText(str(self.plan_ul.__str__()))

    def bPowtorzFB_click(self):
        self.plan_fb = src.classes.FB(self.limitedEquipment)
        self.plan_label_fb.setText(str(self.plan_fb.__str__()))

    def aktualizujPrzegladajPage(self):
        self.zawartosc_planow = ""
        if not self.plans:
            self.zawartosc_planow = "Brak zapisanych planów."
        else:
            for nazwa_planu, plan in self.plans.items():
                self.zawartosc_planow += f"{nazwa_planu}\n"
                self.zawartosc_planow += f"{plan}\n\n"
        self.label_plany.setText(self.zawartosc_planow)

    def export_button_click(self):
        with open("plany_treningowe.txt", "w") as f:
            f.write(self.zawartosc_planow)

    # switching pages

    def showPrzegladajPage(self):
        self.central_widget.setCurrentWidget(self.przegladaj)

    def showTitlePage(self):
        self.central_widget.setCurrentWidget(self.titlePage)

    def showMenuPage(self):
        self.central_widget.setCurrentWidget(self.menu)

    def showInformacjePage(self):
        self.central_widget.setCurrentWidget(self.informacjePage)

    def showPPLPage(self):
        self.plan_ppl = src.classes.PPL(self.limitedEquipment)
        self.plan_label_ppl.setText(str(self.plan_ppl))
        self.central_widget.setCurrentWidget(self.pplPage)

    def showULPage(self):
        self.plan_ul = src.classes.UL(self.limitedEquipment)
        self.plan_label_ul.setText(str(self.plan_ul))
        self.central_widget.setCurrentWidget(self.ulPage)

    def showFBPage(self):
        self.plan_fb = src.classes.FB(self.limitedEquipment)
        self.plan_label_fb.setText(str(self.plan_fb))
        self.central_widget.setCurrentWidget(self.fbPage)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

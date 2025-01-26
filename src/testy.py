from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class PrzegladajPlanyPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.plans = {}  # Słownik z planami
        self.initUI()

    def initUI(self):
        # Główny układ strony
        layout = QVBoxLayout()

        # Tytuł strony
        tytul = QLabel("Twoje zapisane plany")
        tytul.setFont(QFont('Bahnschrift Semibold', 20))
        tytul.setStyleSheet("color: #5e0811")
        tytul.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Zawartość planów (tekst)
        zawartosc_planow = self.formatuj_plany(self.plans)

        # Etykieta z zawartością planów
        label_plany = QLabel(zawartosc_planow)
        label_plany.setFont(QFont('Bahnschrift Semibold', 10))
        label_plany.setStyleSheet("color: black")
        label_plany.setWordWrap(True)  # Zawijanie tekstu

        # Przewijany obszar
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Dostosowanie rozmiaru widgetu
        scroll_area.setWidget(label_plany)  # Ustaw etykietę jako widget w QScrollArea

        # Dodanie widgetów do układu
        layout.addWidget(tytul)
        layout.addWidget(scroll_area)

        # Ustawienie układu dla strony
        self.setLayout(layout)

    def formatuj_plany(self, plans):
        # Formatowanie zawartości słownika do tekstu
        zawartosc = ""
        for nazwa_planu, grupy in plans.items():
            zawartosc += f"{nazwa_planu}\n"
            for grupa, cwiczenia in grupy.items():
                zawartosc += f"  {grupa}:\n"
                for cwiczenie in cwiczenia:
                    zawartosc += f"    {cwiczenie}\n"
            zawartosc += "\n"  # Dodaj pustą linię między planami
        return zawartosc


# Przykładowe dane
przykladowe_plany = {
    "pierwszy plan": {
        "Push": ["ćwiczenie 1", "ćwiczenie 2"],
        "Pull": ["ćwiczenie 1", "ćwiczenie 2"]
    },
    "drugi plan": {
        "Upper": ["ćwiczenie 1", "ćwiczenie 2"],
        "Lower": ["ćwiczenie 1", "ćwiczenie 2"]
    }
}

# Uruchomienie aplikacji
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PrzegladajPlanyPage(przykladowe_plany)
    window.setWindowTitle("Przeglądaj Plany")
    window.resize(400, 300)  # Rozmiar okna
    window.show()
    sys.exit(app.exec_())
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
import currency_converter
# si besoin de command line
import sys

# 1 Creation de la classe custom ré*
# presentant la fenetre principale
#Subclass QMainWindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Currency Converter")
        # self.setFixedSize(QSize(400, 300)) # fixer le size
    # 6. Les elements de la fenetres
        layout = QHBoxLayout()
        self.cbb_from = QComboBox()
        self.spn_montant = QSpinBox()
        self.cbb_to = QComboBox()
        self.spn_montantConverti = QSpinBox()
        self.button_invert = QPushButton("Inverser Devises")
        layout.addWidget(self.cbb_from)
        layout.addWidget(self.spn_montant)
        layout.addWidget(self.cbb_to)
        layout.addWidget(self.spn_montantConverti)
        layout.addWidget(self.button_invert)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.set_default_values()
        # placer le widget au milieu de la fenetre.
        #self.setCentralWidget(button)
    def set_default_values(self):
        self.cbb_from.addItems(sorted(self.c.currencies)) # convert set to sorted list of currencies
        self.cbb_to.addItems(sorted(self.c.currencies)) # convert set to sorted list of currencies
        self.cbb_from.setCurrentText('EUR')
        self.cbb_to.setCurrentText('EUR')
        
# 2. Creation d'application globale avec l'option de CL args
app = QApplication(sys.argv)
#si pas besoin de commande line args
# app = QApplication([]) 

# 4. Création(intantiation) de la fenetre (windows)
window = MainWindow()

# 5. Affichage de la fenetre 
window.show()

# 3. Excution de l'application 
app.exec_()
        
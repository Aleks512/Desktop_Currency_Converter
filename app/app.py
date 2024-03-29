import decimal

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    # QCheckBox,
    QComboBox,
    # QDateEdit,
    # QDateTimeEdit,
    # QDial,
    # QDoubleSpinBox,
    # QFontComboBox,
    # QLabel,
    # QLCDNumber,
    # QLineEdit,
    QMainWindow,
    # QProgressBar,
    QPushButton,
    # QRadioButton,
    # QSlider,
    QSpinBox,
    # QTimeEdit,
    # QVBoxLayout,
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
        self.curr = currency_converter.CurrencyConverter()
        self.setWindowTitle("Currency Converter")
        self.setFixedSize(QSize(600, 300)) # fixer le size
    # 6. Les elements de notre window
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
        self.setup_connections()
        self.set_up_css()

        # placer le widget au milieu de la fenetre.
        #self.setCentralWidget(button)
    def set_up_css(self):
        self.setStyleSheet("""
        background-color:rgb(30,30,30);
        color: rgb(240,240,240);
        border : none;
        """)
        self.button_invert.setStyleSheet("background-color: rgb(20,100,20)")
    def set_default_values(self):
        self.cbb_from.addItems(sorted(self.curr.currencies)) # convert set to sorted list of currencies
        self.cbb_to.addItems(sorted(self.curr.currencies)) # convert set to sorted list of currencies
        self.cbb_from.setCurrentText('EUR')
        self.cbb_to.setCurrentText('EUR')
        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)

    # creation des signaux (connecting widgets to methodes compute & inverser_devises)
    def setup_connections(self):
        self.cbb_from.activated.connect(self.compute)
        self.cbb_to.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute) # en changant la valeur dans spinBox cela va connect to method compute
        self.button_invert.clicked.connect(self.inverser_devises)
    def compute(self):
        montant = self.spn_montant.value() #int
        devise_from = self.cbb_from.currentText()
        devise_to = self.cbb_to.currentText()
        try:
            resultat = self.curr.convert(montant, devise_from, devise_to)
            print(resultat)
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversion n'a pas fonctionné ")
        else:
            self.spn_montantConverti.setValue(resultat)


    def inverser_devises(self):
        devise_from = self.cbb_from.currentText()
        devise_to = self.cbb_to.currentText()
        self.cbb_from.setCurrentText(devise_to)
        self.cbb_to.setCurrentText(devise_from)
        self.compute()
        
# 2. Creation d'application globale avec l'option de CL args
app = QApplication(sys.argv)
#si pas besoin de commande line args
# app = QApplication([]) 

# 4. Création(intantiation) de la fenetre (windows)
window = MainWindow()

# 5. Affichage de la fenetre 
window.show()

# 3. Excution de l'application 
app.exec()
        
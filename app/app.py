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
# si besoin de command line
import sys

# 1 Creation de la classe custom ré*
# presentant la fenetre principale
#Subclass QMainWindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter")  
        # self.setFixedSize(QSize(400, 300)) # fixer le size
    # 6. Les elements de la fenetres
        layout = QHBoxLayout()
        cbb_from = QComboBox()
        spn_montant = QSpinBox()
        cbb_to = QComboBox()
        spn_montantConverti = QSpinBox()
        button_invert = QPushButton("Inverser Devises")
        layout.addWidget(cbb_from)
        layout.addWidget(spn_montant)
        layout.addWidget(cbb_to)
        layout.addWidget(spn_montantConverti)
        layout.addWidget(button_invert)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # placer le widget au milieu de la fenetre.
        #self.setCentralWidget(button)
        
        
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
        
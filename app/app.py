from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# si besoin de command line
import sys

# 1 Creation de la classe custom répresentant la fenetre principale
#Subclass QMainWindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter")  
    # 6. Les elements de la fenetres
        
        
# 2. Creation d'application globale avc l'option de CL args
app = QApplication(sys.argv)
#si pas besoin de commande line args
# app = QApplication([]) 

# 4. Création(intantiation) de la fenetre (windows)
window = MainWindow()
# 5. Affichage de la fenetre 
window.show()

# 3. Excution de l'application 
app.exec_()
        
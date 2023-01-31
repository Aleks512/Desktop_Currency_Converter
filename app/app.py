from PySide6 import QtWidgets

# a1 Creation de la classe répresentant la fenetre 
class Application(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
# 2. Creation d'application globale
app = QtWidgets.QApplication([])

# 4. Création(intantiation) de la fenetre (windows)
win = Application()
# 5. Affichage de la fenetre 
win.show()


# 3. Excution de l'application 
app.exec_()
        
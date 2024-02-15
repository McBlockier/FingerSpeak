import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.uic import loadUi
from UI.Implements import ThreadWorker, MethodsWindow, hoverButton

class InitRecognizer(QMainWindow, MethodsWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz desde el archivo .ui
        loadUi('GUI.ui', self)

        self.initializeComponents()
        self.initializeVariables()
        self.initializeStyles()

    def initializeVariables(self):
        #Método para declarar variables globales de la clase
        self.version.setText("v0.1 Alpha")
        self.mode.setText("Modo de reconocimiento: ")
        self.modeDefault = "Abecedario"
        self.setMode.setText(self.modeDefault)

        self.letters = ""


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLetter)
        self.timer.start(1000)  # Actualiza cada 1s
        self.index = 0

    def initializeComponents(self):
        #Método para inicializar los componetes, como ligar eventos a boton
        self.StartButton.clicked.connect(self.on_start_button_clicked)#Ligamos evento a botón
        self.StartTranslate.clicked.connect(self.on_start_button_clicked_translate)#Ligamos otro evento a botón

    def initializeStyles(self):
        # Método para inicializar el CSS, donde se encuentran los estilos para los botones
        try:
            with open('StylesButton.css', 'r') as f:
                styles = f.read()
                self.setStyleSheet(styles)  # Usar self en lugar de app
        except Exception as ex:
            print(f"Hubo un error al inicializar los estilos: {ex}")

    def updateLetter(self):
        try:
            if self.index < len(self.letters):
                self.index += 1
                self.labelDetect.setText(self.letters[:self.index])
                print("Entro a la impresion")
        except Exception as ex:
            print(f"There are a throw except an point -> {ex} line 55")

    def print_letter(self, letter):
        self.letters = letter

    def print_letter(self, letter):
        try:
            print("Letra detectada: ", letter)
        except Exception as ex:
            print(f"There are a throw except an point -> {ex} line 64")

    def on_start_button_clicked(self):
        try:
            self.setMode.setText("Abecedario")#Establecemos el modo de operación del programa
            from DataSet import inference_classifier#Hacemos una importación local desde el paquete DataSet
            Recognizer = inference_classifier.Recognizer()
            Recognizer.startCamera()
        except Exception as ex:
            print(f"There are a throw except an point -> {ex} at line 48")

    def on_start_button_clicked_translate(self):
        try:
            self.setMode.setText("Traducción en tiempo real")
            #Sin implementación todavia
        except Exception as ex:
            print(f"There are a throw except an point -> {ex} line 80")


if __name__ == "__main__":
    # Inicializar la aplicación de PyQt
    app = QApplication(sys.argv)
    # Crear una instancia de la ventana
    ventana = InitRecognizer()
    # Mostrar la ventana
    ventana.show()
    # Ejecutar el bucle de eventos de la aplicación
    sys.exit(app.exec_())
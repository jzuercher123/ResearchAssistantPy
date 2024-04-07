import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLineEdit

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Python GUI with PyQt')
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        self.output_text = QTextEdit()
        layout.addWidget(self.output_text)

        button_layout = QHBoxLayout()
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_function)
        button_layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_function)
        button_layout.addWidget(self.stop_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def start_function(self):
        # Add your function logic here
        input_text = self.input_text.text()
        output_text = f'Output from function with input: {input_text}'
        self.output_text.setText(output_text)

    def stop_function(self):
        self.output_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_gui = MyGUI()
    my_gui.show()
    sys.exit(app.exec_())
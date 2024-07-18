from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QToolBox
)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(600, 400, 410, 250)
        self.main_box = QHBoxLayout()
        self.box1 = QVBoxLayout()
        self.box2 = QVBoxLayout()
        self.box3 = QVBoxLayout()

        #box1
        self.box1_1 = QToolBox(self)
        self.box1_2 = QToolBox(self)
        self.box1_3 = QToolBox(self)

        self.box1.addWidget(self.box1_1)
        self.box1.addWidget(self.box1_2)
        self.box1.addWidget(self.box1_3)

        self.box1_1.setStyleSheet("""
            QToolBox{
                background-color: red;
            }
        """)

        self.box1_2.setStyleSheet("""
            QToolBox{
                background-color: yellow;
            }
        """)
        self.box1_3.setStyleSheet("""
            QToolBox{
                background-color: purple;
            }
        """)

        #

        #box 2
        self.box2_1 = QToolBox(self)

        self.box2.addWidget(self.box2_1)
        self.box2_1.setStyleSheet("""
            QToolBox{
                background-color: green;
            }
        """)

        # 


        #box3
        self.box3_1 = QToolBox(self)
        self.box3_2 = QToolBox(self)

        self.box3.addWidget(self.box3_1)
        self.box3.addWidget(self.box3_2)

        self.box3_1.setStyleSheet("""
            QToolBox{
                background-color: red;
            }
        """)
        self.box3_2.setStyleSheet("""
            QToolBox{
                background-color: purple;
            }
        """)

        #


        self.main_box.addLayout(self.box1)
        self.main_box.addLayout(self.box2)
        self.main_box.addLayout(self.box3)

        self.setLayout(self.main_box)
        self.show()

app = QApplication([])

win = Window()
app.exec_()
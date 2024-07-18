from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(700, 350, 360, 450)
        self.setFixedSize(400,470)
        self.setStyleSheet("background-color: #bec5d6")
        self.setWindowTitle("Calculator")
        self.setStyleSheet("font-size: 20px;")

        #box, btn, edit, lable ochilishi -->

        self.display = ""

        self.main_box = QVBoxLayout()
        self.enter_num = QLineEdit(self)
        self.error_label = QLabel("           ", self)
        self.box1 = QHBoxLayout()
        self.box2 = QHBoxLayout()
        self.box3 = QHBoxLayout()
        self.box4 = QHBoxLayout()
        self.box5 = QHBoxLayout()


        #box1

        self.all_clear_btn = QPushButton("C", self)
        self.bracket_btn = QPushButton("(", self)
        self.ed_bracket_btn = QPushButton(")", self)
        self.slash_btn = QPushButton("/", self)

        self.all_clear_btn.clicked.connect(self.outclear)
        self.bracket_btn.clicked.connect(self.press)
        self.ed_bracket_btn.clicked.connect(self.press)
        self.slash_btn.clicked.connect(self.press)

        self.box1.addWidget(self.all_clear_btn)
        self.box1.addWidget(self.bracket_btn)
        self.box1.addWidget(self.ed_bracket_btn)
        self.box1.addWidget(self.slash_btn)

        #

        #box2
        self.num_btn7 = QPushButton("7", self) 
        self.num_btn8 = QPushButton("8", self) 
        self.num_btn9 = QPushButton("9", self) 
        self.num_multiplication = QPushButton("*", self) 

        self.num_btn7.clicked.connect(self.press)
        self.num_btn8.clicked.connect(self.press)
        self.num_btn9.clicked.connect(self.press)
        self.num_multiplication.clicked.connect(self.press)
        

        self.box2.addWidget(self.num_btn7)
        self.box2.addWidget(self.num_btn8)
        self.box2.addWidget(self.num_btn9)
        self.box2.addWidget(self.num_multiplication)

        #

        #box3
        self.num_btn4 = QPushButton("4", self)
        self.num_btn5 = QPushButton("5", self)
        self.num_btn6 = QPushButton("6", self)
        self.num_minus = QPushButton("-", self)

        self.num_btn4.clicked.connect(self.press)
        self.num_btn5.clicked.connect(self.press)
        self.num_btn6.clicked.connect(self.press)
        self.num_minus.clicked.connect(self.press)

        self.box3.addWidget(self.num_btn4)
        self.box3.addWidget(self.num_btn5)
        self.box3.addWidget(self.num_btn6)
        self.box3.addWidget(self.num_minus)
        #

        
        #box4
        self.num_btn1 = QPushButton("1", self)
        self.num_btn2 = QPushButton("2", self)
        self.num_btn3 = QPushButton("3", self)
        self.num_plus = QPushButton("+", self)

        self.num_btn1.clicked.connect(self.press)
        self.num_btn2.clicked.connect(self.press)
        self.num_btn3.clicked.connect(self.press)
        self.num_plus.clicked.connect(self.press)

        self.box4.addWidget(self.num_btn1)
        self.box4.addWidget(self.num_btn2)
        self.box4.addWidget(self.num_btn3)
        self.box4.addWidget(self.num_plus)
        #

        #box 5
        self.clear_btn = QPushButton("<--", self)
        self.zero_btn = QPushButton("0", self)
        self.point_btn = QPushButton(".", self)
        self.equal_btn = QPushButton("=", self)

        self.clear_btn.clicked.connect(self.one_del)
        self.zero_btn.clicked.connect(self.press)
        self.point_btn.clicked.connect(self.press)
        self.equal_btn.clicked.connect(self.calculate)

        self.box5.addWidget(self.clear_btn)
        self.box5.addWidget(self.zero_btn)
        self.box5.addWidget(self.point_btn)
        self.box5.addWidget(self.equal_btn)
        #


        #(box, btn, edit, lable)<--


        # style -->
        
        app.setStyleSheet("""
            QPushButton{
                border: 1.5px solid #6c6d6f;
                background-color: #c0c3c7;
                padding: 10 15
            }
        """)


        self.enter_num.setFixedHeight(55)
        self.enter_num.setStyleSheet("""
        QLineEdit {
            border: 1.5px solid #003ac3;                   
            padding: 5px;
        }

        """)

        self.error_label.setStyleSheet("""
            QLabel{
                color: red;
            }
        """)


        # style <--

        #main boxga qo'shish
        self.main_box.addWidget(self.enter_num)
        self.main_box.addWidget(self.error_label)
        self.main_box.addLayout(self.box1)
        self.main_box.addLayout(self.box2)
        self.main_box.addLayout(self.box3)
        self.main_box.addLayout(self.box4)
        self.main_box.addLayout(self.box5)
        self.setLayout(self.main_box)
        self.show()

        #function -->
    def press(self):
        btn = self.sender()
        self.display += btn.text()
        self.enter_num.setText(self.display)
        self.error_label.setText("")

        self.enter_num.setStyleSheet("""
                QLineEdit {
                border: 1.5px solid #003ac3;                   
                padding: 5px;
                }
            """)

    def outclear(self):
        if not self.display:
            self.error_label.setText("Raqamlar mavjut emas")
        else:
            self.enter_num.clear()
            self.display = ""
            self.error_label.setText("")
        self.enter_num.setStyleSheet("""
                QLineEdit {
                border: 1.5px solid #003ac3;                   
                padding: 5px;
                }
        """)
    
    def one_del(self):
        self.enter_num.setText(self.display[:-1])
        self.display = self.display[:-1]
    def calculate(self):
        i = 1
        try:
            self.enter_num.setText(str(eval(self.display)))
            with open("V2/history", "w") as f:
                f.write(str(i) + "-" + str(eval(self.display)) + "\n")
                i += 1
            self.display = str(eval(self.display))
        except SyntaxError:
            self.error_label.setText("Input bo'sh holatda")
        except ZeroDivisionError:
            self.error_label.setText("0 ga bo'linmyadi!")
            self.enter_num.setStyleSheet("""
                QLineEdit {
                border: 1.5px solid red;                   
                padding: 5px;
                }
            """)

        #function <--


app = QApplication([])
win = Window()
app.exec_()

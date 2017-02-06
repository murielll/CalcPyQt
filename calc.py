import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


ExpressionString = ""


def ButtonClick(CalcButton):
    def wrapper():
        global ExpressionString
        if CalcButton == "C":
            ExpressionString = ""
            w.DisplayCalc.setText("0")
            return
        if CalcButton == r"=":
            if not ExpressionString:
                w.DisplayCalc.setText("No input data!")
                return
            try:
                w.DisplayCalc.setText(str(eval(ExpressionString)))
            except SyntaxError:
                w.DisplayCalc.setText("Error occured!")
            ExpressionString = ""
            return
        else:
            if not ExpressionString:
                w.DisplayCalc.clear()
            if CalcButton in (r"-", r"+", r"*", r"/", r".") and \
                    ExpressionString.endswith((r"-", r"+", r"*", r"/", r".")):
                return
            if ExpressionString.endswith("0") and CalcButton \
                    not in (r"-", r"+", r"*", r"/", r"."):
                ExpressionString = ExpressionString[:-1] + CalcButton
                w.DisplayCalc.setText(w.DisplayCalc.text()[:-1] +
                                      CalcButton)
                return
            ExpressionString += CalcButton
            w.DisplayCalc.setText(w.DisplayCalc.text() + CalcButton)
    return wrapper


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = uic.loadUi("calcwindow.ui")
    w.resize(300, 360)
    w.move(300, 300)
    w.setWindowTitle('Calculator')
    w.show()

    w.Button_0.clicked.connect(ButtonClick("0"))

    w.Button_1.clicked.connect(ButtonClick("1"))

    w.Button_2.clicked.connect(ButtonClick("2"))

    w.Button_3.clicked.connect(ButtonClick("3"))

    w.Button_4.clicked.connect(ButtonClick("4"))

    w.Button_5.clicked.connect(ButtonClick("5"))

    w.Button_6.clicked.connect(ButtonClick("6"))

    w.Button_7.clicked.connect(ButtonClick("7"))

    w.Button_8.clicked.connect(ButtonClick("8"))

    w.Button_9.clicked.connect(ButtonClick("9"))

    w.Button_C.clicked.connect(ButtonClick(r"C"))

    w.Button_plus.clicked.connect(ButtonClick(r"+"))

    w.Button_minus.clicked.connect(ButtonClick(r"-"))

    w.Button_division.clicked.connect(ButtonClick(r"/"))

    w.Button_multiplication.clicked.connect(ButtonClick(r"*"))

    w.Button_equal.clicked.connect(ButtonClick(r"="))

    w.Button_dot.clicked.connect(ButtonClick(r"."))

# Bind on menu Exit function
    w.actionExit.triggered.connect(app.exit)

    sys.exit(app.exec_())

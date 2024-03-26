from controller import *


def main():
    app = QApplication([])
    window = Controller()
    window.setupUi(window)
    window.makeUIWork()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

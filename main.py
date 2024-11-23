import sys
from PyQt5.QtWidgets import QApplication
from gui import BTCPriceTrackerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = BTCPriceTrackerApp()
    main_window.show()
    sys.exit(app.exec_())

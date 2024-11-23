from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt  # Import Qt for alignment
from btc_tracker import get_btc_price

class BTCPriceTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BTC Price Tracker")
        self.setGeometry(100, 100, 400, 200)

        # Label to display BTC price
        self.price_label = QLabel("Fetching BTC price...", self)
        self.price_label.setStyleSheet("font-size: 20px;")
        self.price_label.setAlignment(Qt.AlignCenter)

        # Refresh button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.update_price)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.price_label)
        layout.addWidget(self.refresh_button)

        # Main widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Timer for auto-refresh
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_price)
        self.timer.start(4000)  # Refresh every 60 seconds

        self.update_price()  # Initial price update

    def update_price(self):
        price = get_btc_price()
        if price is not None:
            self.price_label.setText(f"Current BTC Price: ${price}")
        else:
            self.price_label.setText("Failed to fetch BTC price.")

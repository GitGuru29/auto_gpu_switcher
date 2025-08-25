import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QComboBox, QHBoxLayout, QMessageBox)
from .service import GPUSwitcherService

class GPUSwitcherGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto GPU Switcher")
        self.service = GPUSwitcherService()
        self.init_ui()
        self.refresh_status()

    def init_ui(self):
        layout = QVBoxLayout()

        self.status_label = QLabel("Status: Not running")
        layout.addWidget(self.status_label)

        self.start_btn = QPushButton("Start Service")
        self.start_btn.clicked.connect(self.start_service)
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop Service")
        self.stop_btn.clicked.connect(self.stop_service)
        self.stop_btn.setEnabled(False)
        layout.addWidget(self.stop_btn)

        self.refresh_btn = QPushButton("Refresh Status")
        self.refresh_btn.clicked.connect(self.refresh_status)
        layout.addWidget(self.refresh_btn)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["App", "Learned", "Manual Override"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def start_service(self):
        self.service.start()
        self.status_label.setText("Status: Running")
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

    def stop_service(self):
        self.service.stop()
        self.status_label.setText("Status: Stopped")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def refresh_status(self):
        status = self.service.get_status()
        learned = status["learned"]
        overrides = status["manual_overrides"]
        self.table.setRowCount(0)
        all_apps = set(learned.keys()) | set(overrides.keys())
        for row, app in enumerate(sorted(all_apps)):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(app))
            self.table.setItem(row, 1, QTableWidgetItem(learned.get(app, "")))
            self.table.setItem(row, 2, QTableWidgetItem(learned.get(app, "")))

    def set_override(self):
        app = self.app_input.text().strip()
        gpu = self.gpu_select.currentText()
        if not app():
            QMessageBox.warning(self, "Input Error", "Please enater an app name.")
            return
        self.service.set_manual_override(app, gpu)
        QMessageBox.information(self, "Override Set", f"{app} -> {gpu}")
        self.refresh_status()

def main():
    app = QApplication(sys.argv)
    gui = GPUSwitcherGUI()
    gui.show()
    sys.exit(app.exec_())


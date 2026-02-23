from PySide6.QtWidgets import QMainWindow, QTextEdit
from PySide6.QtGui import QFont
from interfaces.data_source import ILogSource


class MainWindow(QMainWindow):
    def __init__(self, log_source: ILogSource):
        super().__init__()
        self.log_source = log_source
        self._setup_ui()
        self.load_logs()

    def _setup_ui(self):
        self.setWindowTitle("Advanced Log Viewer")
        self.resize(1000, 700)

        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        
        font = QFont("Consolas", 11) if "Consolas" in QFont().families() else QFont("Monospace", 11)
        font.setStyleHint(QFont.Monospace)
        self.log_display.setFont(font)
        
        self.setCentralWidget(self.log_display)

    def load_logs(self):
        data = self.log_source.get_logs()
        self.log_display.setPlainText("\n".join(data))

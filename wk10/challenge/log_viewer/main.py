import os
from PySide6.QtWidgets import QApplication
from services.mock_source import MockLogSource
from services.log_factory import LogFactory
from ui.main_window import MainWindow

def main():
    app = QApplication([])

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "logs", "voters.csv")
    
    use_mock = False
    log_source = MockLogSource() if use_mock else LogFactory.create_source(file_path)

    viewer = MainWindow(log_source)
    viewer.show()

    app.exec()

if __name__ == "__main__":
    main()

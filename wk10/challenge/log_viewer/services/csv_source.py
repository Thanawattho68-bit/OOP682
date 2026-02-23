import csv
from interfaces.data_source import ILogSource


class CsvLogSource(ILogSource):
    def __init__(self, filename):
        self.filename = filename

    def get_logs(self):
        try:
            with open(self.filename, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [
                    f"Name: {row['ชื่อ']:<20} | "
                    f"Age: {row['อายุ']:<3} | "
                    f"Province: {row['จังหวัด']:<15} | "
                    f"Party: {row['พรรคที่เลือก']}"
                    for row in reader
                ]
        except FileNotFoundError:
            return ["Error: CSV file not found"]
        except Exception as e:
            return [f"Error reading CSV: {str(e)}"]

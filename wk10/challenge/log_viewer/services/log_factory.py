from services.file_source import FileLogSource
from services.csv_source import CsvLogSource


class LogFactory:
    _MAPPING = {
        ".csv": CsvLogSource,
        ".log": FileLogSource,
    }

    @classmethod
    def create_source(cls, filename: str):
        filename_lower = filename.lower()
        
        for ext, source_class in cls._MAPPING.items():
            if filename_lower.endswith(ext):
                return source_class(filename)
                
        raise ValueError(f"Unsupported file type for: {filename}")

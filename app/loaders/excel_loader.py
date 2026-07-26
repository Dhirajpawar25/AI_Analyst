import pandas as pd
from app.loaders.base_loader import BaseLoader
from app.models.document import Document

class ExcelLoader(BaseLoader):
    def load(self, document: Document):
        df = pd.read_excel(document.storage_path)
        return df
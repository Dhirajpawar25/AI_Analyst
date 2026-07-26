import pandas as pd
from app.loaders.base_loader import BaseLoader
from app.models.document import Document

class CSVLoader(BaseLoader):
    def load(self, document: Document):
        df = pd.read_csv(document.storage_path)
        return df
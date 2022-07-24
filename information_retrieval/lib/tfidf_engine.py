from information_retrieval.lib.base_engine import BaseEngine

from information_retrieval.lib.quran_mir.preprocess_quran_text import quran_normalizer, quran_series
from information_retrieval.lib.quran_mir.tfidf_vectorizer import get_most_similars


class TFIDFEngine(BaseEngine):

    @staticmethod
    def process_query(text):
        results = list(get_most_similars(quran_series, quran_normalizer(text), 10)['آیه'])
        return [
            {
                "verse": result,
                "verse_number": 1,
                "surah_name": "Baghareh",
            } for result in results
        ]

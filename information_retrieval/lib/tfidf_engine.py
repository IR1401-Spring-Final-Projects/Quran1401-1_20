from information_retrieval.lib.base_engine import BaseEngine
from information_retrieval.lib.quran_mir.preprocess_quran_text import quran_normalizer, quran_series
from information_retrieval.lib.quran_mir.quran_ir import TfIdfQuranIR


class TFIDFEngine(BaseEngine):
    ir_model = None

    @staticmethod
    def get_ir_model():
        if TFIDFEngine.ir_model is None:
            TFIDFEngine.ir_model = 1
            TFIDFEngine.ir_model = TfIdfQuranIR()
        return TFIDFEngine.ir_model

    @staticmethod
    def process_query(text, k=10):
        tfidf_quran_ir = TFIDFEngine.get_ir_model()
        result_df = tfidf_quran_ir.get_most_similars(quran_normalizer(text), K=k)
        return BaseEngine.dataframe_to_dict(result_df)

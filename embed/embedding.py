from sentence_transformers import SentenceTransformer

class load_model:
    def __init__(self, text: list[dict]) -> None:
        self.text=text
        self.embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")

    def encode(self):
        for item in self.text:
            item['embedding'] = self.embedding_model.encode(item["sentence_chunk"])
        return self.text

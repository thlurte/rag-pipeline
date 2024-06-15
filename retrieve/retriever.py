from sentence_transformers import util, SentenceTransformer
import torch
import numpy as np

class similarity_search:
    def __init__(self,query: str, text: list[dict]) -> None:
        self.query = query
        self.text = text
        self.embeddings = self._process(text)
        self.embedding_model = SentenceTransformer(model_name_or_path='all-mpnet-base-v2')

    def _process(self,text: list[dict]):
        # for some reason do this
        return torch.tensor(np.array([i['embedding'] for i in text]),dtype=torch.float32)

    def retrieve(self):
        query_embedding=self.embedding_model.encode(self.query,convert_to_tensor=True)
        dot_scores=util.dot_score(a=query_embedding,b=self.embeddings)[0]
        return torch.topk(dot_scores,k=5)

    

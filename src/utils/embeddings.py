""" embedings loader for sentence-transformers """

from sentence_transformers import SentenceTransformer

class SentenceEmbedder:
    def __init__(self):
        self._model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")
        self.dim = 384

    def encode_with_usage(self, texts):
        # only list
        batch = [texts] if isinstance(texts, str) else texts
        vectors = self._model.encode(batch)
        token_count = sum(len(t.split()) for t in batch)
        usage = {"prompt_tokens": token_count, "total_tokens": token_count}
        vecs = vectors.tolist() if hasattr(vectors, "tolist") else [v.tolist() for v in vectors]
        return (vecs[0] if isinstance(texts, str) else vecs, usage)

    def encode(self, texts):
        return self._model.encode(texts).tolist()

print("embedder ready.")

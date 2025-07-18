from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedding_fn = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"  # using minilm for embedding
)

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="chapters",
    embedding_function=embedding_fn
)
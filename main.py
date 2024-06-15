from preprocess.indexing import chunking, process_pdf 
from embed.embedding import load_model
from retrieve.retriever import similarity_search
from generate.generator import load_llm
document = process_pdf('/home/ahmed/Downloads/b.pdf')

text_chunks = chunking(10,document.open_and_read_pdf()).chunk_and_split_text()

embedding_model = load_model(text_chunks)
embeddings = embedding_model.encode()
retriever = similarity_search(query="What is concurrency",text=embeddings)

top_k = retriever.retrieve()

llm = load_llm(top_k, embeddings,"What is concurrency")
print(llm.chat())

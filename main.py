from preprocess.indexing import chunking, process_pdf 
from embed.embedding import load_model
document = process_pdf('/home/ahmed/Downloads/b.pdf')
text_chunks = chunking(10,document.open_and_read_pdf()).chunk_and_split_text()
embedding_model = load_model(text_chunks)
print(embedding_model.encode())


from embed.embedding import load_model
from generate.generator import load_llm
from retrieve.retriever import similarity_search
from preprocess.indexing import chunking, process_pdf

def main():
    # Preprocessing
    document = process_pdf('/home/ahmed/Downloads/b.pdf')
    text_chunks = chunking(10,document.open_and_read_pdf()).chunk_and_split_text()
    
    #  Embedding
    embedding_model = load_model(text_chunks)
    embeddings = embedding_model.encode()
    
    # Retrieval
    query="What is concurrency"
    retriever = similarity_search(query=query,text=embeddings)
    top_k = retriever.retrieve()

    # Generation
    llm = load_llm(top_k, embeddings,query)
    response = llm.chat()

    print(response)

if __name__ == "__main__":
    main()

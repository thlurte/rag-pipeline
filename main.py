from preprocess.indexing import chunking, process_pdf 

document = process_pdf('/home/ahmed/Downloads/b.pdf')
text_chunks = chunking(10,document.open_and_read_pdf()).chunk_and_split_text()
print(text_chunks)

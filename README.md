# RAG Pipeline

Retrieval-Augmented Generation (RAG) is an approach to enhance LLMs by retrieving relevant document chunks from external knowledge base through semantic similarity calculation. 

![[assets/a.png]]

A typical RAG workflow begins with the creation of an index comprising external sources. This index will later be used for retrieving relevant information through a retriever model based on a specific query. The final step involves a generator model, which combines the retrieved information with the query to produce the desired output.
 
### Indexing
Indexing starts with the cleaning and extraction of raw data in diverse formats like PDF, HTML, Word, and Markdown, which is then converted into a uniform plain text format. 

Since there is a need to consider the context limitations of language model, text is segmented into smaller, digestible chunks. This will later help to to facilitate more focused searches, allowing for the pinpointing of segments containing pertinent keywords. 

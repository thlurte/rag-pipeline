import fitz
from spacy.lang.en import English
import re

class process_pdf:
    def __init__(self,path) -> None:
        self.path=path

    def text_formatter(self, text: str) -> str:
        """ Text formatting """
        cleaned_text=text.replace("\n","").strip()
        return cleaned_text

    def open_and_read_pdf(self) -> list[dict]:
        """ Returns the details of PDF file with text """
        document = fitz.open(self.path)
        page_details = []
        for page_number, page in enumerate(document):
            text = self.text_formatter(page.get_text())
            page_details.append({
                "page_number": page_number+1 ,
                "page_char_count": len(text),
                "page_word_count": len(text.split(" ")),
                "page_sentence_count_raw": len(text.split(". ")),
                "page_token_count": len(text) / 4,
                "text": text
            })
        return page_details

class chunking:
    def __init__(self,size: int, text: list[dict]) -> None:
        self.size=size
        self.text=self._sentencizer(text)

    def _sentencizer(self,text: list[dict]):
        sentencizer = English()
        sentencizer.add_pipe("sentencizer")
        for item in text:
            item["sentences"]=list(sentencizer(item['text']).sents)
            item["sentences"] = [str(sentence) for sentence in item["sentences"]]
            item["page_sentence_count_spacy"] = len(item["sentences"])
        return text

    def _chunk(self,text: str):
        return [text[i:i + self.size] for i in range(0, len(text), self.size)]
    
    def chunk_and_split_text(self):
        for item in self.text:
            item["sentence_chunks"]=self._chunk(item['sentences'])
            item['num_chunks']=len(item["sentence_chunks"])
        
        pages_and_chunks=[]
        
        for item in self.text:
            for sen_chunk in item["sentence_chunks"]:
                chunk_dict={}
                chunk_dict["page_number"] = item["page_number"]

                joined_sentence_chunk = "".join(sen_chunk).replace("  ", " ").strip()
                joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sentence_chunk) # ".A" -> ". A" for any full-stop/capital letter combo 
                chunk_dict["sentence_chunk"] = joined_sentence_chunk

                # Get stats about the chunk
                chunk_dict["chunk_char_count"] = len(joined_sentence_chunk)
                chunk_dict["chunk_word_count"] = len([word for word in joined_sentence_chunk.split(" ")])
                chunk_dict["chunk_token_count"] = len(joined_sentence_chunk) / 4 # 1 token = ~4 characters
                
                pages_and_chunks.append(chunk_dict)
        return pages_and_chunks




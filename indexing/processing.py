import fitz


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
                "page_number": page_number - 41,
                "page_char_count": len(text),
                "page_word_count": len(text.split(" ")),
                "page_sentence_count_raw": len(text.split(". ")),
                "page_token_count": len(text) / 4,
                "text": text
            })
        return page_details

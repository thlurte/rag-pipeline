import google.generativeai as genai

class load_llm:
    def __init__(self,top_k,results,prompt) -> None:
        genai.configure(api_key='mehh....')
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        self.llm = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
        )
        self.chat_session = self.llm.start_chat(
        history=[]
        )
        self.top_k = top_k
        self.results = results
        self.context = self._context_formatting()
        self.prompt = prompt

    def _context_formatting(self):
        context=""
        for i in list(self.top_k)[1]:
            context = context+self.results[i.numpy()]['sentence_chunk']
        return context

    def chat(self):
        self.response = self.chat_session.send_message("Using the following context, answer the question below"+self.context+"\n\n"+self.prompt)
        return self.response.text


        

import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path,"config.json")) as f:
    data = json.load(f)

import google.generativeai as genai
genai.configure(api_key=data["google_api_key"])
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

class Model:
    def __init__(self,safety_settings=safety_settings,temperature=0.9,top_p=1,top_k=1,max_output_tokens=2048):
        self.generation_config = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens,
        }
        self.model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=self.generation_config,
                              safety_settings=safety_settings)
    def get_text(self,prompt):
        # prompt_parts = [
        #     prompt
        # ]
        # response = self.model.generate_content(prompt_parts)
        chat = self.model.start_chat(history=[])
        response = chat.send_message(prompt)
        return response.text
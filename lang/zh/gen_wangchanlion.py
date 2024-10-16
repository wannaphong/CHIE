import os
import pathlib
import transformers
import torch
import pandas as pd
from tqdm.auto import tqdm
import argparse


root_dir=pathlib.Path(__file__).parent.resolve()

eval_df = pd.read_csv(os.path.join(root_dir,"eval.csv"))


parser = argparse.ArgumentParser()
parser.add_argument("-m","--model", help="HuggingFace model id",default="airesearch/WangchanLion7B")
args = parser.parse_args()


model_id = args.model
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
# tokenizer.eos_token=""

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.float16},
    device_map="auto",
    return_full_text=False,
    trust_remote_code=True,
    tokenizer=tokenizer,
    eos_token_id = tokenizer.eos_token_id
)

predictions=[]

for reference,context,question in tqdm(list(zip(eval_df.references,eval_df.context,eval_df.question))):
    prompt = f"""Background: {context}

Question: {question}

Answer:"""
    outputs = pipeline(prompt, max_new_tokens=512, do_sample=False)  # Don't change do_sample=False
    # print(outputs)
    predictions.append(outputs[0]["generated_text"])

eval_df["predictions"]=predictions

eval_df.to_csv(model_id.split("/",1)[1]+".csv",index=False)
import os
import pandas as pd
import openai
from dotenv import load_dotenv
load_dotenv()

df = pd.read_csv("data.csv")
prompt = df.loc[0, 'prompt']

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME")

print(prompt)

response = openai.Completion.create(
    model=model_name,
    prompt=prompt,
    temperature=0,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response['choices'][0]['text'])
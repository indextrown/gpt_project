from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# 내용을 API에 요청
# completion_tokens: 받은 토큰
# prompt_tokens=53: 명령 토큰
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)


print(response.choices[0].message.content)
 
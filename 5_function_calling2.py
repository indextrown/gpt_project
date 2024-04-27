from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
# https://platform.openai.com/docs/guides/function-calling
load_dotenv()
client = OpenAI()

tools = [
    {
        "type": "function",
        "function": 
        {
            "name": "noname",
            "description": "내 아이피 주소 얻기",
            "parameters": 
            {
                "type": "object",
                "properties": 
                {
                    "명언": 
                    {
                        "type": "string",
                    },
                    "저자": 
                    {
                        "type": "string",
                    },
                    "국가": 
                    {
                        "type": "string",
                    },
                },
                "required": ["명언", "저자", "국가"], # 필수로 나오는거 이 부분은 json의 key
            },
        },
    }
]

messages = [{"role": "user", "content": "프로그래밍에 대한 명언 5개 알려주고 그 얘기를 누가 했는지 어떤 나라 사람이 말했는지 말해줘."}]

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=messages,
    tools=tools,
    tool_choice="auto",  # auto is default, but we'll be explicit
)

response_message = response.choices[0].message
tool_calls = response_message.tool_calls

for tool_call in tool_calls:
    #print(tool_call)
    print(tool_call.function.arguments)
    print()
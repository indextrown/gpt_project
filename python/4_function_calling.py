from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
# https://platform.openai.com/docs/guides/function-calling
load_dotenv()
client = OpenAI()

def get_my_ip():
  url = "https://api.ip.pe.kr/"
  res = requests.get(url)
  if res.status_code == 200:
    ip = res.text
    return json.dumps({"ip": ip}) #  str


tools = [
  {
      "type": "function",
      "function": {
          "name": "get_my_ip",
          "description": "내 아이피 주소 얻기",
          "parameters": {
              "type": "object",
              "properties": {
                  "ip": {
                      "type": "string",
                      "description": "my ipaddress",
                  },
                  # "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
              },
              "required": ["ip"], # 필수로 나오는거 이 부분은 json의 key
          },
      },
  }
]

messages = [{"role": "user", "content": "내 아이피 주소는 어떻게 되나요?"}]
#messages = [{"role": "user", "content": "안녕?"}]


response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=messages,
    tools=tools,
    tool_choice="auto",  # auto is default, but we'll be explicit
)

response_message = response.choices[0].message
# print(response_message)
tool_calls = response_message.tool_calls

if tool_calls:
  available_functions = {"get_my_ip": get_my_ip}
  messages.append(response_message)
  
  for tool_call in tool_calls:
      function_name = tool_call.function.name

      function_to_call = available_functions[function_name]
      function_args = json.loads(tool_call.function.arguments)
      function_response = function_to_call()
      #print("fs: ", function_response)
      messages.append(
          {
              "tool_call_id": tool_call.id,
              "role": "tool",
              "name": function_name,
              "content": function_response,
          }
      )  # extend conversation with function response
  second_response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=messages,
  )  # get a new response from the model where it can see the function response
  print(second_response)
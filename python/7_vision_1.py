# https://platform.openai.com/docs/guides/images/usage
from openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()

# OpenAI API Key
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        #{"type": "text", "text": "What’s in this image?"},
        {"type": "text", "text": "이 이미지에는 무엇이 있나요?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-x64HcbPDaGG80IBDkvuhQR1Z/user-N9ELYZ7JiFERFRbAODmOzenF/img-MsQOwLYHxQ6ql87Ew2tuXIXJ.png?st=2024-04-27T08%3A30%3A12Z&se=2024-04-27T10%3A30%3A12Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-04-26T23%3A47%3A27Z&ske=2024-04-27T23%3A47%3A27Z&sks=b&skv=2021-08-06&sig=E%2BySNNhzWJ8LSkaowv3N1c53%2B1e8EnoDM1oBN%2BqbJPw%3D",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
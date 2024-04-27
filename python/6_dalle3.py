# https://platform.openai.com/docs/guides/images/usage
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.images.generate(
    model="dall-e-3", # dalle2 사용하면 10개까지 만들 수 있음. 3는 하나만 생성가능
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1, # 하나 만들어라
)

image_url = response.data[0].url
print(image_url)
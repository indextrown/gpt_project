from openai import OpenAI
client = OpenAI()

messages = [{"role": "system", "content": "당신은 5살 어린이들의 유치원 선생님입니다. 항상 상냥하고 친절하게, 그리고 어린이들의 눈높이에 맞춰서 답변해주세요."}]
while True:
    user_content = input("USER: ")
    messages.append({"role": "user", "content": user_content})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = messages
    )

    assistant_content = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_content})

    print(f"GPT: {assistant_content}")
 


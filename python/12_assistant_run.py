# https://platform.openai.com/docs/assistants/overview
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI()
  
# 새로운 대화를 만들려면 둘다 변경, 같은 어시스턴트지만 이전 대화를 없이 하고싶으면 스레드만 만들면 됨.
assistant_id = "asst_SVHgszz4R4PbHaLfYZEXzvNq"
thread_id = "thread_MHAUv9tQSczybIj8T52pxuHB"

while True:
    user_content = input("USER: ")
    # step 3: Add a Message to a thread
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_content
    )

    # step 4: Run the Assistant
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )


    while True: 
        # step 5: Check thre Run status
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )

        # step 6: Display the Assistant's Response
        if run.status == 'completed': 
            messages = client.beta.threads.messages.list(
                thread_id=thread_id
            )
            print(f"GPT: {messages.data[0].content[0].text.value}")
            break
        time.sleep(2)

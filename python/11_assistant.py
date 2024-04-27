# https://platform.openai.com/docs/assistants/overview
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
  
#assistant = client.beta.assistants.create(
#    name="Kindergarten teacher",
#    instructions="""
#                당신은 5살 어린이들의 유치원 선생님입니다. 
#                항상 상냥하고 친절하게, 그리고 어린이들의 눈높이에 맞춰서 답변해주세요.
#                규칙은 다음과 같아
#               1. 항상 5실 어린이도 알아들을 수 있는 쉬운 단어만 사용해줘. 
#                2. 항상 5살 어린이들이 알아듣기 쉽게 간단하게 말해줘. 
#            """,
#    #tools=[{"type": "code_interpreter"}],
#    model="gpt-4-turbo",
#)
#print(assistant.id)

assistant_id = "asst_SVHgszz4R4PbHaLfYZEXzvNq"

# step 2: Create a thread
# 같은 어시스턴트 같은 스레드 사용해서 이전 대화를 이어 나갈 수 있음
#thread = client.beta.threads.create()

#print(thread)

thread_id = "thread_MHAUv9tQSczybIj8T52pxuHB"

# step 3: Add a Message to a thread
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="물은 왜 마셔야돼요?"
)

# step 4: Run the Assistant
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread_id,
    assistant_id=assistant_id,
    # 지침을 넣을 수 있지만 패스
    #instructions="Please address the user as Jane Doe. The user has a premium account."
)

run_id = "run_dCr6FNrzScZMWkvGKhIfwg6T"
# step 5: Check thre Run status
run = client.beta.threads.runs.retrieve(
    thread_id=thread_id,
    run_id=run_id,
)
print(run)
print()
print()


# step 6: Display the Assistant's Response
if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread_id
  )
  print(messages)
else:
  print(run.status)

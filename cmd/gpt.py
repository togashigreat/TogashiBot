from time import sleep
import openai
from asyncio import sleep
info = {
    "name": "gpt",
    "version": "0.0.1",
    "description": "It is a command to chat with ChatGpt-3",
    "example": "/gpt Explain Quantam Theory",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 5
  }

#Enter Your OpenAI Api key here
openai.api_key = ""




async def gpt(api, msg, threadID, thread_type, **kwargs):

    if not len(openai.api_key) == 0:
        api.sendMessage("please wait getting ans...", threadID, thread_type)
        question = " ".join(msg)
        try:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.3,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1,
            stop=[" Human:", " AI:"]
            )
            answer = response['choices'][0]['text']
            await sleep(3)
            return api.sendMessage(answer, thread_id=threadID, thread_type=thread_type)
        except Exception as e:
            return api.sendMessage(e, thread_id=threadID, thread_type=thread_type)
    else:
        return api.sendMessage("No OpenAI API key is given, please give one to use this command contact Admin", thread_id=threadID, thread_type=thread_type)

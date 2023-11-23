info = {
    "name": "say",
    "version": "1.0.0",
    "description": "It is a command to add user in a group chat.",
    "example": "/say Hello there!",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 0
}


async def say(api, msg, threadID, thread_type, **kwargs):
    msg = " ".join(msg) if len(msg) else "use /help say"
    return api.sendMessage(msg, thread_id=threadID, thread_type=thread_type)

info = {
    "name": "botid",
    "version": "1.0.0",
    "description": "get Bot id",
    "example": "/botid",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 1,
    "cooldown": 0
}
async def botid(api, author_id, threadID, thread_type, message_object, **kwargs):
    botID = f"Bot id: {api.uid}"
    api.reply(botID, message_object, threadID, thread_type)

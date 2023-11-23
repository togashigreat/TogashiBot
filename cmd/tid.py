from data import botInfo
info = {
    "name": "tid",
    "version": "0.0.1",
    "description": "Get Group Id",
    "catagory": "group",
    "example": f"{botInfo.prefix}tid",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 0
}
async def tid(api, threadID, thread_type, **kwargs):
    text = f"This group id: {threadID}"
    return api.sendMessage(text, threadID, thread_type)

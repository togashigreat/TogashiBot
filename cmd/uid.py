from data import botInfo
info = {
    "name": "uid",
    "version": "0.0.1",
    "description": "get user uid",
    "example": f"{botInfo.prefix}uid @Togashi Yuuta",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 0,
}


async def uid(api, message_object, threadID, thread_type, **kwargs):
    mentionedUser = message_object.mentions[0].thread_id
    if mentionedUser == []:
        return api.sendMessage("Please mention someone", threadID, thread_type)
    else:
        try:
            texts = f"Mentioned user id: {mentionedUser}"
            return api.sendMessage(texts, threadID, thread_type)
        except:
            return api.sendMessage("Coudn't get user id")

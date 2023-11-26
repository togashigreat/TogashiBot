from utily.utils import ban, unban 
from data import botInfo
info = {
    "name": "user",
    "version": "0.0.1",
    "description": "ban/unban users by mentioning or using uid",
    "example": f"{botInfo.prefix}user ban @Togashi Yuuta",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 2,
}


async def user_ban(api, userID, threadID, thread_type):
    ban("./cmd/data/BannedUser.json",userID)
    return api.sendMessage("Banned user succesfully", threadID, thread_type)


async def user_unban(api, userID, threadID, thread_type):
    unban("./cmd/data/BannedUser.json",userID)
    return api.sendMessage("Unbanned user succesfully", threadID, thread_type)


async def user(api, msg, message_object, threadID, thread_type, **kwargs):
    if len(msg) == 0:
        api.sendMessage("Please mention someone", threadID, thread_type)
    elif len(message_object.mentions[0].thread_id) != 0:
        userID = message_object.mentions[0].thread_id
        if msg[0] == "ban":
            await user_ban(api, userID, threadID, thread_type)
        elif msg[0] == "unban":
            await user_unban(api, userID, threadID, thread_type)
        else:
            api.sendMessage("Unknown command. use /help user", threadID, thread_type)
    else:
        userID = msg[1]
        if msg[0] == "ban":
            await user_ban(api, userID, threadID, thread_type)
        elif msg[0] == "unban":
            await user_unban(api, userID, threadID, thread_type)
        else:
            api.sendMessage("Unknown command. use /help user", threadID, thread_type)

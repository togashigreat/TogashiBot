from data import botInfo
info = {
    "name": "adduser",
    "version": "0.0.1",
    "description": "It is a command to add user in a group chat.", 
    "example": f"{botInfo.prefix}adduser 100083837299",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 0
}


async def adduser(api, msg, threadID, thread_type, **kwargs):
    try:

        api.addUsersToGroup(msg, threadID)
        txts = f"Added {msg} in the group"
        return api.sendMessage(txts, thread_id=threadID, thread_type=thread_type)

    except Exception as e:
        print(e)
        return api.sendMessage("Cant add the user in the group", thread_id=threadID, thread_type=thread_type)

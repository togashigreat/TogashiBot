from fbchat import FBchatException
from data import botInfo
info = {
    "name": "removeuser",
    "version": "1.0.0",
    "description": "It is a command to add user in a group chat. (will be updated)",
    "example": f"{botInfo.prefix}removeuser 100083837299",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 1,
    "cooldown": 0
}


async def removeuser(api, msg, threadID, thread_type, **kwargs):
    userID = msg[0]
    try:
        api.removeUserFromGroup(userID, threadID)
        txts = f"Removed {userID} from the group"
        api.sendMessage(txts, thread_id=threadID, thread_type=thread_type)

    except FBchatException as e:
        print(e)
        api.sendMessage("Cant remove the user from the group", thread_id=threadID, thread_type=thread_type)

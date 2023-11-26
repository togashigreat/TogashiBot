from togashi_fbchat import FBchatException
from data import botInfo
info = {
    "name": "removeuser",
    "version": "0.0.1",
    "description": "It is a command to remove user in a group chat",
    "example": f"{botInfo.prefix}removeuser @Togashi Yuuta",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 1,
    "cooldown": 0
}


async def removeuser(api, msg, message_object, threadID, thread_type, **kwargs):

    group_admins = api.fetchThreadInfo(threadID)[threadID].admins
    if api.uid in group_admins:

        if len(msg[0]) and not len(message_object.mentions[0].thread_id):
            try:
                api.removeUserFromGroup(msg[0], threadID)
                txts = f"Removed {msg[0]} from the group"
                api.sendMessage(txts, thread_id=threadID, thread_type=thread_type)

            except FBchatException as e:
                print(f"{botInfo.BOT} {e}")
                api.sendMessage("Cant remove the user from the group", thread_id=threadID, thread_type=thread_type)
        elif len(message_object.mentions[0].thread_id):
            try:
                user_id = message_object.mentions[0].thread_id
                api.removeUserFromGroup(user_id, threadID)
            except FBchatException as e:
                print(f"{botInfo.BOT} {e}")
                api.sendMessage("Cant remove user", threadID, thread_type)
    else:
        api.sendMessage("⚠️ Only group admins can remove members. Bot isn't a group admin yet", threadID, thread_type)

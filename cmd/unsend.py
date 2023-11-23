info = {
    "name": "unsend",
    "version": "1.0.0",
    "description": "reply to the bot message with /unsend to unsend a bot message",
    "example": "/unsend",
    "credit": "Muhammad MuQiT",
    "hasPermission": 0,
    "cooldown": 0
}

async def unsend(api, message_object, threadID, thread_type, **kwargs):
    msg_to_unsend = message_object.replied_to.uid
    try:
        api.unsend(msg_to_unsend)
    except Exception as e:
        api.reply("Can't unsend the message", message_object, threadID, thread_type)
        print(e)

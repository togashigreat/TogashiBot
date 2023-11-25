from handle.load_modules import *

info = {
    "name": "reload",
    "version": "1.0.0",
    "description": "reloads the bot's commands files (currently depricated)",
    "example": "/reload",
    "credit": "Muhammad MuQiT",
    "hasPermission": 2,
    "cooldown": 0
}

async def reload(api, threadID, thread_type, **kwargs):
    try:
        global commmands
        commmands = {}
        commmands = loadModule()
        return api.sendMessage("Commands reloaded successfully.", thread_id=threadID, thread_type=thread_type)
    except Exception as e:
        print(e)
        return api.sendMessage("Failed to reload commands.", thread_id=threadID, thread_type=thread_type)


from handler import handleCommands 
info = {
    "name": "p",
    "version": "1.0.0",
    "description": "Reloads the bot commands dynamically.",
    "example": "/p",
    "credit": "Muhammad MuQiT",
    "hasPermission": 2,
    "cooldown": 0
}
async def p(api, threadID, thread_type, **kwargs):
    txts = f"{handleCommands.commmands}"
    api.sendMessage(txts, threadID, thread_type)

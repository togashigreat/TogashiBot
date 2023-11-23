from handler import load_modules
info = {
    "name": "p",
    "version": "1.0.0",
    "description": "Reloads the bot commands dynamically.",
    "example": "/p",
    "credit": "Muhammad MuQiT",
    "hasPermission": 2,
    "cooldown": 0
}
async def p1(api, threadID, thread_type, **kwargs):
    txts = f"{load_modules.commmands}"
    api.sendMessage(txts, threadID, thread_type)

import json
from data import botInfo
info = {
    "name": "authorinfo",
    "version": "0.0.1",
    "description": "Shows information about BOT's developer",
    "example": f"{botInfo.prefix}authorinfo",
    "credit": "Muhammad MuQiT",
    "hasPermission": 0
    }

async def authorinfo(api, msg, threadID, thread_type, **kwargs):
    owner = botInfo.owner
    ownerFB = botInfo.owner_fb
    ownerAge = botInfo.owner_age
    ownerGender = botInfo.owner_gender
    owner_info = f"   🍁🍁 𝙰𝚞𝚝𝚑𝚘𝚛 𝙸𝚗𝚏𝚘 🍁🍁\n\n ☑ 𝗡𝗮𝗺𝗲: {owner}\n\n ☑ 𝗔𝗴𝗲: {ownerAge}\n\n ☑ 𝗚𝗲𝗻𝗱𝗲𝗿: {ownerGender}\n\n ☑ 𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸: {ownerFB}"
    return api.sendMessage(owner_info, thread_id=threadID, thread_type=thread_type)

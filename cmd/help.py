from os import listdir
from importlib import import_module

info = {
    "name": "help",
    "version": "1.0.5",
    "description": "use this command to get command list or to see the usage of other commands",
    "example": "/help or /help adduser",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 0
}


async def help(api, message, msg, threadID, thread_type, **kwargs):

    if len(msg) == 0:
        # Looping through each file in cmd folder
        command_list = [file.removesuffix(".py") for file in listdir("./cmd") if file.endswith(".py") and not file.startswith("__")]
        texts = ""
        for command in command_list:
            texts += f"➜ {command}\n"

        styled_cmd = f"✧༝┉˚*❋𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝙻𝚒𝚜𝚝❋*˚┉༝✧\n\n {texts} \n ❏ 𝗧𝗼𝘁𝗮𝗹 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀: {len(command_list)}"

        return api.sendMessage(styled_cmd, thread_id=threadID, thread_type=thread_type)
    else:
        module_name = f"cmd.{msg[0]}"  # getting module Name
        module = import_module(module_name)
        info = module.info
        help_box = f"◤─────•~❉❅᯽❅❉~•─────◥\n      📓 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚄𝚜𝚊𝚐𝚎 📓\n\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵\n🗂𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚗𝚊𝚖𝚎:  {info['name']}\n\n⚙️ 𝚟𝚎𝚛𝚜𝚒𝚘𝚗:  {info['version']}\n\n📖 𝚄𝚜𝚊𝚐𝚎:  {info['description']}\n\n📒 𝚎𝚡𝚊𝚖𝚙𝚕𝚎:  {info['example']}\n\n©️ 𝚊𝚞𝚝𝚑𝚘𝚛:  {info['credit']}\n\n◣──────•~❉᯽❉~•───────◢"
        return api.sendMessage(help_box, thread_id=threadID, thread_type=thread_type)

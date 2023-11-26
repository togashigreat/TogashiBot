import json
from data import botInfo
info = {
    "name": "antiout",
    "version": "1.0.0",
    "description": "if any member left gc they will be automatically re-addeed when this setting is turned on.",
    "example": f"{botInfo.prefix}antiout on",
    "credit": "Muhammad MuQiT",
    "hasPermission": 1,
    "cooldown": 0
}


def load_config():
    try:
        with open("./cmd/configs/config.json", "r") as file:
            return json.load(file)           
    except FileNotFoundError:
        default_config = {
                'ANTIOUT': False
        }
        with open("./cmd/configs/config.json", "w") as file:
            json.dump(default_config, file, indent=2)
        return default_config
def save_config(config_data):
    with open("./cmd/configs/config.json", "w") as file:
        json.dump(config_data, file, indent=2)
async def antiout(api, msg, threadID, thread_type, **kwargs):
    data = load_config()
    if msg[0] == "on" and not data["ANTIOUT"]:
        data["ANTIOUT"] = True
        save_config(data)
        api.sendMessage("🔒 Antiout feature is turned ON✅️", threadID, thread_type)
    elif msg[0] == "off" and data["ANTIOUT"]:
        data["ANTIOUT"] = False
        save_config(data)
        api.sendMessage("🔓The antiout feature turned off✅️", threadID, thread_type)
    elif msg[0] == "on" and data["ANTIOUT"]:
        api.sendMessage("Antiout is already turned on", threadID, thread_type)
    elif msg[0] == "off" and not data["ANTIOUT"]:
        api.sendMessage("Antiout is already turned off", threadID, thread_type)
    else:
        api.sendMessage("Use `antiout on/off` to on/off this feature", threadID, thread_type)



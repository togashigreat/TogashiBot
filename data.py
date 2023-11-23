from dataclasses import dataclass 
import json
@dataclass
class botInfo:
    """
    for easy loading data 
    add some more if you want like admin id
    bannedUsers etc. etc. lazy to do ;)
    """

    prefix: str
    owner: str
    owner_fb: str
    BotAdmin: list
    owner_age: int
    owner_gender: str
    BOT = "\x1B[1;38;5;210m[ Togashi ]->\x1B[0m"


def load_botinfo():
    with open("./config.json", "r") as f:
        data = json.load(f)
        botInfo.prefix = data["PREFIX"]
        botInfo.owner = data["OWNER"]
        botInfo.BotAdmin = data["BOTADMIN"]
        botInfo.owner_fb = data["FACEBOOK"]
        botInfo.owner_age = data["AGE"]
        botInfo.owner_gender = data["GENDER"]

load_botinfo()
if __name__ == "__main__":
    print("Loading bot data")

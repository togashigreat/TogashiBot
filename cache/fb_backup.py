from fbchat import Client, log
from fbchat.models import *
from colorama import Fore, Style
import json
import asyncio
import os
from importlib import import_module
from handler.handleEvents import onNicknameChange, welcome, goodbye
from handler.handleCommands import handleCommands

# Getting Coookies from json file
def getCookie():
    with open("fbstate.json", "r") as f:
        data = json.load(f)
    cookies = {}
    need_cookie = ["c_user", "datr", "sb", "fr", "xs"]
    for cookie in data:
        if cookie.get("name") in need_cookie:
            cookies[cookie["name"]] = cookie["value"]
    return cookies

session_cookies = getCookie()

BOT = f"\x1B[1;94m[ Togashi ]->\x1B[0m"

with open("./config.json", "r") as f:
    prefix = json.load(f)["PREFIX"]
    print(f"{BOT} \x1B[1;92mPrefix Loadded Succesfully!\x1B[0m")
    

commmands = {}
# Loop through files in the 'cmd' directory
print(f"{BOT} \x1B[38;5;196mLoading Commands...\x1B[0m")
def loadModule():
    for filename in os.listdir("./cmd/"):
        if filename.endswith(".py") and not filename.startswith("__"):
            commmand_name = os.path.splitext(filename)[0] # Remove the '.py' extensionmodule_name
            module_name = f"cmd.{commmand_name}" # Build the module name
            module = import_module(module_name)
            #getting hasPermission  for command handling
            perm_lvl = module.info["hasPermission"]

        # Get the function with the same name as the file and add it to the commands dictionary
            if hasattr(module, commmand_name):
                commmand_function = getattr(module, commmand_name)
                commmands[commmand_name] = (commmand_function, perm_lvl) #adding commmands in dictionary
            print(f"{BOT} \x1B[38;5;210mSuccesfully Loadded module: {commmand_name}\x1B[0m")

loadModule()


class togashi(Client):
    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None,**kwargs):

        if author_id != self.uid:
            
            if str(message_object.text).startswith(prefix):
                msg = message_object.text
                asyncio.run(handleCommands(api=self, message=msg, mid=mid, author_id=author_id, thread_id=thread_id, thread_type=thread_type, message_object=message_object, commmands=commmands))
            #else:
            #self.sendMessage("Hi", thread_id=thread_id, thread_type=thread_type)
            # else:
            #print("use !help for commmand")

    def onNicknameChange(self, mid=None, author_id=None, changed_for=None, new_nickname=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        onNicknameChange(self=self, author_id=author_id, changed_for=changed_for, new_nickname=new_nickname, thread_id=thread_id, thread_type=thread_type)

    def onPeopleAdded(self, mid=None, added_ids=None, author_id=None, thread_id=None, ts=None, msg=None):
        welcome(self=self, added_ids=added_ids, author_id=author_id, thread_id=thread_id)


    def onPersonRemoved(self, mid=None, removed_id=None, author_id=None, thread_id=None, ts=None, msg=None):
        goodbye(self=self, removed_id=removed_id, author_id=author_id, thread_id=thread_id)
    def onListening(self):
        mesg = f"{BOT} \x1B[38;5;46mis Listening...\x1B[0m"
        log.info(mesg)
         
            




bot = togashi("", "",session_cookies=session_cookies)

if bot.isLoggedIn():
    ownInfo = bot.fetchUserInfo(bot.uid)[bot.uid]
    name = ownInfo.name
    print(f"{BOT} \x1B[38;5;48mBot is logged in as {name}\x1B[0m")
bot.listen()

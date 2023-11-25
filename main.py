from togashi_fbchat import Client, log, Message, Mention
from togashi_fbchat.models import *
import json
import asyncio
from handle.handleEvents import onNicknameChange, welcome, goodbye
from utily.utils import getCookie


BOT = f"\x1B[1;38;5;210m[ Togashi ]->\x1B[0m"
print(
    """
"  \x1b[38;2;220;0;78m███╗░░░███╗██╗░░░██╗░██████╗░██╗████████╗"
"  \x1b[38;2;255;85;85m████╗░████║██║░░░██║██╔═══██╗██║╚══██╔══╝"
"  \x1b[38;2;255;153;51m██╔████╔██║██║░░░██║██║██╗██║██║░░░██║░░░"
"  \x1b[38;2;255;202;87m██║╚██╔╝██║██║░░░██║╚██████╔╝██║░░░██║░░░"
"  \x1b[38;2;255;255;112m██║░╚═╝░██║╚██████╔╝░╚═██╔═╝░██║░░░██║░░░"
"  \x1b[38;2;255;255;0m╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚═╝░░░"
"""
)
with open("./config.json", "r") as f:
    prefix = json.load(f)["PREFIX"]
    print(f"{BOT} \x1B[1;92mPrefix Loadded Succesfully!\x1B[0m")

from handle.handleMessage import handleMessage
class togashi(Client):
    prefix = prefix

    def onListening(self):
        mesg = f"{BOT} \x1B[38;5;48mis Online.\x1B[0m"
        log.info(mesg)
        


    """All listened Messages managed here"""

    def onMessage(
        self,
        mid=None,
        author_id=None,
        message=None,
        message_object=None,
        thread_id=None,
        thread_type=ThreadType.USER,
        ts=None,
        msg=None,
        **kwargs,
    ):
       handleMessage(
            self,
            mid,
            message,
            message_object,
            author_id,
            thread_id,
            thread_type,
            msg,
            ts,
        )   

    """ custom reply method for essy reply """

    def reply(
        self,
        message,
        message_object,
        thread_id,
        thread_type,
        mentions=None,
        reactions=None,
    ):
        if mentions != None:
            name = self.fetchUserInfo(mentions)[mentions].name
            message = f"@{name} {message}"
            mentions = [Mention(thread_id=mentions, length=len(name) + 1)]
        self.send(
            Message(text=message, reply_to_id=message_object.uid, mentions=mentions),
            thread_id,
            thread_type,
        )
        
    """ All events starts here """

    def onNicknameChange(
        self,
        mid=None,
        author_id=None,
        changed_for=None,
        new_nickname=None,
        thread_id=None,
        thread_type=ThreadType.USER,
        **kwargs,
    ):
        onNicknameChange(
            self=self,
            author_id=author_id,
            changed_for=changed_for,
            new_nickname=new_nickname,
            thread_id=thread_id,
            thread_type=thread_type,
        )

    def onPeopleAdded(
        self,
        mid=None,
        added_ids=None,
        author_id=None,
        thread_id=None,
        ts=None,
        msg=None,
    ):
        welcome(
            self=self, added_ids=added_ids, author_id=author_id, thread_id=thread_id
        )

    def onPersonRemoved(
        self,
        mid=None,
        removed_id=None,
        author_id=None,
        thread_id=None,
        ts=None,
        msg=None,
    ):
        asyncio.run(
            goodbye(
                self=self,
                removed_id=removed_id,
                author_id=author_id,
                thread_id=thread_id,
            )
        )

if __name__ == "__main__":
    session_cookies = getCookie("fbstate.json")
    bot_togashi = togashi("", "", session_cookies=session_cookies)
    if bot_togashi.isLoggedIn():
        ownInfo = bot_togashi.fetchUserInfo(bot_togashi.uid)[bot_togashi.uid]
        name = ownInfo.name
        print(f"{BOT} \x1B[1;38;5;219mBot is logged in as {name}\x1B[0m")
    bot_togashi.listen()

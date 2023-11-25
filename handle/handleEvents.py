from togashi_fbchat import Message, Mention
import json
from cmd.events import antiout
def onNicknameChange(self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs):
    author = self.fetchUserInfo(author_id)[author_id]
    newName_user = self.fetchUserInfo(changed_for)[changed_for]
    texts = f"{author.name} changed {newName_user.name}'s name to {new_nickname}"
    self.send(Message(text=texts), thread_id=thread_id, thread_type=thread_type)


def welcome(self, added_ids, author_id, thread_id):

    thread = self.fetchThreadInfo(thread_id)[thread_id]
    thread_type = thread.type
    thread_name = thread.name
    if self.uid not in added_ids:
        for id in added_ids:
            user = self.fetchUserInfo(id)[id]
            welcome_msg = f"@{user.name}, Welcome 🎉🎊 to the {thread_name} GC, You are the no.{len(thread.participants)} member of the GC. Have a nice time here 🍁"
            self.sendLocalImage("./src/welcome1.gif", message=Message(text=welcome_msg, mentions=[Mention(thread_id=id, length=len(user.name)+1)]), thread_id=thread_id, thread_type=thread_type)
    else:
        return self.send(Message(text="Hello! This is BoT Izumi your papa"), thread_id=thread_id, thread_type=thread_type)


async def goodbye(self, author_id, removed_id, thread_id, **kwargs):
    if removed_id != self.uid:
        with open("./cmd/configs/config.json", "r") as f:
            isActivated = json.load(f)["ANTIOUT"]
        if isActivated:
           await antiout.antiout(api=self, author_id=author_id, removed_id=removed_id, thread_id=thread_id)
        thread = self.fetchThreadInfo(thread_id)[thread_id]
        user = self.fetchUserInfo(removed_id)[removed_id]
        thread_type = thread.type
        try:
            goodbye_msg = f"Goood bye {user.name}! Hope we will see you in {thread.name} GC again "
            return self.send(Message(text=goodbye_msg), thread_id=thread_id, thread_type=thread_type)
        except Exception as e:
            return self.send(Message(text=e), thread_id=thread_id, thread_type=thread_type)

         


import json
import asyncio
from handle.handleCommands import handleCommands
from data import botInfo
"""
Getting Banned Users and Groups id and Approved users and Groups id, the bot will only response to approved ids.
"""
def getUsersData():
    with open("./cmd/data/BannedUser.json", "r") as file:
        bannedUser = json.load(file)
    with open("./cmd/data/ApprovedUser.json", "r") as file:
        approvedUser = json.load(file)
    with open("./cmd/data/BannedThread.json", "r") as file:
        bannedThread = json.load(file)
    with open("./cmd/data/ApprovedThread.json", "r") as file:
        approvedThread = json.load(file)
    return bannedUser, approvedUser, bannedThread, approvedThread
#Loading prefix from config.json
adminIDs = botInfo.BotAdmin
prefix = botInfo.prefix

""" Getting Reason for ban """

def getBanReason():
    with open("./cmd/data/reasonForUserBan.json", "r") as f:
        data = json.load(f)
        return data

def NoPrefixMessage():
    pass
print(f"{botInfo.BOT} \x1b[1;0mloading message handler......\x1b[0m")

def handleMessage(
    api, mid, message, message_object, author_id, thread_id, thread_type, msg, ts
):
    bannedUsers, approvedUsers, bannedThreads, approvedThreads = getUsersData()
    if api.uid != author_id:
        if message.startswith(prefix):
            if author_id in adminIDs:
                asyncio.run(handleCommands(
                        api,
                        mid,
                        author_id,
                        message,
                        thread_id,
                        thread_type,
                        message_object,
                        ts,
                    ))
                
            elif author_id not in bannedUsers and author_id in approvedUsers:
                asyncio.run(handleCommands(
                        api,
                        mid,
                        author_id,
                        message,
                        thread_id,
                        thread_type,
                        message_object,
                        ts,
                    ))
                
            elif author_id in bannedUsers:
                data = getBanReason()
                if author_id in data:
                    buid_msg = f"You are banned fron using the bot.\nReason: {data[author_id]['reason']}\nDate: {data[author_id]['date']}"
                    api.sendMessage(buid_msg, thread_id, thread_type)
                api.sendMessage(
                    "You are banned from using commands.", thread_id, thread_type
                )
            else:
                api.sendMessage(
                    "Your thread is not approved yet. Ask admin for approval to use the bot."
                )
        else:
            if thread_id in approvedThreads and author_id in approvedUsers:
                return NoPrefixMessage()


if __name__ == "__main__":
    print("\x1b[1;38;5;120m/////Loadded Message Handler\x1b[0m")

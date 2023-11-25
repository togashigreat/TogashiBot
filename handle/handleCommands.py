from handle import load_modules
from data import botInfo


prefix = botInfo.prefix
BOTADMINS = botInfo.BotAdmin



""" Loading all files from cmd directory """

print(f"{botInfo.BOT} \x1B[38;5;130mLoading Commands......\x1B[0m")



async def handleCommands(
    api, mid, author_id, message, thread_id, thread_type, message_object, ts
):
    #global commmands
    commmands: dict = load_modules.commmands
    text = message.split(" ")
    """ removing prefix & getting Command """
    command = text[0].removeprefix(prefix)

    commandUser = api.fetchUserInfo(author_id)[author_id]
    thread = api.fetchThreadInfo(thread_id)[thread_id]

    no_perm_msg = (
        f"{commandUser.name}, You don't have the permission to use this command"
    )

    if command in commmands:
        """
        Checking command permission level

        level 2: only Bot admin can use commands.
        level 1: only group admins and bot admins can use the command.
        level 0: everyone can use the command.

        """
        if commmands[command][1] == 2:
            if author_id in BOTADMINS:
                return await commmands[command][0](
                    api=api,
                    message=message,
                    msg=text[1:],
                    threadID=thread_id,
                    thread_type=thread_type,
                    message_object=message_object,
                    author_id=author_id,
                    mid=mid,
                    ts=ts,
                )
            else:
                api.sendMessage(
                    no_perm_msg, thread_id=thread_id, thread_type=thread_type
                )
        elif commmands[command][1] == 1:
            if author_id in thread.admins or author_id in BOTADMINS:
                return await commmands[command][0](
                    api=api,
                    message=message,
                    msg=text[1:],
                    threadID=thread_id,
                    thread_type=thread_type,
                    message_object=message_object,
                    author_id=author_id,
                    mid=mid,
                    ts=ts,
                )
            else:
                api.sendMessage(
                    no_perm_msg, thread_id=thread_id, thread_type=thread_type
                )
        elif commmands[command][1] == 0:
            return await commmands[command][0](
                api=api,
                message=message,
                msg=text[1:],
                threadID=thread_id,
                thread_type=thread_type,
                message_object=message_object,
                author_id=author_id,
                mid=mid,
                ts=ts,
            )
        else:
            api.sendMessage(
                "Unknown permission level!Please check command permission level or notify bot Admin"
            )

    else:
        return api.sendMessage(
            "Commnad not fouund", thread_id=thread_id, thread_type=thread_type
        )


if __name__ == "__main__":
    print("\x1b[1;91mhandle Command Loadded Succesfully\x1b[0m")

info = {
    "name": "topuser",
    "version": "1.0.0",
    "description": "get list of top cahtter in gc",
    "example": "/topuser",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 5
}
async def topuser(api, threadID, thread_type, message_object, **kwargs):
    api.reply("⋘ 🔍 𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡... ⋙", message_object, threadID, thread_type)

    groupMembers = api.fetchThreadInfo(threadID)[threadID].participants
    membersMessages = {member: 0 for member in groupMembers}
    threadMesaages = api.fetchThreadMessages(threadID, 1000)


    """ Counting messages of each member in recent 1000 messge """
    for messsage in threadMesaages:
        authorID = messsage.author
        if authorID != None and messsage.author in membersMessages:
            membersMessages[messsage.author] += 1


    """ getting top 10 most chatted member """
    TopMsgers = dict(sorted(membersMessages.items(), key=lambda item: item[1], reverse=True)[:10])


    print(TopMsgers)
    #styling text
    top = f"╔⏤⏤⏤⏤⏤ ✉ ⏤⏤⏤⏤⏤╗\n{' '*12}𝚃𝚘𝚙 𝙲𝚑𝚊𝚝𝚝𝚎𝚛\n╚⏤⏤⏤⏤⏤ ✉ ⏤⏤⏤⏤⏤╝\n"
    winner = next(iter(TopMsgers))
    freeloader = api.fetchUserInfo(winner)[winner].name

    for user, countedMsg in TopMsgers.items():
        UserName = api.fetchUserInfo(user)[user].name
        top += f"● {UserName} -- {countedMsg} messages\n"


    box = f"{top} \n\nToday's life less person: {freeloader} with {TopMsgers[winner]} messages"
    api.sendMessage(box, threadID, thread_type)

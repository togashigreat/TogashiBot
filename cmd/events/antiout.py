async def antiout(api, author_id, removed_id, thread_id):
    thread = api.fetchThreadInfo(thread_id)[thread_id]
    thread_type = thread.type
    if author_id not in thread.admins:
        try:
            api.addUsersToGroup(removed_id, thread_id)
            api.sendMessage("[ Antiout ]: successfully Re-added user in the group", thread_id, thread_type)
        except Exception as e:
            print(e)
            api.sendMessage("[ Antiout ]: Can't add user in the group", thread_id, thread_type)


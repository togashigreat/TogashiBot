from utily.utils import find_uid
import re
from data import botInfo
info = {
    "name": "fbid",
    "version": "0.0.1",
    "description": "get fb uid by profile link",
    "example": f"{botInfo.prefix}fbid link_of_the_profile",
    "credit": "𝙼𝚞𝚑𝚊𝚖𝚖𝚊𝚍 𝙼𝚞𝚀𝚒𝚃",
    "hasPermission": 0,
    "cooldown": 5
}


def is_facebook_profile_url(url):
    # Regular expression pattern for a basic Facebook profile URL
    pattern = r'https?://(?:www\.)?facebook\.com/[a-zA-Z0-9.]+'
    # Check if the URL matches the pattern
    return bool(re.match(pattern, url))

async def fbid(api, msg, threadID, thread_type, message_object, **kwargs):
    isUrl = is_facebook_profile_url(msg[0])
    if isUrl:
        try:
            uid = await find_uid(msg[0])
            api.reply(uid, message_object, threadID, thread_type)
        except Exception as e:
            raise e

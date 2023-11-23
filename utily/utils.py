import json
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

""" BAN USER/THREAD ID """
def ban(file_path: str, user_id: str):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        data = []
    if user_id not in data:
        data.append(user_id)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)
    else:
        print("Thread is already in banned list")


""" UNBAN USER/THREAD ID """

def unban(file_path: str, user_id: str):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

    if user_id in data:
        data.remove(user_id)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Thread ID {user_id} removed successfully.")
    else:
        print(f"Thread ID {user_id} not found in the JSON file.")


""" FIND USER ID """

async def find_uid(link):
    try:
        async with httpx.AsyncClient() as client:
            # Attempt to get UID using the first method
            response = await client.post(
                'https://seomagnifier.com/fbid',
                data={
                    'facebook': '1',
                    'sitelink': link
                },
                headers={
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': 'PHPSESSID=0d8feddd151431cf35ccb0522b056dc6'
                }
            )
            id = response.text.strip()

            # Try another method if the first one fails
            if not id.isdigit():
                html = await client.get(link)
                soup = BeautifulSoup(html.text, 'html.parser')
                el = soup.find('meta', property='al:android:url')

                if not el:
                    raise ValueError('UID not found')

                # Extract UID from the URL
                uid_url = el.get('content')
                uid = parse_qs(urlparse(uid_url).query).get('id', [None])[0]

                if not uid:
                    raise ValueError('UID not found')

                return uid

            return id

    except Exception as e:
        raise ValueError('An unexpected error occurred. Please try again.')

if __name__ == "__main__":
    print("Utils file is being used")

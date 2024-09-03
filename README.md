# TogashiBot
A simple messenger Bot using Python fbchat api.
## Usage
First, git clone this repo

```bash
git clone https://github.com/togashigreat/TogashiBot.git
```

**Install the requirements using poetry**

```bash
poetry install
```
**or**
```bash
pip3 install -r requirements.txt
```

Use c3c fbstate or cookie-editor or developer tools to get your facebook account cookies and put it in fbstate.json
now, you can start using the bot it by running


```bash
python3 main.py
```

The bot will be updated It's just the test version.
You can configure bot prefix and other stuff in config.json

### 🗂Command
You can make command very easily. if you know a little bit python.
you will have to define every function with async and the function musthave the same name as the command file As an example:

````python
#filename  sayhi.py

async def sayhi(api, message_object, threadID, thread_type, author_id, **kwargs):
    return api.reply("Hello", message_object, threadID, thread_type, author_id)

    #author_id is the user who used the command sayhi
    #passing it as the 4th argument will mention the member
````
To access everything like the message sender ID, threadID, bot id, the message context etc. you can access these easily

`api` = same as how you use in mirai

`message` = the message sent by the command user

`msg` = the message sent by the the command user but without prefix and comand name

        example:       
               user sent message in groupchat "/user ban @Togashi Yuuta"
              `msg` would be "ban @Togashi Yuuta"
               and `message` would "/user ban @Togashi Yuuta"

`author_id` = the command user id

`message_object` = the command user's message. including messageID, author id, replied to etc. you
                you can print(message_object) what else attributes it has. you can access them using
                `message_object.author`, `message_object.text`, `message_object.uid` (this is messageID noy user id)
                
`threadID` = the group id or user id

`thread_type` `= thread type can be User or Group


Add a Info dictionary
```
info = {

"name": "command name"

"version": "command version"

"usage": "explain how to use"

"example": "explain how to use"

"hasPermission": "0,1,2 any of these three number"

"cooldown": "no functionality added for cooldown yet"
}
```
dictionary as well which is called object in Javascript.
you can look at the other command files to see how the commands are made.

In, mirai or goatbot you send Message using

`api.sendMessage("Hellow", threadID, messageID)`


in TogashiBot you can do that using:

`api.sendMessage("Hellow", threadID, thread_type)`

or

`api.send(Message(text="Hellow"), threadID, thread_type)`

#here thread_type is to define wether It's a group chat or a private chat.

api.sendMessage only sends message but doesn't reply to any message
to reply a message use:

`api.reply("Hellow", message_object, threadID, thread_type)`

if you want to mention someone add the `author_id` after thread_id in api.reply
Get bot uid by using `api.uid`
**Its just the test version of TogashiBot. I'm re modeling it to make it more object oriented than functional.**


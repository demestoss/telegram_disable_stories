import os
from telethon import TelegramClient, functions, types
from dotenv import load_dotenv

load_dotenv()

api_id = os.environ.get('TELEGRAM_API_ID')
api_hash = os.environ.get('TELEGRAM_API_HASH')

if api_id == None or api_hash == None:
    raise ValueError('Please set TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables')

client = TelegramClient('anon', api_id, api_hash)

async def main():
    # me = await client.get_me()
    # print(me.stringify())

    contacts = await client(functions.contacts.GetContactIDsRequest(
        hash=-12398745604826
    ))

    for contactId in [a for a in contacts if a not in [0]]:
        res = await client(functions.contacts.ToggleStoriesHiddenRequest(id=contactId, hidden=True))
        print(contactId, res)

    # print(res)
    # result = await client(functions.stories.ToggleAllStoriesHiddenRequest(
    #     hidden=False
    # ))
    # print(result)

with client:
    client.loop.run_until_complete(main())
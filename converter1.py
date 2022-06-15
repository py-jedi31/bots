from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import UseCurrentSession
import asyncio
import json

async def main():

    tdataFolder = r"C:\Users\Admin\AppData\Roaming\Telegram Desktop\tdata"
    tdesk = TDesktop(tdataFolder)

    client = await tdesk.ToTelethon("newSession.session", UseCurrentSession)

    await client.connect()
    sessions = await client.GetSessions()
    await client.PrintSessions()

    jsonString = json.dumps(sessions.to_json())
    jsonString = jsonString.replace("\\", "")
    jsonString = jsonString.replace("\"", "\'")
    with open("data.json", "w") as file:
        json.dump(jsonString, file)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
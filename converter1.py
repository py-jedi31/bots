from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, CreateNewSession, UseCurrentSession
import asyncio
import json

async def main():
    # Load TDesktop client from tdata folder
    tdataFolder = r"C:\Users\Admin\AppData\Roaming\Telegram Desktop\tdata"
    tdesk = TDesktop(tdataFolder)

    # Convert TDesktop session to telethon client
    # CreateNewSession flag will use the current existing session to
    # authorize the new client by `Login via QR code`.
    client = await tdesk.ToTelethon("newSession.session", UseCurrentSession)

    # Although Telegram Desktop doesn't let you authorize other
    # sessions via QR Code (or it doesn't have that feature),
    # it is still available across all platforms (APIs).

    # Connect and print all logged in devices
    await client.connect()
    sessions = await client.GetSessions()
    await client.PrintSessions()
    # for session in sessions[0]:
    #     print(session)
    jsonString = json.dumps(sessions.to_json())
    jsonString = jsonString.replace("\\", "")
    jsonString = jsonString.replace("\"", "\'")
    with open("data.json", "w") as file:
        json.dump(jsonString, file)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
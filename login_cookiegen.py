import asyncio
from twikit import Client

client = Client("ja-JP")

async def login_and_save_cookies():
    await client.login(auth_info_1="",
        password="")
    client.save_cookies("cookies.json")

if __name__ == "__main__":
    asyncio.run(login_and_save_cookies())

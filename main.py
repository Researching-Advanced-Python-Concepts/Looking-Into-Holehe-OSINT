import trio
import httpx
import os

from dotenv import load_dotenv
from holehe.modules.social_media.snapchat import snapchat
# from holehe.modules.social_media.twitter import twitter
from holehe.modules.social_media.instagram import instagram
from holehe.modules.software.lastpass import lastpass
from holehe.modules.programing.replit import replit

load_dotenv()

async def main():
    email = os.environ.get("EMAIL")
    out = []
    client = httpx.AsyncClient()
    
    # await snapchat(email, client, out)
    # await lastpass(email, client, out)
    await replit(email, client, out)
    # await instagram(email, client, out)
    # await twitter(email, client, out)
    
    print(out)
    # close transport and proxies
    await client.aclose()

trio.run(main)

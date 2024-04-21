import logging
import os
import requests
from pyrogram import Client, filters


@Client.on_message(filters.command('repo'))
async def git(Kashmira, message):
    pablo = await message.reply_text("`Processing...`")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("No input found")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("File not found")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
<b>Name :</b> <i>{qw.get("name")}</i>

<b>Full Name :</b> <i>{qw.get("full_name")}</i>

<b>Link :</b> {qw.get("html_url")}

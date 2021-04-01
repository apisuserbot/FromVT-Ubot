# port by @vckyouubitch


import asyncio
import os
import random

from telethon import functions

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.autopic(?: |$)(.*)")
async def autopic(e):
    search = e.pattern_match.group(1)
    if not search:
        return await event.edit(get_string("autopic_1"))
    clls = returnpage(search)
    if len(clls) == 0:
        return await event.edit(get_string("autopic_2").format(search))
    if not len(clls) == 1:
        num = random.randrange(0, len(clls) - 1)
    else:
        num = 0
    page = clls[num]
    title = page["title"]
    await event.edit(get_string("autopic_3").format(title))
    udB.set("AUTOPIC", "True")
    while True:
        ge = udB.get("AUTOPIC")
        if not ge == "True":
            return
        animepp(page["href"])
        file = await bot.upload_file("autopic.jpg")
        await bot(functions.photos.UploadProfilePhotoRequest(file))
        os.remove("autopic.jpg")
        await asyncio.sleep(1100)


@register(outgoing=True, pattern="^.stoppic(?: |$)(.*)")
async def stoppo(ult):
    gt = udB.get("AUTOPIC")
    if not gt == "True":
        return await event.edit(ult, "`AUTOPIC was not in used !!`")
    udB.set("AUTOPIC", "None")
    await event.edit(ult, "`AUTOPIC Stopped !!`")


CMD_HELP.update({"autopic": "`.autopic` : `.stoppic`\
    \nPenjelasan: `.autopic : Auto Pic | .stoppic : Stop Auto Pic`"})

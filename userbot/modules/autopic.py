# wahahaha
# port by @Vckyouuu

import asyncio
import os
import random

from telethon import functions
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern="^.apic ?(.*)")
async def autopic(e):
    search = e.pattern_match.group(1)
    if not search:
        return await e.edit(get_string("autopic_1"))
    clls = returnpage(search)
    if len(clls) == 0:
        return await e.edit(get_string("autopic_2").format(search))
    if not len(clls) == 1:
        num = random.randrange(0, len(clls) - 1)
    else:
        num = 0
    page = clls[num]
    title = page["title"]
    await e.edit(get_string("autopic_3").format(title))
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


@register(outgoing=True, pattern="^.spic ?(.*)")
async def stoppo(e):
    gt = udB.get("AUTOPIC")
    if not gt == "True":
        return await e.edit("`AUTOPIC was not in used !!`")
    udB.set("AUTOPIC", "None")
    await e.edit("`AUTOPIC Stopped !!`")

# Kalian semua kontol

CMD_HELP.update(
    {
        "autopic": ">`.apic`"
        "\nUsage: AutoPic"
        "\n>`.spic``"
        "\nUsage: `Stop AutoPic`"
    }
)

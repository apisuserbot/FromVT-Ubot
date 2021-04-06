# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.zping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⌖ ᴘɪɴɢ!**\n"
                    f"➥ **ᴘɪɴɢ   :** "
                    f"`%sms` \n"
                    f"• **Uptime :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**▁**")
    await pong.edit("**▂▁**")
    await pong.edit("**▃▂▁**")
    await pong.edit("**▄▃▂▁**")
    await pong.edit("**▅▄▃▂▁**")
    await pong.edit("**▇▅▄▃▂▁**")
    await pong.edit("**▇▆▅▄▃▂▁**")
    await pong.edit("**█▇▆▅▄▃▂▁**")
    await pong.edit("**PING!!!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡ 𝙁𝙍𝙊𝙈-𝙑𝙏 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⚡**\n"
                    f"**┉┈────┉┈──┈┉────┈┉**\n"
                    f"**▸ ᴘᴏɴɢ    :** "
                    f"`%sms` \n"
                    f"**▸ ᴏɴʟɪɴᴇ  :** "
                    f"`{uptime}` \n"
                    f"**▸ ᴏᴡɴᴇʀ  :** `{ALIVE_NAME}`" % (duration))


# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**10% █▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡𝗙𝗥𝗢𝗠-𝗩𝗧 𝗣𝗜𝗡𝗚⚡** \n"
                    f"╭┈──────────── \n"
                    f"**▸ ᴘᴏɴɢ     :**"
                    f" %sms \n"
                    f"**▸ ᴏɴʟɪɴᴇ  :** "
                    f"`{uptime}` \n"
                    f"**▸ ᴏᴡɴᴇʀ  :**"
                    f" {ALIVE_NAME} \n"
                    f"╰┈─────────" % (duration))


@register(outgoing=True, pattern="^.suing$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`                       /¯ )")
    await pong.edit("`                       /¯ )\n                       /¯  /")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit("`                       /¯ )\n                       /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡ 𝙁𝙍𝙊𝙈-𝙑𝙏 𝙋𝙄𝙉𝙂⚡**\n"
                    f"**┉┈───┉┈─┈┉───┈┉**\n"
                    f"**▸ ᴘᴏɴɢ     :** "
                    f"`%sms` \n"
                    f"**▸ ᴏɴʟɪɴᴇ  :** "
                    f"`{uptime}` \n"
                    f"**▸ ᴏᴡɴᴇʀ  :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.from$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡ 𝙁𝙍𝙊𝙈-𝙑𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" ⚡𝙍𝙊𝙈-𝙑𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁⚡𝙊𝙈-𝙑𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍⚡𝙈-𝙑𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊⚡-𝙑𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈⚡𝙑𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈-⚡𝙏 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈-𝙑⚡ 𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈-𝙑𝙏⚡𝘽𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈-𝙑𝙏 ⚡𝙊𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈-𝙑𝙏 𝘽⚡𝙏**!**")
    await pong.edit(" 𝙁𝙍𝙊𝙈-𝙑𝙏 𝘽𝙊⚡!")
    await pong.edit(" 𝙁𝙍𝙊𝙈-𝙑𝙏 𝘽𝙊𝙏⚡")
    await pong.edit("**𝙁𝙍𝙊𝙈-𝙑𝙏 𝙋𝙄𝙉𝙂!⚡**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡𝙁𝙍𝙊𝙈-𝙑𝙏 𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡** \n"
                    f"┉┈────┉┈─┈┉────┈┉\n"
                    f"➥ **Sinyal  :**"
                    f" %sms \n"
                    f"➥ **Owner :**"
                    f" {ALIVE_NAME} \n" % (duration))


@register(outgoing=True, pattern="^.spong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁𓂺**")
    await pong.edit("**▁▁▁▁▁▁▁▁▁▁▁▁▁▁𓂺▁**")
    await pong.edit("**▁▁▁▁▁▁▁▁▁▁▁▁▁𓂺▁▁**")
    await pong.edit("**▁▁▁▁▁▁▁▁▁▁▁▁𓂺▁▁▁**")
    await pong.edit("**▁▁▁▁▁▁▁▁▁▁▁𓂺▁▁▁▁**")
    await pong.edit("**▁▁▁▁▁▁▁▁▁▁𓂺▁▁▁▁▁**")
    await pong.edit("**▁▁▁▁▁▁▁▁▁𓂺▁▁▁▁▁▁**")
    await pong.edit("**▁▁▁▁▁▁▁▁𓂺▁▁▁▁▁▁▁**")
    await pong.edit("**▁▁▁▁▁▁▁𓂺▁▁▁▁▁▁▁▁**")
    await pong.edit("**▁▁▁▁▁▁𓂺▁▁▁▁▁▁▁▁▁**")
    await pong.edit("**▁▁▁▁▁𓂺▁▁▁▁▁▁▁▁▁▁**")
    await pong.edit("**▁▁▁▁𓂺▁▁▁▁▁▁▁▁▁▁▁**")
    await pong.edit("**▁▁▁𓂺▁▁▁▁▁▁▁▁▁▁▁▁**")
    await pong.edit("**▁▁𓂺▁▁▁▁▁▁▁▁▁▁▁▁▁**")
    await pong.edit("**▁𓂺▁▁▁▁▁▁▁▁▁▁▁▁▁▁**")
    await pong.edit("**𓂺▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁**")
    await pong.edit("⚡")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**═══════════════**\n"
                    f"     **⚠️ 𝙁 𝙍 𝙊 𝙈 - 𝙑 𝙏 ⚠️**\n"
                    f"**═══════════════**\n"
                    f"**➾ ᴘɪɴɢ**   : "
                    f"`%sms` \n"
                    f"**➾ ᴏɴʟɪɴᴇ** : "
                    f"`{uptime}` \n"
                    f"**➾ ᴏᴡɴᴇʀ** : `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"⚠️ 𝙁𝙍𝙊𝙈-𝙑𝙏 ⚠️\n"
                    f"**▬▬▬▬▬▬▬▬**\n"
                    f"**• 𝚂𝚒𝚗𝚢𝚊𝚕  :** "
                    f"`%sms` \n"
                    f"**• 𝙾𝚗𝚕𝚒𝚗𝚎  :** "
                    f"`{uptime}` \n"
                    f"**• 𝙾𝚠𝚗𝚎𝚛   :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "✺ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✺ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✺ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✺ **Ping:** "
                   f"`{result['ping']}` \n"
                   "✺ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✺ **BOT:** `ERROR404NOTFOUND BOT`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`ᴘᴏɴɢ!.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("🦚 **ᴘᴏɴɢ!**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping` ; `.spong` ; `.from` ; `.xping` ; `.sping`\
    \nUsage: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nUsage: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nUsage: sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "`.sinyal`\
    \nPenjelasan: sama seperti `.ping`."
     })

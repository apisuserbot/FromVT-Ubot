# BASED FROM ULTROID PORTED FOR FromVT-Userbot BY ALVIN / @LIUALVINAS
# THANKS FOR TEAMULTROID
# DONT REMOVE THIS
# PIKI GANS
# @LORDUSERBOT_GROUP

from telethon import events
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio
# piki


@register(outgoing=True, pattern="^.tempmail ?(.*)")
async def _(event):
    chat = "@TempMailBot"
    fromvt = await event.edit("Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            fromvtuserbot = ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fromvt.edit("Mohon Unblock @TempMailBot !!!")
            return
        await event.edit(f"**TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK MELIHAT VERIFIKASI]({fromvtuserbot})")


# Piki Gantengg

CMD_HELP.update({"tempmail": "**Modules:** __Temp Mail__\n\n**Perintah:** `.tempmail`"
                 "\n**Penjelasan:** Mendapatkan Email Gratis Dari Temp Mail"})

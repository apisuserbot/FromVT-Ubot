# Port By: Piki Ganteng

from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from plugins.stickertools import deEmojify
import random

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.net (.*)")
async def nope(fromvt):
    vt = fromvt.pattern_match.group(1)
    a = await event.edit("`Processing...`")
    if not vt:
        if fromvt.is_reply:
            (await fromvt.get_reply_message()).message
        else:
            return await event.edit("`Sir please give some query to search and download it for you..!`",
                                    )
    sticcers = await bot.inline_query("Lybot", f"{(deEmojify(vt))}")
    try:
        await sticcers[0].click(
            fromvt.chat_id,
            reply_to=doit.reply_to_msg_id,
            silent=True if doit.is_reply else False,
            hide_via=True,
        )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Boss ! I cant use inline things here...`")


CMD_HELP.update(
    {
        "net": ">`.net <Judul Lagu>`"
        "\nUsage: Mendownload Music"
    }
)

# Port By: Piki Ganteng

from telethon.errors import ChatSendInlineForbiddenError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.net (.*)")
async def nope(event):
    vt = event.pattern_match.group(1)
    await event.edit("`Processing...`")
    if not vt:
        if event.is_reply:
            (await event.get_reply_message()).message
        else:
            return await event.edit("`Sir please give some query to search and download it for you..!`",
                                    )
    fromvt = await event.client.inline_query("Lybot", f"{(deEmojify(vt))}")
    try:
        await fromvt[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            silent=True if event.is_reply else False,
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

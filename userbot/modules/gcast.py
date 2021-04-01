# frm Ultroid
# port by Koala @manusiarakitann
# @LordUserbot_Group
# Alvin Ganteng

from userbot.events import register
from userbot import CMD_HELP, bot
# Alvin Ganteng


@register(outgoing=True, pattern="^.rgc (.*)")
async def broadcast_remover(event):
    chat_id = event.pattern_match.group(1)
    await event.edit(event, get_string("com_1"))
    if chat_id == "all":
        await event.edit("`Menghapus...`")
        udB.delete("BROADCAST")
        await event.edit("Basis data dihapus.")
        return
    if is_channel_added(chat_id):
        rem_channel(chat_id)
        await event.edit("Dihapus dari database")
        await asyncio.sleep(3)
        await event.delete()
    elif is_channel_added(event.chat_id):
        rem_channel(event.chat_id)
        await event.edit("Dihapus dari database")
        await asyncio.sleep(3)
        await event.delete()
    elif not is_channel_added(event.chat_id):
        await event.edit("Channel sudah dihapus dari database. ")
        await asyncio.sleep(3)
        await event.delete()


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Lord, Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`📢 Sedang Mengirim Pesan Secara Global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")

# Alvin Ganteng
CMD_HELP.update(
    {
        "gcast": ">`.gcast <pesan>`\
    \nPenjelasan: Global Broadcast mengirim pesan ke Seluruh Grup yang Anda Masuki."
        "\n\n>`.rgcast`"
        "\nUsage: Menghapus Seluruh Broadcast Yang Anda Kirim."


    }
)

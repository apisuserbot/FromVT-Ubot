# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from userbot.functions.pmpermit_db import, bot
from telethon import events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.utils import get_display_name

from userbot import CMD_HELP, bot
from userbot.events import register

# Piki Gantengggg
COUNT_PM = {}
LASTMSG = {}
if Redis("PMPIC"):
    PMPIC = Redis("PMPIC")
else:
    PMPIC = "https://telegra.ph/file/40f9e0b2a50f68bd46e93.jpg"

UND = get_string("pmperm_1")

if not Redis("PM_TEXT"):
    UNAPPROVED_MSG = """
**PMSecurity of {ON}!**

{UND}

You have {warn}/{twarn} warnings!"""
else:
    UNAPPROVED_MSG = (
        """
**PMSecurity of {ON}!**"""
        f"""

{Redis("PM_TEXT")}
"""
        """

{UND}

You have {warn}/{twarn} warnings!"""
    )

UNS = get_string("pmperm_2")
# 1
if Redis("PMWARNS"):
    try:
        WARNS = int(Redis("PMWARNS"))
    except BaseException:
        WARNS = 4
else:
    WARNS = 4
NO_REPLY = get_string("pmperm_3")
PMCMDS = [
    f"{hndlr}a",
    f"{hndlr}approve",
    f"{hndlr}da",
    f"{hndlr}disapprove",
    f"{hndlr}block",
    f"{hndlr}unblock",
]
# =================================================================


@bot.on(events.NewMessage(incoming=True, func=lambda event: event.is_private))
async def permitpm(event):
    user = await event.get_chat()
    if user.bot or user.is_self:
        return
    if Redis("PMLOG") == "True":
        pl = udB.get("PMLOGGROUP")
        if pl is not None:
            return await event.forward_to(pl)
        await event.forward_to(Var.LOG_CHANNEL)


sett = Redis("PMSETTING")
if sett is None:
    sett = True
if sett == "True" and sett != "False":

    @bot.on(events.NewMessage(outgoing=True,
                              func=lambda event: event.is_private))
    async def autoappr(event):
        miss = await event.get_chat()
        if miss.bot or miss.is_self or miss.verified or Redis(
                "AUTOAPPROVE") != "True":
            return
        if str(miss.id) in DEVLIST:
            return
        mssg = event.text
        if mssg.startswith(HNDLR):  # do not approve if outgoing is a command.
            return
        if not is_approved(event.chat_id):
            approve_user(event.chat_id)
            async for message in event.client.iter_messages(event.chat_id, search=UND):
                await message.delete()
            async for message in event.client.iter_messages(event.chat_id, search=UNS):
                await message.delete()
            if Var.LOG_CHANNEL:
                name = await event.client.get_entity(e.chat_id)
                name0 = str(name.first_name)
                await event.client.send_message(
                    Var.LOG_CHANNEL,
                    f"#AutoApproved\nßecoz of outgoing msg\nUser - [{name0}](tg://user?id={event.chat_id})",
                )

    @bot.on(events.NewMessage(incoming=True,
                              func=lambda event: event.is_private))
    async def permitpm(event):
        user = await event.get_chat()
        if user.bot or user.is_self or user.verified:
            return
        if str(user.id) in DEVLIST:
            return
        apprv = is_approved(user.id)
        if not apprv and event.text != UND:
            name = user.first_name
            fullname = (user.first_name, user.last_name)
            username = user.username
            mention = f"[{get_display_name(user)}](tg://user?id={user.id})"
            count = len(get_approved())
            try:
                wrn = COUNT_PM[user.id] + 1
            except KeyError:
                wrn = 1
            if user.id in LASTMSG:
                prevmsg = LASTMSG[user.id]
                if event.text != prevmsg:
                    async for message in event.client.iter_messages(
                        user.id, search=UND
                    ):
                        await message.delete()

                    async for message in event.client.iter_messages(
                        user.id, search=UNS
                    ):
                        await message.delete()
                    await event.client.send_file(
                        user.id,
                        PMPIC,
                        caption=UNAPPROVED_MSG.format(
                            ON=OWNER_NAME,
                            warn=wrn,
                            twarn=WARNS,
                            UND=UND,
                            name=name,
                            fullname=fullname,
                            username=username,
                            count=count,
                            mention=mention,
                        ),
                    )
                elif event.text == prevmsg:
                    async for message in event.client.iter_messages(
                        user.id, search=UND
                    ):
                        await message.delete()
                    await event.client.send_file(
                        user.id,
                        PMPIC,
                        caption=UNAPPROVED_MSG.format(
                            ON=OWNER_NAME,
                            warn=wrn,
                            twarn=WARNS,
                            UND=UND,
                            name=name,
                            fullname=fullname,
                            username=username,
                            count=count,
                            mention=mention,
                        ),
                    )
                LASTMSG.update({user.id: event.text})
            else:
                async for message in event.client.iter_messages(user.id, search=UND):
                    await message.delete()
                await event.client.send_file(
                    user.id,
                    PMPIC,
                    caption=UNAPPROVED_MSG.format(
                        ON=OWNER_NAME,
                        warn=wrn,
                        twarn=WARNS,
                        UND=UND,
                        name=name,
                        fullname=fullname,
                        username=username,
                        count=count,
                        mention=mention,
                    ),
                )
                LASTMSG.update({user.id: event.text})
            if user.id not in COUNT_PM:
                COUNT_PM.update({user.id: 1})
            else:
                COUNT_PM[user.id] = COUNT_PM[user.id] + 1
            if COUNT_PM[user.id] >= WARNS:
                async for message in event.client.iter_messages(user.id, search=UND):
                    await message.delete()
                await event.respond(UNS)
                try:
                    del COUNT_PM[user.id]
                    del LASTMSG[user.id]
                except KeyError:
                    if Var.LOG_CHANNEL:
                        await event.client.send_message(
                            Var.LOG_CHANNEL,
                            "PMPermit is messed! Pls restart the bot!!",
                        )
                        return LOGS.info("COUNT_PM is messed.")
                await event.client(BlockRequest(user.id))
                await event.client(ReportSpamRequest(peer=user.id))
                if Var.LOG_CHANNEL:
                    name = await event.client.get_entity(user.id)
                    name0 = str(name.first_name)
                    await event.client.send_message(
                        Var.LOG_CHANNEL,
                        f"[{name0}](tg://user?id={user.id}) was blocked for spamming.",
                    )

    @register(outgoing=True, pattern=r"^\.approve$")
    async def approvepm(event):
        if apprvpm.reply_to_msg_id:
            reply = await event.get_reply_message()
            replied_user = await event.client.get_entity(reply.sender_id)
            aname = replied_user.id
            if str(aname) in DEVLIST:
                return await event.edit(
                    event, "Lol, He is my Developer\nHe is auto Approved"
                )
            name0 = str(replied_user.first_name)
            uid = replied_user.id
            if not is_approved(uid):
                approve_user(uid)
                await event.edit(f"[{name0}](tg://user?id={uid}) `approved to PM!`")
                await asyncio.sleep(3)
                await event.delete()
            else:
                await event.edit("`User may already be approved.`")
                await asyncio.sleep(5)
                await event.delete()
        elif event.is_private:
            user = await event.get_chat()
            aname = await event.client.get_entity(user.id)
            if str(user.id) in DEVLIST:
                return await event.edit(
                    event, "Lol, He is my Developer\nHe is auto Approved"
                )
            name0 = str(aname.first_name)
            uid = user.id
            if not is_approved(uid):
                approve_user(uid)
                await event.edit(f"[{name0}](tg://user?id={uid}) `approved to PM!`")
                async for message in event.client.iter_messages(user.id, search=UND):

                    await message.delete()
                async for message in event.client.iter_messages(user.id, search=UNS):
                    await message.delete()
                await asyncio.sleep(3)
                await event.delete()
                if Var.LOG_CHANNEL:
                    await event.client.send_message(
                        Var.LOG_CHANNEL,
                        f"#APPROVED\nUser: [{name0}](tg://user?id={uid})",
                    )
            else:
                await event.edit("`User may already be approved.`")
                await asyncio.sleep(5)
                await event.delete()
                if Var.LOG_CHANNEL:
                    await event.client.send_message(
                        Var.LOG_CHANNEL,
                        f"#APPROVED\nUser: [{name0}](tg://user?id={uid})",
                    )
        else:
            await event.edit(NO_REPLY)

    @register(outgoing=True, pattern=r"^\.disapprove$")
    async def disapprovepm(event):
        if event.reply_to_msg_id:
            reply = await event.get_reply_message()
            replied_user = await event.client.get_entity(reply.sender_id)
            aname = replied_user.id
            if str(aname) in DEVLIST:
                return await event.edit(
                    event, "`Lol, He is my Developer\nHe Can't Be DisApproved.`"
                )
            name0 = str(replied_user.first_name)
            if is_approved(replied_user.id):
                disapprove_user(replied_user.id)
                await event.edit(
                    f"[{name0}](tg://user?id={replied_user.id}) `Disaproved to PM!`"
                )
                await asyncio.sleep(5)
                await event.delete()
            else:
                await event.edit(
                    f"[{name0}](tg://user?id={replied_user.id}) was never approved!"
                )
                await asyncio.sleep(5)
                await event.delete()
        elif e.is_private:
            bbb = await event.get_chat()
            aname = await event.client.get_entity(bbb.id)
            if str(bbb.id) in DEVLIST:
                return await event.edit(
                    event, "`Lol, He is my Developer\nHe Can't Be DisApproved.`"
                )
            name0 = str(aname.first_name)
            if is_approved(bbb.id):
                disapprove_user(bbb.id)
                await event.edit(f"[{name0}](tg://user?id={bbb.id}) `Disaproved to PM!`")
                await asyncio.sleep(5)
                await event.delete()
                if Var.LOG_CHANNEL:
                    await event.client.send_message(
                        Var.LOG_CHANNEL,
                        f"[{name0}](tg://user?id={bbb.id}) was disapproved to PM you.",
                    )
            else:
                await event.edit(f"[{name0}](tg://user?id={bbb.id}) was never approved!")
                await asyncio.sleep(5)
                await event.delete()
        else:
            await event.edit(NO_REPLY)

            BOTLOG_CHATIDger.warn(str(e))


CMD_HELP.update(
    {
        "pmpermit": ">`.approve`"
        "\nUsage: Cek sendiri.\n"
        ">`.disapprove`"
        "\nUsage: Cek sendiri."
    }
)

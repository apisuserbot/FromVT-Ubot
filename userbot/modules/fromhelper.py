""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/vckyouuu)"
        "\n[Repo](https://github.com/vckyou/FromVT-Ubot)"
        "\n[Instagram](Instagram.com/Vckyouuu)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Vckyou/FromVT-Ubot/FromVT-Ubot/varshelper.txt)")


CMD_HELP.update({
    "lhelp":
    "`.lordhelp`\
\nPenjelasan: Bantuan Untuk 𝘍𝘳𝘰𝘮𝘝𝘛-𝘜𝘴𝘦𝘳𝘉𝘰𝘵.\
\n`.lordvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})

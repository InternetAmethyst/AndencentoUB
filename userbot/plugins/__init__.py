import datetime
from .. import *
from ..config import Config
from ..helpers import *
from ..utils import *
from telethon import version


from userbot import *
from userbot.config import Config
from userbot.helpers import *
from userbot.utils import *
from userbot.random_strings import *
from telethon import version

Eiva_USER = Andencento.me.first_name
ForGo10God = Andencento.uid
Eiva_mention = f"[{Eiva_USER}](tg://user?id={ForGo10God})"

Andencento_USER = bot.me.first_name
Andencento_mention = f"[{Andencento_USER}](tg://user?id={ForGo10God})"
Andencento_logo = "./userbot/resources/andencento_logo.jpg"
cjb = "./userbot/resources/cjb.jpg"
restlo = "./userbot/resources/rest.jpeg"
shuru = "./userbot/resources/shuru.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
Andencento_ver = "0.1"
tel_ver = version.__version__

user_mention = Andencento_mention

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid


sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m = "Disabled"

START_TIME = datetime.datetime.now()




HANDLER = os.environ.get("HANDLER", ".")

from .. import CMD_HELP, CMD_HELP_BOT
import os

chnl_link = "https://t.me/Andencento"

COMMAND_HAND_LER = os.environ.get("HANDLER", ".")

#################################################################################################################

class CmdHelp:
    """
    The class I wrote to better generate command aids.
    """

    FILE = ""
    ORIGINAL_FILE = ""
    FILE_AUTHOR = ""
    IS_OFFICIAL = True
    COMMANDS = {}
    PREFIX = COMMAND_HAND_LER
    WARNING = ""
    INFO = ""

    def __init__(self, file: str, official: bool = True, file_name: str = None):
        self.FILE = file
        self.ORIGINAL_FILE = file
        self.IS_OFFICIAL = official
        self.FILE_NAME = file_name if not file_name == None else file + ".py"
        self.COMMANDS = {}
        self.FILE_AUTHOR = ""
        self.WARNING = ""
        self.INFO = ""

    def set_file_info(self, name: str, value: str):
        if name == "name":
            self.FILE = value
        elif name == "author":
            self.FILE_AUTHOR = value
        return self

    def add_command(self, command: str, params=None, usage: str = "", example=None):
        """
        Inserts commands..
        """

        self.COMMANDS[command] = {
            "command": command,
            "params": params,
            "usage": usage,
            "example": example,
        }
        return self

    def add_warning(self, warning):
        self.WARNING = warning
        return self

    def add_info(self, info):
        self.INFO = info
        return self

    def get_result(self):
        """
        Brings results.
        """

        result = f"**📗 File :** `{self.FILE}`\n"
        if self.WARNING == "" and self.INFO == "":
            result += f"**⬇️ Official:** {'✅' if self.IS_OFFICIAL else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if self.IS_OFFICIAL else '❌'}\n"

            if self.INFO == "":
                if not self.WARNING == "":
                    result += f"**⚠️ Warning :** {self.WARNING}\n\n"
            else:
                if not self.WARNING == "":
                    result += f"**⚠️ Warning :** {self.WARNING}\n"
                result += f"**ℹ️ Info:** {self.INFO}\n\n"

        for command in self.COMMANDS:
            command = self.COMMANDS[command]
            if command["params"] == None:
                result += f"**🛠 Command :** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
            else:
                result += f"**🛠 Command :** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

            if command["example"] == None:
                result += f"**💬 Details :** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Details :** `{command['usage']}`\n"
                result += (
                    f"**⌨️ For Example :** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
                )
        return result

    def add(self):
        """
        Directly adds CMD_HELP.
        """
        CMD_HELP_BOT[self.FILE] = {
            "info": {
                "official": self.IS_OFFICIAL,
                "warning": self.WARNING,
                "info": self.INFO,
            },
            "commands": self.COMMANDS,
        }
        CMD_HELP[self.FILE] = self.get_result()
        return True

    def getText(self, text: str):
        if text == "REPLY_OR_USERNAME":
            return "<user name> <user name/answer >"
        elif text == "OR":
            return "or"
        elif text == "USERNAMES":
            return "<user name (s)>"

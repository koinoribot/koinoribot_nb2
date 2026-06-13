from nonebot import on_command
from nonebot.params import Depends
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, Event
import time

from ...money import money
from ...tools import get_uid

__plugin_meta__ = PluginMetadata(
    name="say_goodnight",
    description="说晚安",
    usage="说晚安"
)

say_goodnight = on_command("晚安")

cooldown = {}


@say_goodnight.handle()
async def say_goodnight_handle(
    bot: Bot,
    event: Event,
    uid: int = Depends(get_uid),
) -> None:
    user_id = event.get_user_id()

    if user_id == str(bot.self_id):
        return

    now = time.time()
    if user_id in cooldown and now - cooldown[user_id] < 10:
        return
    cooldown[user_id] = now

    if money.gold >= 50:
        money.gold -= 50
        await say_goodnight.finish("晚安喵")
    else:
        return

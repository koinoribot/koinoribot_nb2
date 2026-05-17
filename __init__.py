"""
Koinoribot NB2 - 主插件入口

从旧版 hoshinobot/nonebot1.8 迁移的 koinoribot
支持 OneBot V11 和 QQ-Bot 双协议
"""

from pathlib import Path
import nonebot
from nonebot import get_plugin_config, get_driver
from nonebot.plugin import PluginMetadata

from .config import Config

# 导入核心模块
from . import uid_manager
from . import money
from . import resources
from . import nickname
from .koinori_config import config as koinori_config
from . import tools as _tools
__plugin_meta__ = PluginMetadata(
    name="koinoribot_nb2",
    description="Koinoribot NoneBot2 版本 - 集成多种娱乐功能",
    usage="签到、钓鱼、宠物、炒股、红包等功能",
    config=Config,
)

# 获取配置
config = get_plugin_config(Config)

# 获取驱动器
driver = get_driver()


@driver.on_startup
async def init_koinoribot():
    """初始化 koinoribot"""
    # 设置资源目录
    plugin_dir = Path(__file__).parent
    src_dir = plugin_dir / "src"
    resources.set_resource_dir(src_dir)
    
    # 设置数据库路径
    db_path = src_dir / "database" / "koinoribot.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    uid_manager.set_database_path(str(db_path))
    money.set_database_path(str(db_path))
    nickname.set_db_path(str(db_path))
    
    # 初始化数据库
    uid_manager.init_uid_database()
    money.init_money_database()
    nickname.init_nickname_database()
    
    # 读取官Bot AppID配置
    appid_path = plugin_dir / "appid.json"
    try:
        import json
        with open(appid_path, "r", encoding="utf-8") as f:
            appid_data = json.load(f)
        appid = appid_data.get("appid", "")
        openid_api = appid_data.get("openid_api", "")
        if appid:
            _tools.set_qqbot_appid(appid, openid_api)
            nonebot.logger.info(f"已加载官Bot AppID: {appid}")
        else:
            nonebot.logger.warning("appid.json 中 appid 为空，官Bot用户昵称将显示为默认值")
    except FileNotFoundError:
        import json
        default_data = {
            "comment": "在此填入你的官方Bot AppID，用于通过 openid 获取用户昵称和头像。不填则官bot用户昵称将显示为默认值。",
            "appid": "",
            "openid_api": "https://oiapi.net/api/Openid"
        }
        with open(appid_path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=2, ensure_ascii=False)
        nonebot.logger.info("已自动创建 appid.json，请填写 appid 和 openid_api")
    except Exception as e:
        nonebot.logger.warning(f"读取 appid.json 失败: {e}，官Bot用户昵称将显示为默认值")
    
    nonebot.logger.info("Koinoribot NB2 初始化完成")


# 加载子插件
sub_plugins = nonebot.load_plugins(
    str(Path(__file__).parent.joinpath("plugins").resolve())
)

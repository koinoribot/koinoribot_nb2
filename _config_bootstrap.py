from pathlib import Path
import shutil


CONFIG_FILENAME = "koinori_config.py"
TEMPLATE_FILENAME = "koinori_config.py.template"


def ensure_koinori_config() -> tuple[Path, bool]:
    """Create the local config from the template before imports need it."""
    plugin_dir = Path(__file__).resolve().parent
    config_path = plugin_dir / CONFIG_FILENAME
    template_path = plugin_dir / TEMPLATE_FILENAME

    if config_path.exists():
        return config_path, False

    if not template_path.exists():
        raise FileNotFoundError(
            f"{CONFIG_FILENAME} does not exist and template {TEMPLATE_FILENAME} was not found"
        )

    shutil.copyfile(template_path, config_path)
    return config_path, True

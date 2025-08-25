import os
import yaml

DEFAULT_CONFIG = {
    "manual_overrides": {},
    "gpu_threshold": 30,
    "learning": True,
    "battery_aware": False,
}

CONFIG_PATH = os.path.expanduser("~/.config/auto_gpu_switcher/config.yaml")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH),  exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            yaml.dump(DEFAULT_CONFIG, f)
        return DEFAULT_CONFIG.copy()
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f)

        
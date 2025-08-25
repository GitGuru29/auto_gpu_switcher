import time
import threading
from .config import load_config, save_config
from .gpu_utils import get_nvidia_processes, is_nvidia_available
from .monitor import get_running_apps, classify_app

class GPUSwitcherService:
    def __init__(self):
        self.config = load_config()
        self.running = False
        self.learned = {} 

def monitor_loop(self):
    while self.running:
        nvidia_procs = get_nvidia_processes() if is_nvidia_available() else []
        running_apps = get_running_apps()
        for pid, name in running_apps.items():
            override = self.config["manual_overrides"].get(name)
            if override:
                continue
            classification = classify_app(pid, nvidia_procs, self.config["gpu_threshold"])
            if self.config["learning"]:
                self.learned[name] = classification
        time.sleep() #add sleep time

def start(self):
    self.runing = True
    self.thread = threading.Thread(target=self.monitor_loop, daemon=True)
    self.thread.start()

def stop(self):
    self.runing = False
    self.thread.join()

def get_status(self):
    return{
        "learned": self.learned,
        "manual_overrides": self.config["manual_overrides"]
    }

def set_manual_override(self, app, gpu):
    self.config["manual_overrides"][app] = gpu
    save_config(self.config)
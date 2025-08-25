import psutil
from .gpu_utils import get_nvidia_processes

def get_running_apps():
    apps = {}
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['username'] and proc.info['username'] != 'root':
                apps[proc.info['pid']] = proc.info['name']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return apps

def classify_app(pid, nvidia_procs, threshold):
    for proc in nvidia_procs:
        if proc['pid'] == pid:
            if proc['mem'] > threshold:
                return "heavy"
            else:
                return "light"
    return "light"

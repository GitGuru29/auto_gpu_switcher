import os
import subprocess
from .gpu_utils import detect_prime_run

def launch_on_gpu(command, gpu="integrated"):
    if gpu == "integrated":
        subprocess.Popen(command)
    elif gpu == "nvidia":
        if detect_prime_run():
            subprocess.Popen(["prime-run"] + command)
        else:
            env = os.environ.copy()
            env["__NV_PRIME_RENDER_OFFLOAD"] = "1"
            env["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
            subprocess.Popen(command, env=env)
    else:
        raise ValueError("Unknown GPU: {}".format(gpu))
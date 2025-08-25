import subprocess
import shutil

def is_nvidia_available():
    try:
        subprocess.check_output(["nvidia-smi"], stderr=subprocess.DEVNULL)
        return True
    except Exception:
        try:
            lsmod = subprocess.check_output(["lsmod"], encoding="utf-8")
            if "nvidia" in lsmod:
                return True
        except Exception:
            pass
    return False

def get_nvidia_processes():
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-compute-apps=pid,process_name,used_gpu_memory", "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        process = []
        for line in output.strip().split("\n"):
            if line:
                pid, name, mem = [x.strip() for x in line.split(",")]
                procs.append({"pid": int(pid), "name":name, "mem": int(mem)})
        return process
    except Exception:
        return []

def detect_prime_run():
    return shutil.which("prime-run") is not None

    
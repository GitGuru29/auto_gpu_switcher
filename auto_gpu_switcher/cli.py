import argparse
import time
from .service import GPUSwitcherService
from .launcher import launch_on_gpu


def main():
    parser = argparse.ArgumentParser(description="Auto GPU Switcher CLI")
    parser.add_argument("--status", action="store_true", help="Show current GPU assignments")
    parser.add_argument("--override", nargs=2, metavar=("APP", "GPU"), help="Manually override GPU for app (integrated/nvidia)")
    parser.add_argument("--start", action="store_true", help="Start background service")
    parser.add_argument("--launch", nargs="+", metavar="COMMAND", help="Launch an app on the appropriate GPU")
    args = parser.parse_args()

    service = GPUSwitcherService()

    if args.status:
        status = service.get_status()
        print("Learned assignments:", status["learned"])
        print("Manual overrides:", status["manual_overrides"])

    elif args.override:
        app, gpu = args.override
        if gpu not in ("integrated", "nvidia"):
            print("Error: GPU must be 'integrated' or 'nvidia'")
        else:
            service.set_manual_override(app, gpu)
            print(f"Override set: {app} -> {gpu}")

    elif args.start:
        print("Starting GPU Switcher service (Ctrl+C to stop)...")
        service.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping service...")
            service.stop()

    elif args.launch:
        app = args.launch[0]
        config = service.config
        gpu = config["manual_overrides"].get(app, "integrated")
        print(f"Launching {' '.join(args.launch)} on {gpu} GPU...")
        launch_on_gpu(args.launch, gpu)

    else:
        parser.print_help()

from setuptools import setup, find_packages

setup(
    name="auto_gpu_switcher",
    version="0.3.0",
    description="Cross-distro Auto GPU Switcher for Linux Hybrid Graphics",
    author="SILUNA NUSAL",
    packages=find_packages(),
    install_requies=[
        "psutil",
        "pyyaml",
        "PyQt5"
    ],
    entry_points={
        "console_scripts": [
            "auto-gpu-switcher=auto_gpu_switcher.cli:main",
            "auto-gpu-switcher-gui=auto_gpu_switcher.gui:main"
        ]
    },
    include_package_data=True,
)
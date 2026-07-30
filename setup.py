from setuptools import setup, find_packages

setup(
    name="plex-mpv-shim",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-mpv>=1.0.6",
        "python-mpv-jsonipc>=1.1.0",
        "requests>=2.31.0",
        "pystray>=0.19.5",
    ],
    entry_points={
        "console_scripts": [
            "plex-mpv-shim=plex_mpv_shim.mpv_shim:main",
        ],
    },
    author="iwalton3 / Forked",
    description="Cast media from Plex to MPV with Fedora 44, GNOME 50, and mpv 0.41 optimizations",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)

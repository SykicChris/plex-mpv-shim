import logging
import multiprocessing
import os
import sys

log = logging.getLogger('gui_mgr')

def tray_worker():
    """Worker process for running the system tray icon safely under Wayland/GNOME."""
    try:
        import pystray
        from PIL import Image

        icon_path = os.path.join(os.path.dirname(__file__), 'systray.png')
        if not os.path.exists(icon_path):
            log.warning("Systray icon not found at %s", icon_path)
            return

        image = Image.open(icon_path)

        def on_quit(icon, item):
            icon.stop()
            os._exit(0)

        menu = pystray.Menu(
            pystray.MenuItem("Plex MPV Shim", lambda: None, enabled=False),
            pystray.MenuItem("Quit", on_quit)
        )

        icon = pystray.Icon("plex-mpv-shim", image, "Plex MPV Shim", menu)
        icon.run()
    except Exception as e:
        log.warning("System tray unavailable (GNOME Wayland without AppIndicator?): %s", e)

class UserInterface:
    def __init__(self):
        self.tray_process = None
        self.gui_available = True

    def start_tray(self):
        try:
            self.tray_process = multiprocessing.Process(target=tray_worker, daemon=True)
            self.tray_process.start()
            log.info("System tray worker initialized.")
        except Exception as e:
            log.warning("Failed to launch systray process: %s", e)

    def stop_tray(self):
        if self.tray_process and self.tray_process.is_alive():
            try:
                self.tray_process.terminate()
                self.tray_process.join(timeout=2)
            except Exception as e:
                log.debug("Error terminating tray process: %s", e)

    def open_gui(self):
        log.info("GUI requested; operating in headless/tray-managed desktop mode.")

userInterface = UserInterface()

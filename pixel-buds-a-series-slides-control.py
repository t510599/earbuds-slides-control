import time
import keyboard
import platform

# dummy class
class ScanCode(object):
    PLAY_PAUSE = None
    NEXT_TRACK = None
    PREV_TRACK = None

class Controller:
    scan_code = ScanCode

    def __init__(self) -> None:
        # For Pixel Buds A-Series, it would send "play/pause media" right after "next/previous track" occurs.
        self.lock = False
        self.hooks = dict()
        self.keys = [self.scan_code.PLAY_PAUSE, self.scan_code.NEXT_TRACK, self.scan_code.PREV_TRACK]

    def next_page(self, _ev: keyboard.KeyboardEvent):
        if not self.lock:
            keyboard.send("right")

        self.lock = False

    def last_page(self, _ev: keyboard.KeyboardEvent):
        self.lock = True # lock "play/pause media" once
        keyboard.send("left")

    def bind_hook(self):
        for code in self.keys:
            # clean up old one
            if self.hooks.get(code):
                keyboard.unhook_key(self.hooks[code])

            hook = keyboard.on_press_key(code, self.hook, suppress=True)
            self.hooks[code] = hook

    def unbind_hook(self):
        for code in list(self.hooks.keys()):
            keyboard.unhook_key(self.hooks[code])
            self.hooks.pop(code)

    def hook(self, ev: keyboard.KeyboardEvent):
        if ev.scan_code == self.scan_code.PLAY_PAUSE:
            self.next_page(ev)
        elif ev.scan_code == self.scan_code.NEXT_TRACK:
            self.last_page(ev)
        elif ev.scan_code == self.scan_code.PREV_TRACK:
            # we still need to lock for "previous track", so the subsequent "play/pause media" won't trigger next page
            self.lock = True
        else:
            # propagate all other keys
            keyboard.send(ev.name)

    def loop(self):
        # return until Ctrl+C
        while True:
            try:
                time.sleep(100)
            except KeyboardInterrupt:
                return

# Scan Codes for Windows
class Win_ScanCode(ScanCode):
    PLAY_PAUSE = -179
    NEXT_TRACK = -176
    PREV_TRACK = -177

class WindowsController(Controller):
    scan_code = Win_ScanCode

if __name__ == "__main__":
    if platform.system() == "Windows":
        controller = WindowsController()
    else:
        raise OSError("Unsupported platform '{}'".format(platform.system()))

    print("Start hijacking media buttons!")
    controller.bind_hook()
    controller.loop()

    controller.unbind_hook()
    print("Exited.")
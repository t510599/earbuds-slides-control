import time
import asyncio
import keyboard

from config import NEXT_PAGE_KEY, PREV_PAGE_KEY

from winrt.windows.media import \
    SystemMediaTransportControls, SystemMediaTransportControlsButtonPressedEventArgs, SystemMediaTransportControlsButton, MediaPlaybackType
from winrt.windows.media.playback import MediaPlayer, MediaPlaybackState

lock = False

def next_page():
    global lock

    # "PAUSE" is triggered with the following "NEXT"
    # so we have to wait for a while to make sure this is not the one followed by "NEXT"
    time.sleep(0.5)
    if not lock:
        keyboard.send(NEXT_PAGE_KEY)
        print("Next Page!")

    lock = False


def previous_page():
    global lock
    lock = True
    keyboard.send(PREV_PAGE_KEY)
    print("Previous Page!")


def btn_press(sender: SystemMediaTransportControls, args: SystemMediaTransportControlsButtonPressedEventArgs):
    global lock

    match args.button:
        case SystemMediaTransportControlsButton.PLAY | SystemMediaTransportControlsButton.PAUSE:
            next_page()
        case SystemMediaTransportControlsButton.NEXT:
            previous_page()
        case SystemMediaTransportControlsButton.PREVIOUS:
            # lock and do nothing
            lock = True
            pass


async def setup_control():
    # just a dummy player for SMTC
    player = MediaPlayer()
    controls = player.system_media_transport_controls
    # detach command manager from player, so we can handle the event manually
    player.command_manager.is_enabled = False

    # show SMTC
    controls.is_enabled = True
    # setup status
    controls.is_play_enabled = True
    controls.is_pause_enabled = True
    controls.is_next_enabled = True
    controls.is_previous_enabled = True

    # set it to playing so the control would stay with us
    controls.playback_status = MediaPlaybackState.PLAYING

    # update SMTC info
    updater = controls.display_updater
    if updater:
        updater.type = MediaPlaybackType.MUSIC
        updater.music_properties.artist = "Slides Controller"
        updater.music_properties.title = "Slides Controller"
        updater.update()

    # bind handler
    controls.add_button_pressed(btn_press)

    # run forever
    await asyncio.Future()

if __name__ == '__main__':
    print("Started as a media player!")
    try:
        asyncio.run(setup_control())
    except:
        pass
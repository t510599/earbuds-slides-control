# Earbuds-Slides-Control

This simple script helps you to control your slides with your wireless earbuds!  
From now on, you won't need other's help during your presentation!  

## Usage
- Tap Once: `Next Page` (Originally play/pause media)
- Tap Twice: `Previous Page` (Originally next track)
- Tap 3 times: Nothing happen (Originally previous track)

## Run
### `pixel-buds-a-series-slides-control.py`
*Implementation for Pixel Buds A Series, but may work with other devices*
1. `pip install keyboard`
2. `python pixel-buds-a-series-slides-control.py` (if on linux, you must run this with `sudo`)

### `windows-smtc.py` (Windows 10+ only)
1. `pip install winwt`
2. `python windows-smtc.py`

## How it works
When you tap on your earphone, it would send the media control signal to your computer.  
It intercepts the media control button event, and it sends left/right keyboard event instead.

## For Python 3.10+ Users with `windows-smtc.py`
Official `winrt` package supports Python 3.7 ~ 3.9 only.  
You may refer to [winsdk](https://github.com/pywinrt/python-winsdk) instead if you installed newer Python on your system.  
You have to replace `winrt` imports in the file with `winsdk` on your own.

## For Linux Users
The current scan code are fetched from my laptop with Ubuntu 22.04 and Arch Linux, and luckily it seemed to be same on both system.  
But the scan code on your system may vary. You could use `sudo python -m keyboard` to observe the scan code on your own.  

## Known Issues
- [x] Currently only Windows support, since I am lazy to find scan codes on other platform.
- [x] KeyboardEvent for media controls never fires if you are currently playing media.
    - Supported by SystemMediaTransportControls on Windows with `windows-smtc.py`
- [ ] The tap would control both slides and media at the same time on Linux.  

**PR Welcome!**

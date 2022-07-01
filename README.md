# Pixel-Buds-A-Series-Slides-Control

This simple script helps you to control your slides with your Pixel Buds A-Series!  
From now on, you won't need other's help during your presentation!  

## Usage
- Tap Once: `Next Page` (Originally play/pause media)
- Tap Twice: `Previous Page` (Originally next track)
- Tap 3 times: Nothing happen (Originally previous track)

## Run
### `pixel-buds-a-series-slides-control.py`
1. `pip install keyboard`
2. `python pixel-buds-a-series-slides-control.py`

### `windows-smtc.py` (Windows 10+ only)
1. `pip install winsdk`
2. `python windows-smtc.py`

## How it works
When you tap on your earphone, it would send the media control signal to your computer.  
It intercepts the media control button event, and it sends left/right keyboard event instead.

## Known Issues
- [ ] Currently only Windows support, since I am lazy to find scan codes on other platform.
- [x] KeyboardEvent for media controls never fires if you are currently playing media.
    - Supported by SystemMediaTransportControls on Windows with `windows-smtc.py`

**PR Welcome!**
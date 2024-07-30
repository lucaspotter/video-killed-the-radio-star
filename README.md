# Video Killed the Radio Star

> I heard you on the wireless back in '52
>
> Lying awake, intently tuning in on you

This sure is a project! I am currently trying to create a *thing* which automatically plays video from specific libraries.
I have a Raspberry Pi 3B strapped to an old RCA TruFlat and we're going for a spin. In a similar vein, show and movie recommendations
are welcome. 

This actually works how I imagined it to. Wowzers. Here's how to get it working on your side.

## Setup

- `git clone https://github.com/lucaspotter/video-killed-the-radio-star.git`
- Go into main.py and retrotv.sh and change the directories to what you're using
- "Legally obtain" your favorite shows, movies, and classic commercials
  - me when internet archive
- If you want it to run on boot, then you need to do a magic trick involving rc.local
  - `su user -c '/home/user/retrotv/retrotv.sh'`
  - Change directories, username, yadda yadda
  - Why rc.local and not cron? Cron is [weird and old.](https://forums.raspberrypi.com/viewtopic.php?p=2184401#p2184401) Your audio drivers will fail.
- Attach your Pi or other computer to a television set
  - Silly me assuming that the composite output would be easy as an Adafruit cable and `enable_tvout=1`. I wanted a retro experience without a converter box - I should have gotten the converter box. Abandon hope all ye who enter.
- Run the script (or reboot if you're using rc.local) and enjoy!
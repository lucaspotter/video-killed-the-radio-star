# Video Killed the Radio Star

> I heard you on the wireless back in '52
>
> Lying awake, intently tuning in on you

This sure is a project! I am currently trying to create a *thing* which automatically plays video from specific libraries.
I have a Raspberry Pi 3B strapped to an old RCA TruFlat and we're going for a spin. In a similar vein, show and movie recommendations
are welcome. 

This was *originally* just a playlist generator but then I saw something else and decided that I should do that instead.
Part 1's the playlist thing, part 2's the flask thing.

## Part I

Generates a number of .m3u playlists for automatic playback with VLC. Includes script to begin playback on startup.

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

## Part 2

Ok so. This is a yoink and twist from <ytch.xyz> - the idea is automatically playing youtube videos in the style of cable tv. 
My current implementation is... janky to say the best. But it does work.

### TODO
- ~~Actually shuffle the playlists~~
- ~~Maybe stop using playlists if possible~~
  - Well almost fixed. Playlists now in JSON form, can't be deleted
  - Youtube has a mix feature - cash in?
- Add more channels
  - This one matters less
- Abandon ship on the composite out of the Raspberry Pi
  - But this one costs money
- Maybe infrared?
  - It'd be funny to control it with an actual remote

### KNOWN ISSUES
- JSON parser shatters when prompted with a nonstandard character
  - Weird quotation marks, emojis, etc
  - Default lists has been cleared, be wary when adding your own

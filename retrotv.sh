SCRIPT="/home/user/retrotv/main.py"
PLAYLISTS="/home/user/retrotv/playlists"

rm $PLAYLISTS/*.m3u
python $SCRIPT
export DISPLAY=:0.0
sleep 30
vlc -f $PLAYLISTS/*.m3u
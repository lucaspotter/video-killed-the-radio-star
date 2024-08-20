HOST="/home/user/retrotv/main.py"


rm $PLAYLISTS/*.m3u
python $SCRIPT
export DISPLAY=:0.0
sleep 30
chromium-browser --kiosk
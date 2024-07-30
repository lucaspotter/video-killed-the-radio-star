import os
import random

movieDir = "/home/user/retrotv/movies"
tvDir = "/home/user/retrotv/tv"
advertsDir = "/home/user/retrotv/adverts"
playlistDir = "/home/user/retrotv/playlists"


def absolutePathing(directory):
    root, dirs, files = next(os.walk(directory, topdown=True))
    files = [os.path.join(root, f) for f in files]
    return files


for i in range(12):
    moviePick = random.choice(absolutePathing(movieDir))
    tvPicks = random.sample(absolutePathing(tvDir), 3)
    advertPicks = random.sample(absolutePathing(advertsDir), 25)

    print(moviePick)
    print(tvPicks)
    print(advertPicks)

    playlistName = str(i) + ".m3u"
    playlist = open(playlistDir + "/" + playlistName, "x")
    playlist.close()
    playlist = open(playlistDir + "/" + playlistName, "a")
    playlist.write(tvPicks[0])
    for j in range(0, 5):
        playlist.write("\n" + advertPicks[j])
    playlist.write("\n" + tvPicks[1])
    for j in range(5, 10):
        playlist.write("\n" + advertPicks[j])
    playlist.write("\n" + tvPicks[2])
    for j in range(10, 15):
        playlist.write("\n" + advertPicks[j])
    playlist.write("\n" + moviePick)
    for j in range(15, 20):
        playlist.write("\n" + advertPicks[j])
    playlist.close()

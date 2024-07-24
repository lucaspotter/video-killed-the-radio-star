# TODO - select a movie, 3 episodes of any particular show, and 40 advertisements

"""
Ah shit. Another project?


MOVIE
    - no issues?
TV
    - make sure no duplicates
    - consider doing 3 in a row? s1e1, s1e2, s1e3
ADVERTS
    - make sure no duplicates
    - get more maybe?
"""

import os
import random

movieDir = "F:/retrotv/movies"
tvDir = "F:/retrotv/tv"
advertsDir = "F:/retrotv/adverts"
playlistDir = "F:/retrotv/playlists"

for i in range(12):
    moviePick = random.choice(os.listdir(movieDir))
    tvPicks = random.sample(os.listdir(tvDir), 3)
    advertPicks = random.sample(os.listdir(advertsDir), 25)

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
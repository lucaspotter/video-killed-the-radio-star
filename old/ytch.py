# 8 on the Somerton scale.

import os
import random
from argparse import ArgumentParser

parser = ArgumentParser(prog='YTCH',
                        description='Like cable. But worse.',
                        epilog='Idea yoinked and twisted from ytch.xyz. Thnx to Hadi Safa.')
parser.add_argument("channel", type=int, help="select a channel", metavar="C", choices=range(1, 5))
args = parser.parse_args()

# Currently 4 channels
# 1 - News
# 2 - Food
# 3 - Music Videos
# 4 - Video Essays & Documentaries
# Easy enough to add more.


def channelToContent(channel):
    match channel:
        case 1:
            # news is pretty bad rn lmao
            return "https://www.youtube-nocookie.com/embed/GZ9ZBjtLoTg?list=RDNSj3Qx97oiTy8?autoplay=1&index=1"
        case 2:
            # some would say playlists are not the best choice here
            return "https://www.youtube-nocookie.com/embed/VkaB4FI36gk?autoplay=1&list=PLpfv1AIjenVMmT7iRx6Nwu6uG6A9gSD0j&index=" + str(random.randint(0, 100))
        case 3:
            return "https://www.youtube-nocookie.com/embed/sOnqjkJTMaA?autoplay=1&list=PLDkAFNanIXVgDKa05y_eFqAy6ToBsL4up&index=" + str(random.randint(0, 100))
        case 4:
            return "https://www.youtube-nocookie.com/embed/yDp3cB5fHXQ?autoplay=1&list=PLX61GfEeHdKwn6lXy8Q-OXongRx--1Hmt&index=" + str(random.randint(0, 100))

print("Playing channel", args.channel)

os.system("chromium-browser --kiosk " + str(channelToContent(args.channel)))

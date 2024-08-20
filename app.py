import random

from flask import Flask, request, render_template
import json

app = Flask(__name__)
host = "127.0.0.1:5000"


def channelToVideo(channel):
    match channel:
        case 2:
            # food network
            f = open('food.json')
            data = json.load(f)
            video = random.randint(0, int(len(data))-1)
            print(video)
            print(data[video]['videoId'])
            return data[video]['videoId']
        case 3:
            # music videos
            f = open('music.json')
            data = json.load(f)
            video = random.randint(0, int(len(data)) - 1)
            print(video)
            print(data[video]['videoId'])
            return data[video]['videoId']
        case 4:
            # harris bomberman? is that you?
            f = open('video essay.json')
            data = json.load(f)
            video = random.randint(0, int(len(data)) - 1)
            print(video)
            print(data[video]['videoId'])
            return data[video]['videoId']
        case _:
            # oh! kitty!
            return "0Bmhjf0rKe8"


@app.route("/")
def serving():  # we slay in this household
    channel = request.args.get('channel', 1, type=int)
    print(channel)
    return render_template('index.html', channel=channel, video=channelToVideo(channel), host=host)

@app.route("/next")
def newFlavor(): # well now it's a food metaphor
    channel = request.args.get('channel', 1, type=int)
    return "fuck you"
    pass


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

from flask import Flask, request, render_template

app = Flask(__name__)
host = "10.0.0.69"


def keepSmoking(channel):  # car seat headrest
    match channel:
        case 1:
            return "yDp3cB5fHXQ"
        case 2:
            return "9yjZpBq1XBE"
        case 3:
            return "YQ_xWvX1n9g"
        case 4:
            return "0twDETh6QaI"
        case _:
            return "0Bmhjf0rKe8"


@app.route("/")
def serving():  # we slay in this household
    channel = request.args.get('channel', 1, type=int)
    print(channel)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

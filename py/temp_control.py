import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/targettemperature/<float:temp>", methods=["GET"])
def set_temp(temp):
    print(temp)
    return "OK"


@app.route("/targetstate/<int:state>", methods=["GET"])
def set_state(state):
    print(state)
    return "OK"


app.run()

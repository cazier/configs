from flask import Flask

import config

app = Flask(__name__)


@app.route("/")
def greet() -> str:
    page = f"<p>{config.greeting}, {config.user}!</p>"
    page += f"<p>This {config.kind} came from a {config.source} file.</p>"

    return page


if __name__ == "__main__":
    app.run(host=config.bind, port=config.port, debug=config.debug)

from flask import Flask
from views import query_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(query_blueprint)
    return app


app = create_app()
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import BaseConfig


db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)

    return app


app = create_app()


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    params = db.Column(db.String())
    result = db.Column(db.String())

    def __init__(self, url, params, result, **kwargs):
        self.url = url
        self.params = params
        self.result = result
        super().__init__(**kwargs)


@app.route('/')
def hello():
    result_text = 'Hello!'
    db_request = Request(request.url, '', result_text)
    db.session.add(db_request)
    db.session.commit()
    return jsonify({'text': result_text})


@app.route("/test", methods=["POST"])
def test():
    text = request.form["text"]
    app.logger.debug(f'{request.url} - {text}')
    db_request = Request(request.url, text, '')
    db.session.add(db_request)
    db.session.commit()
    return jsonify(success=True), 200, {'ContentType':'application/json'} 


if __name__ == '__main__':
    app.run(host='0.0.0.0')

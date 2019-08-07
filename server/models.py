from server import db


# class Request(db.Model):
#     __tablename__ = 'requests'

#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String())
#     params = db.Column(db.String())
#     result = db.Column(db.String())

#     def __init__(self, url, params, result, **kwargs):
#         self.url = url
#         self.params = params
#         self.result = result
#         super().__init__(**kwargs)

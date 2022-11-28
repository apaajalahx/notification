from app import db
from sqlalchemy.sql import func
from sqlalchemy.inspection import inspect
import json

class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    
    def serialize_list(l):
        return [m.serialize() for m in l]


class Notification(db.Model, Serializer):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                            server_default=func.now())
    
    def __init__(self, text=None, url=None):
        self.text = text
        self.url = url
    
    def get_notif():
        all = Notification.query.all()
        return json.loads(json.dumps(Notification.serialize_list(all), default=str))
    
    def single_notif(id):
        get = Notification.query.filter(Notification.id == id).first()
        return json.loads(json.dumps(Notification.serialize(get), default=str))
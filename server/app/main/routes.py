from . import main
from app.model import Notification
from webargs.flaskparser import use_args
from .params import CreateNotification
from app import db, socket
from flask_socketio import emit
from flask import jsonify

@main.route('/create', methods=['POST'])
@use_args(CreateNotification, location="json")
def create_notification(args):
    create = Notification(args["text"], args["url"])
    db.session.add_all([create])
    db.session.commit()
    socket.emit('single_notify', {'data':  Notification.single_notif(create.id)})
    return jsonify(Notification.single_notif(create.id))

# @main.route('/ping', methods=['GET'])
# def ping():
#     socket.emit('single_notify', {'data' : 'oke ping'})
#     return '', 200

@socket.on('get_notify')
def ReadNotification(msg):
    print(msg, 'oke')
    latest = Notification.get_notif()
    emit('mass_notify', {'data' : latest})
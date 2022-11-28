from app import db, init_app, socket
import os

app = init_app(os.getenv('ENV', default='production'))

@app.cli.command('migrate:fresh')
def migrate_fresh():
    """ Migration Fresh Database """
    with app.app_context():
        db.create_all()

@app.cli.command('migrate:drop')
def migrate_drop():
    """ Drop All Database """
    with app.app_context():
        db.drop_all()

if __name__ == '__main__':
   socket.run(app, port=int(os.getenv('PORT', default=8000)))
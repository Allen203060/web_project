# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_api.models import db, Notification, User, Movie  # Changed to absolute import
# from datetime import datetime
# import os

# app = Flask(__name__)

# # Configure Flask to use the same SQLite database as Django
# basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "db.sqlite3")}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy with the Flask app
# db.init_app(app)

# # Notification Endpoints
# @app.route('/api/notifications', methods=['GET'])
# def get_notifications():
#     user_id = request.args.get('user_id', type=int)
#     if not user_id:
#         return jsonify({'error': 'user_id is required'}), 400
#     notifications = Notification.query.filter_by(user_id=user_id, is_read=False).order_by(Notificationcreated_at.desc()).all()
#     return jsonify([{
#         'id': notification.id,
#         'user_id': notification.user_id,
#         'message': notification.message,
#         'created_at': notification.created_at.isoformat(),
#         'is_read': notification.is_read,
#         'related_movie_id': notification.related_movie_id,
#         'related_movie_title': notification.related_movie.title if notification.related_movie else None
#     } for notification in notifications])

# @app.route('/api/notifications/<int:id>', methods=['PUT'])
# def mark_notification_read(id):
#     notification = Notification.query.get_or_404(id)
#     data = request.get_json()
#     notification.is_read = data.get('is_read', notification.is_read)
#     db.session.commit()
#     return jsonify({
#         'id': notification.id,
#         'message': notification.message,
#         'is_read': notification.is_read
#     })

# @app.route('/api/notifications', methods=['POST'])
# def create_notification():
#     data = request.get_json()
#     if not data or not all(key in data for key in ['user_id', 'message']):
#         return jsonify({'error': 'Missing required fields'}), 400
#     if not User.query.get(data['user_id']):
#         return jsonify({'error': 'Invalid user_id'}), 400
#     notification = Notification(
#         user_id=data['user_id'],
#         message=data['message'],
#         created_at=datetime.utcnow(),
#         related_movie_id=data.get('related_movie_id')
#     )
#     db.session.add(notification)
#     db.session.commit()
#     return jsonify({
#         'id': notification.id,
#         'message': notification.message
#     }), 201

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sqlite3
# from datetime import datetime

# app = Flask(__name__)
# CORS(app)

# def get_db_connection():
#     conn = sqlite3.connect('notifications.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/api/notifications', methods=['GET'])
# def get_notifications():
#     user_id = request.args.get('user_id')
#     conn = get_db_connection()
#     notifications = conn.execute('SELECT * FROM notifications WHERE user_id = ? AND is_read = 0', (user_id,)).fetchall()
#     conn.close()
#     return jsonify([dict(n) for n in notifications])

# @app.route('/api/notifications', methods=['POST'])
# def create_notification():
#     data = request.get_json()
#     user_id = data.get('user_id')
#     message = data.get('message')
#     related_movie_id = data.get('related_movie_id')
    
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         'INSERT INTO notifications (user_id, message, related_movie_id, created_at, is_read) VALUES (?, ?, ?, ?, ?)',
#         (user_id, message, related_movie_id, datetime.utcnow().isoformat(), 0)
#     )
#     conn.commit()
#     notification_id = cursor.lastrowid
#     conn.close()
#     return jsonify({'id': notification_id, 'message': 'Notification created'}), 201

# @app.route('/api/notifications/<int:id>', methods=['PUT'])
# def update_notification(id):
#     data = request.get_json()
#     is_read = data.get('is_read')
    
#     conn = get_db_connection()
#     conn.execute('UPDATE notifications SET is_read = ? WHERE id = ?', (is_read, id))
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Notification updated'})

# # Add DELETE endpoint
# @app.route('/api/notifications/<int:id>', methods=['DELETE'])
# def delete_notification(id):
#     conn = get_db_connection()
#     conn.execute('DELETE FROM notifications WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Notification deleted'})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('notifications.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    notifications = conn.execute('SELECT * FROM notifications WHERE user_id = ? AND is_read = 0', (user_id,)).fetchall()
    conn.close()
    return jsonify([dict(n) for n in notifications])

@app.route('/api/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    related_movie_id = data.get('related_movie_id')
    is_admin = data.get('is_admin', False)
    is_system_generated = data.get('is_system_generated', False)

    if not (is_admin or is_system_generated):
        return jsonify({'error': 'Only admins or system actions can create notifications'}), 403
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO notifications (user_id, message, related_movie_id, created_at, is_read) VALUES (?, ?, ?, ?, ?)',
        (user_id, message, related_movie_id, datetime.utcnow().isoformat(), 0)
    )
    conn.commit()
    notification_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': notification_id, 'message': 'Notification created'}), 201

@app.route('/api/notifications/<int:id>', methods=['PUT'])
def update_notification(id):
    data = request.get_json()
    is_read = data.get('is_read')
    message = data.get('message')
    is_admin = data.get('is_admin', False)

    if message is not None and not is_admin:
        return jsonify({'error': 'Only admins can edit notification messages'}), 403

    conn = get_db_connection()
    if message is not None:
        conn.execute('UPDATE notifications SET message = ? WHERE id = ?', (message, id))
    if is_read is not None:
        conn.execute('UPDATE notifications SET is_read = ? WHERE id = ?', (is_read, id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Notification updated'})

@app.route('/api/notifications/<int:id>', methods=['DELETE'])
def delete_notification(id):
    data = request.get_json()
    is_admin = data.get('is_admin', False)

    if not is_admin:
        return jsonify({'error': 'Only admins can delete notifications'}), 403

    conn = get_db_connection()
    conn.execute('DELETE FROM notifications WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Notification deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
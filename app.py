from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visited_links.db'
db = SQLAlchemy(app)

class VisitedLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/visited_links', methods=['POST'])
def add_visited_links():
    try:
        data = request.get_json()
        links = data.get('links', [])

        for link in links:
            visited_link = VisitedLink(link=link)
            db.session.add(visited_link)

        db.session.commit()

        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        return jsonify({'status': str(e)}), 500

@app.route('/visited_domains', methods=['GET'])
def get_visited_domains():
    try:
        from_time = request.args.get('from')
        to_time = request.args.get('to')

        from_time = datetime.utcfromtimestamp(int(from_time))
        to_time = datetime.utcfromtimestamp(int(to_time))

        domains = list(set([link.link.split('//')[1].split('/')[0] for link in VisitedLink.query.filter(VisitedLink.timestamp.between(from_time, to_time)).all()]))

        return jsonify({'domains': domains, 'status': 'ok'}), 200
    except Exception as e:
        return jsonify({'status': str(e)}), 500

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


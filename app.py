from flask import Flask, jsonify, Blueprint
from deck import cards
import random, json, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

app = Flask(__name__)
api = Blueprint('api', __name__)


@app.route('/')
def ping():
    return cards

@app.route('/read/<int:draft>')
def draft(draft):
    pick = random.choices(cards['cards'], k=draft)
    final = jsonify(pick)
    return final
    
@app.route('/card/<int:id>') 
def card(id):
    for card in cards['cards']:
        if card['id'] == id:
            return card




if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='/api')
    app.run(debug=True)

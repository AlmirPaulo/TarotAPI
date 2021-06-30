from flask import Flask, jsonify, Blueprint
from deck import cards
import random, json, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

app = Flask(__name__)
api = Blueprint('api', __name__)
app.register_blueprint(api, url_prefix='/api')

@api.route('/')
def ping():
    return cards

@api.route('/read/<int:draft>')
def read(draft):
    if draft > 21:
        return 'Sorry, not enough cards...'
    pick = random.choices(cards['cards'], k=draft)
    final = jsonify(pick)
    return final
    
@api.route('/card/<int:id>') 
def card(id):
    for card in cards['cards']:
        if card['id'] == id:
            return card
    return 'Card not found.'




if __name__ == '__main__':
    app.run(debug=True)

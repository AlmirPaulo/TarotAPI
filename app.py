from flask import Flask, jsonify, Blueprint
from deck import cards
import random, json, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

app = Flask(__name__)
v1 = Blueprint('v1', __name__)

@v1.route('/')
def ping():
    return cards


@v1.route('/read_maj/<int:draft>')
def read_maj(draft):
    if draft > 21:
        return "Sorry, not cards enough."
    draft_cards = []
    while draft > 0:
        pick = random.randint(0, 21)
        for card in cards['cards']:
            if card['id'] == pick and card not in draft_cards:
                draft_cards.append(card)
                draft = draft - 1
            
    return jsonify(draft_cards)

# @v1.route('/read_min/<int:draft>')
# def read_min(draft):
#     if draft > 56:
#         return "Sorry, not cards enough."
#     draft_cards = []
#     while draft > 0:
#         pick = random.randint(22, 78)
#         for card in cards['cards']:
#             if card['id'] == pick and card not in draft_cards:
#                 draft_cards.append(card)
#                 draft = draft - 1
            
#     return jsonify(draft_cards)

@v1.route('/read_whole/<int:draft>')
def read_whole(draft):
    if draft > 21:
        return 'Sorry, not enough cards...'
    pick = random.choices(cards['cards'], k=draft)
    final = jsonify(pick)
    return final
    
@v1.route('/card/<int:id>') 
def card(id):
    for card in cards['cards']:
        if card['id'] == id:
            return card
    return 'Card not found.'


app.register_blueprint(v1, url_prefix='/v1')


if __name__ == '__main__':
    app.run(debug=True)

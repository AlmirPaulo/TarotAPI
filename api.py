from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from deck import cards
import uvicorn, random, logging


# logging.basicConfig(level=logging.INFO, filename='server.log',format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@api.get("/")
def full_deck():
    """
    Show all cards data.

    """
    logging.info("root")
    return cards


@api.get("/read_maj/{draft}")
def read_maj(draft: int):
    """
    Draft the determined number of cards randomly, considering only the major arcana.
    """
    if draft > 22:
        return "Sorry, not cards enough."
    draft_cards = []
    while draft > 0:
        pick = random.randint(0, 21)
        for card in cards["cards"]:
            if card["id"] == pick and card not in draft_cards:
                draft_cards.append(card)
                draft = draft - 1

    logging.info("read_maj")
    return draft_cards


# @api.get('/api/read_min/{draft}')
# def read_min(draft:int):
#     if draft > 56:
#         return "Sorry, not cards enough."
#     draft_cards = []
#     while draft > 0:
#         pick = random.randint(22, 78)
#         for card in cards['cards']:
#             if card['id'] == pick and card not in draft_cards:
#                 draft_cards.append(card)
#                 draft = draft - 1

#     return draft_cards


@api.get("/read_whole/{draft}")
def read_whole(draft: int):
    """
    Draft the determined number of cards randomly, considering the whole deck.
    """
    if draft > 22:
        return "Sorry, not enough cards..."
    pick = random.choices(cards["cards"], k=draft)
    logging.info("read_whole")
    return pick


@api.get("/card/{id}")
def card(id: int):
    """
    Show the selected card data (by id).
    """
    for card in cards["cards"]:
        if card["id"] == id:
            logging.info("card")
            return card

    logging.info("card")
    return "Card not found."


if __name__ == "__main__":
    uvicorn.run("api:api", reload=True)

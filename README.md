# TarotAPI v1
*A project by [Almir Paulo](https://almirpaulo.github.io/)*

![API Status](https://img.shields.io/website?down_color=red&down_message=Down%2C%20by%20now...&style=for-the-badge&up_color=green&up_message=UP%21&url=https%3A%2F%2Ftarotapi.almirpaulo.repl.co%2Fv1)

A RESTFul API to read tarot cards made in Python with Flask. 

The API can be accessed at:  
    
     https://TarotAPI.almirpaulo.repl.co/v1

## Endpoints

**Root Endpoint:** Show all cards data. 

    .../v1/

**Card Show Endpoint:** Show the selected card data (by id).

    .../v1/card/<id>

**Whole Deck Reading Endpoint:** Draft the determined number of cards randomly, considering the whole deck.

    .../v1/read_whole/<number>

<blockquote>By now we only have the Major Arcana. We will work on the minors soon!</blockquote>

**Major Arcana Reading Endpoint:** Draft the determined number of cards randomly, considering only the major arcana.
 
    .../v1/read_maj/<number>

<!--**Minor Arcana Reading Endpoint:** Draft the determined number of cards randomly, considering only the minor arcana.

    .../v1/read_min/<number>
-->
## Technologies

* Python
* Flask

## For Bug Reports

Please open an Issue.

## Future Plans

* Include the Minor Arcana
* Include other Images from other tarot decks like Marseilles, etc. 

## Contribute
If this project have helped you in some way to earn some money and you're wondering how to say "thank you", consider to buy me coffee! I would appreciate very much!
 
(Button here soon!)

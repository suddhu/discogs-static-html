# discogs-static-html

Simple and hacky way to display your vinyl collection on a static html page. Uses the official [Discogs API client for Python](https://github.com/discogs/discogs_client) to create a HTML + CSS webpage.

![Example](page/example.png "Static html")

## Setup

* ```sh $ pip3 install discogs_client```
* `pip install` all other dependencies found in `page/generate_collection.py`. 
* Add your personal user discogs token to a file `page/token.txt` ([refer](https://blog.discogs.com/en/api-update-discogs-auth/)).
* ```sh $ python generate_collection.py 1```
* ```sh $ python generate_collection.py 0```
* Open the html file generated: `collection.html`

The HTML will serve as a standalone webpage for your collection

## Todo 

[] Make grid adaptive to screen size (mobiles devices show single line)
[] Gray out images on hover 
[] Add links to releases 
[] Graphs and other viz.

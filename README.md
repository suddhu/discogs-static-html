# discogs-static-html

Simple and hacky way to display your vinyl collection on a static html page. Uses the official [I'm an inline-style link with title](https://github.com/discogs/discogs_client "Discogs API client for Python") to create a HTML + CSS webpage.

## Setup

```sh
$ pip3 install discogs_client
```

* `pip install` all other dependencies found in `page/generate_collection.py`. 
* Add your personal user discogs token to a file `page/token.txt` [refer](https://blog.discogs.com/en/api-update-discogs-auth/).
* ```sh $ python3 generate_collection.py 1```
* ```sh $ python3 generate_collection.py 0```
* Open the html file generated: `collection.html`

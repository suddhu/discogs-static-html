# generate static html file
import discogs_client as dc #discogs
import pdb
import pickle
from shutil import copyfile
from helpers import *
import operator
import sys

if len(sys.argv) > 1:
  pickling = int(sys.argv[1]) 
else:
  print("Not enough variables!\n")
  sys.exit()

#### PICKLING
if pickling == 1:
  print("Pickling...")
  
  # load token
  my_token = getToken()
  
  # define discogs client
  ds = dc.Client('ExampleApplication/0.1', user_token=my_token)
  me = ds.identity()
  all_folder = me.collection_folders[0] # The `All` folder is the 0th index in this list
  releases = all_folder.releases.page(1) + all_folder.releases.page(2) # get all the releases

  # loop through all the releases and add them to my data structure
  N = len(releases)
  my_vinyls = []
  for i in range(N): 
      print(i)
      _id = str(releases[i].release.id) # discogs ID
      _title = releases[i].release.title # release name
      _artist = releases[i].release.artists[0].name # artist name
      _artist = removeArticles(_artist) # get rid of 'the', 'a', 'an'
      
      # skip if no image available
      if releases[i].release.images == None: 
        continue
      
      _im_url = releases[i].release.images[0]["uri"] # image url
      my_vinyls.append(ReleaseItem(_id, _title, _artist, _im_url))

  my_vinyls.sort(key=operator.attrgetter('artist')) # sort alphabetically by artist
  
  # save to pickle
  with open('collection.pickle', 'wb') as handle:
    pickle.dump(my_vinyls, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
#### UNPICKLING and GENERATE HTML
else:
  print("Unpickling...")
  # load from pickle
  with open('collection.pickle', 'rb') as handle:
      my_vinyls = pickle.load(handle)

  # copy template code and open for appending
  copyfile("template.html", "collection.html")
  f = open('collection.html','a')
  
  # append first line stats
  f.write("\n")
  discogs_link = '  <a href="https://www.discogs.com/user/suddhus/collection?page=1&limit=250" target="_blank">My discogs collections page</a>'
  f.write('<p>Count: ' + str(len(my_vinyls)) + '&emsp; Last updated: ' + getDate() + '&emsp;' + discogs_link + '<br></p>')

  # write html code for each image
  for vinyl in my_vinyls:
      # get image
      img_tag = '<img src="' + vinyl.im_url + '" width="200" height="200">\n'
      f.write('<div class="zoom" style = "float:left;">')
      f.write('<div class="img__wrap">')
      f.write(img_tag)
      print(vinyl.title.encode('utf-8').upper())
      
      # add the hover text 
      f.write('<p class="artist_name">' + vinyl.artist.encode('utf-8').upper() + ': </p>')
      f.write('<p class="release_title">' + vinyl.title.encode('utf-8').upper() + '</p>')
      f.write('</div>')
      f.write('</div>\n')

  f.write('\n</body>\n</html>')
  f.close()
  
  print("Generated HTML!")



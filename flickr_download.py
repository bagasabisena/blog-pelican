import flickr_api
import json
import flickr_key

flickr_api.set_keys(api_key=flickr_key.key,
                    api_secret=flickr_key.secret)

user = flickr_api.Person.findByUserName('bagasabisena')
photos = user.getPublicPhotos()

base_dir = 'content/images/flickr/'
user_id = flickr_key.user_id
base_url = 'https://www.flickr.com/photos/%s/%s/'

photos_array = []

for p in photos.data:
    photo = {}
    photo['id'] = p.id
    photo['title'] = p.title
    photo['url'] = base_url % (user_id, p.id)
    photos_array.append(photo)
    p.save(base_dir + p.id + '.jpg', size_label='Medium')

with open(base_dir + 'photos.json', 'w') as f:
    json.dump(photos_array, f)

from mongoengine import *

connect('FlaskUrlShorter')

def databaseController(shortUrl):
    total = len(Url.objects)
    a = len(Url.objects(shortedUrl__ne=shortUrl))
    if total == a:
        return True
    else:
        return False
    
    
def getUrl(data):
    url = []
    for i in data:
        mydict = {'shorturl':i.shortedUrl,'url':i.url}
        url.append(mydict)
    return url



class Url(Document):
    url = StringField(required=True)
    shortedUrl = StringField(required=True)
    



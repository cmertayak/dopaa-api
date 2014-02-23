import urllib2
import json
from api.models import Product
from django.db.utils import IntegrityError

opener = urllib2.build_opener(urllib2.HTTPHandler);

def collect(id):
    print "collecting product id: %d" % id
    
    url = "http://api.macys.com/v3/catalog/product/%d?imagewidth=200" % id
    request = urllib2.Request(url)
    request.add_header('X-Macys-Webservice-Client-Id', 'hackathon')
    request.add_header('Accept', 'application/json')
    data = opener.open(request).read()
    obj = json.loads(data)
    obj = obj['product'][0]
    
    try:
        if 'current' in obj['price']:
            currentPrice = obj['price']['current']['value']
        elif 'sale' in obj['price']:
            currentPrice = obj['price']['sale']['value']
        elif 'regular' in obj['price']:
            currentPrice = obj['price']['regular']['value']
        elif 'original' in obj['price']:
            currentPrice = obj['price']['regular']['value']
        
        product = Product(store_id = obj['id'],
                          title = obj['summary']['name'],
                          desc = obj['summary']['description'],
                          sizes = obj['SizeMap'],
                          colors = obj['colorMap'],
                          images = obj['image'],
                          price = currentPrice,
                          instore_eligible = obj['availability']['instoreeligible'] != 'false'
                          )
        product.save()
    except KeyError as e:
        print e
        print "KeyError passing %d" % id
        return
    
    print "done"
    
    
def init_some_prods():
    ids = ["97171", "97172", "99521", "101262", "101343", "107967", "107968", "110417", "134729", "134871", "153449", "153450", "153453", "156331", "156889", "159815", "166725", "166726", "178922", "180784", "181718", "192192", "198750", "199234", "200483", "200485", "200490", "200491", "207352", "207353", "216953", "218287", "223193", "224139", "224140", "224151", "224152", "224153", "224156", "226930", "227262", "229581", "235665", "241631", "245982", "246498", "246545"]
    
    for id in ids:
        try:
            collect(int(id))
        except IntegrityError:
            print 'IntegrityError passing %s' % id

def correct_fields():
    products = Product.objects.all()

    for product in products:
        product.sizes = product.sizes.replace("'", '"')
        product.save()
            
def run():
    #print "done"
    #return
    correct_fields()


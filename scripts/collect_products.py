import urllib2
import json
from api.models import Product
from django.db.utils import IntegrityError
import time

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
        elif 'everydayvalue' in obj['price']:
            currentPrice = obj['price']['everydayvalue']['value']
        
        product = Product(store_id = obj['id'],
                          title = obj['summary']['name'],
                          desc = obj['summary']['description'],
                          sizes = json.dumps(obj['SizeMap']),
                          colors = json.dumps(obj['colorMap']),
                          images = json.dumps(obj['image']),
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
    ids = ["1412803", "1413432", "1413434", "1413831", "1413843", "1414752", "1414764", "1414769", "1414775", "1414787", "1414813", "1414834", "1414848", "1414856", "1414858", "1414863", "1414873", "1414878", "1414893", "1414905", "1415116", "1415127", "1415137", "1415145", "1415269", "1415275", "1415277", "1415336"]
    
    for id in ids:
        try:
            collect(int(id))
            time.sleep(0.5) 
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
    init_some_prods()


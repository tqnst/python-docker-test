from flask import Flask
from redis import Redis
from redis.sentinel import Sentinel
#import redis

application = Flask(__name__)
#r = redis.StrictRedis(host='54.178.186.218', password='Admin123', port=6379, db=0)
#print "r= " + r.get('test')
sentinel = Sentinel([('54.178.186.218', 26379), ('52.199.211.78', 26379), ('13.231.104.253', 26379)], password='Admin123', socket_timeout=0.1)
m = sentinel.discover_master('mymaster')
s = sentinel.discover_slaves('mymaster')
print "m =====> " + str(m)
print "s =====> " + str(s)
master = sentinel.master_for('mymaster', socket_timeout=0.1)
print "master  ======> " + str(master)
slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
print "slave  ======> " + str(slave)

@application.route("/")
def hello():
    count = int(master.get('test_count'))
    master.set('test_count', str(count + 1))
    print 'count = ' + str(count)
    return "<h1 style='color:red'>Hello World!</h1><br/>" + str(count + 1)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
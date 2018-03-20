from flask import Flask
from redis import Redis
from redis.sentinel import Sentinel

application = Flask(__name__)

sentinel = Sentinel([('54.178.186.218', 26379), ('52.199.211.78', 26379), ('13.231.104.253', 26379)], socket_timeout=0.1)
sentinel.discover_master('mymaster')
setinel.discover_slaves('mymaster')
master = sentinel.master_for('mymaster', socket_timeout=0.1)
slave = sentinel.salve_for('mymaster', socket_timeout=0.1)

@application.route("/")
def hello():
    count = master.get('test_count')
    print 'count = ' + str(count)
    master.set('test_count', count + 1)
    return "<h1 style='color:red'>Hello World!</h1><br/>" + str(count)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
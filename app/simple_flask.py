from flask import Flask
from redis import Redis
application = Flask(__name__)
redis = Redis(host='redis', port=6379)

@application.route("/")
def hello():
    count = redis.incr('hits')
    return "<h1 style='color:red'>Hello World!</h1><br/>" + str(count)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
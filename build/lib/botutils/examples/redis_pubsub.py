from multiprocessing import Process
import redis
import time

redis_url = 'redis://localhost:6379'
channel = "test_channel"

def send_redis():
    r = redis.from_url(redis_url)

    time.sleep(5)
    count = 0
    print "starting to publish"
    while True:
        dictionary = {'foo': 'bar', 'count': count}
        r.publish(channel, dictionary)
        count += 1
        print "published: %s" % dictionary
        time.sleep(2)
        if count > 5:
            break

def receive_redis():
    r = redis.from_url(redis_url)
    p = r.pubsub(ignore_subscribe_messages=True)

    print "Recive subscribing"
    p.subscribe(channel)

    print "Listening"
    for message in p.listen():
        print "Message: ", message
        print 'MY HANDLER: ', message['data']
        time.sleep(5)


if __name__ == "__main__":

    p1 = Process(target=send_redis)
    p2 = Process(target=receive_redis)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
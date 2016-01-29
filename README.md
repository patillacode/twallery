# twallery

Tweet a picture with a given hashtag -  find it in your private Twallery

### Dataflow:

tweet -> listener -> redis -> website

------------

### Install
`$ git clone https://github.com/patillacode/twallery.git`
`$ mkvirtualenv twallery`

#### Node environment and packages
```
    $ pip install nodeenv
    $ npm install
```

#### Redis

[Here](http://redis.io/topics/quickstart) is the official documentation

[This](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis) is also a nice tutorial

Summary:

```
    $ wget http://download.redis.io/redis-stable.tar.gz # download redis
    $ tar xvzf redis-stable.tar.gz                      # uncompress it
    $ cd redis-stable                                   # move into the uncompressed folder
    $ make                                              # install
    $ make test                                         # run tests
    $ sudo cp src/redis-server /usr/local/bin/          # copy server command into your environment
    $ sudo cp src/redis-cli /usr/local/bin/             # copy client command into your environment
```

#### Python

`$ pip install -r requirements.txt`

Remember for the twitter listener to create a `keys.py` file in `src/python/listener` like this:

```
ACCESS_TOKEN = "YOUR ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR ACCESS_TOKEN_SECRET"
CONSUMER_KEY = "YOUR CONSUMER_KEY"
CONSUMER_SECRET = "YOUR CONSUMER_SECRET"
```
To get your keys take a look [here](https://apps.twitter.com/)

------------

### Run

#### Redis
`$ redis-server`

##### Node

```
    $ cd src/node
    $ DEBUG=socket.io* node server.js
```

#### Python

##### Webserver
```
    $ cd src/python/webserver
    $ python server.py



    usage: server.py [-h] [--host HOST] [--port PORT]

    optional arguments:
      -h, --help   show this help message and exit
      --host HOST  IP to run on [default: 127.0.0.1]
      --port PORT  port to listen to [default: 8080
```

##### Twitter Listener
```
    $ cd src/python/listener
    $ python listener.py --hashtags ht1 ht2 hst3 ... htN



    usage: listener.py [-h] --hashtags [HASHTAGS [HASHTAGS ...]]

    optional arguments:
      -h, --help            show this help message and exit

    mandatory arguments:
      --hashtags [HASHTAGS [HASHTAGS ...]]
```

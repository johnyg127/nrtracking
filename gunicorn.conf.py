bind = '0.0.0.0:8000'
workers = 5
worker_class = 'gevent'
worker_connections = 1000
keepalive = 5

keyfile = '/etc/letsencrypt/live/backend.nerdrebel.xyz/privkey.pem'
certfile = '/etc/letsencrypt/live/backend.nerdrebel.xyz/cert.pem'
ca_certs = '/etc/letsencrypt/live/backend.nerdrebel.xyz/chain.pem'
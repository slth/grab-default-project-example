from grab import Grab

g = Grab(log_file='out.html')
g.setup(proxy='127.0.0.1:6588', proxy_type='http')
g.go('http://localhost')



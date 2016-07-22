from grab import Grab

g = Grab(log_file='out.html')
g.setup(proxy='localhost:6588', proxy_type='http')

g.go('http://localhost/blog/')



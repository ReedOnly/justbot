from urllib2 import Request, urlopen
request = Request("https://justcoin.apiary-mock.com/api/v1/markets/{id}/depth")
response_body = urlopen(request).read()
print response_body

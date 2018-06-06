import urllib.request
'''
req = urllib.request.Request(url='http://localhost:8000/api/fake_chart_data', method='GET')
'''
req = urllib.request.Request(url='http://54.238.157.69/api/fake_chart_data', method='GET')
response = urllib.request.urlopen(req)  
print(response.read().decode("utf-8"))
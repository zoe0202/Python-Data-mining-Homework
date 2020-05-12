import re
import urllib.request
response = urllib.request.urlopen("http://www.cuc.edu.cn")
html = str(response.read())
result = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',html)
print(result)
import json
import re
numbers = [1, 3, 5, 7, 11]
filename = "numbers.json"
with open(filename, 'w') as file_obj:
  json.dump(numbers, file_obj)

  #这个代码来源于网络，看了教程后感觉自己没办法单独写出这个代码

import requests

url = 'https://api.ownthink.com/kg/knowledge?entity=苹果'      # 知识图谱API
sess = requests.get(url) # 请求

text = sess.text # 获取返回的数据
print(text) 

knowledge = eval(text) # 转为字典类型
print(knowledge)
print(knowledge['data']['avp']) # 打印avp







import requests

url = 'https://api.ownthink.com/kg/knowledge?entity=苹果'
sess = requests.get(url)

text = sess.text
print(text)

knowledge = eval(text)
print(knowledge)
print(knowledge['data']['avp'])

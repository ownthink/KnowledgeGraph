'''
 * Copyright (C) 2017 OwnThink Technologies Inc. 
 *
 * Name        : knowledgegraph.py - 知识图谱
 * Author      : Yener <yener@ownthink.com>
 * Version     : 0.01
 * Description : 知识图谱api请求示范
'''
import requests

def mention2entity(mention):
	'''
	 * mention2entity - 提及->实体
	 * @mention: [in]提及
	 * 根据提及获取歧义关系
	'''
	url = 'https://api.ownthink.com/kg/ambiguous?mention={mention}'.format(mention=mention)      # 知识图谱API，歧义关系
	sess = requests.get(url) # 请求
	text = sess.text # 获取返回的数据
	entitys = eval(text) # 转为字典类型
	return entitys
	
def entity2knowledge(entity):
	'''
	 * entity2knowledge - 实体->知识
	 * @entity: [in]实体名
	 * 根据实体获取实体知识
	'''
	url = 'https://api.ownthink.com/kg/knowledge?entity={entity}'.format(entity=entity)      # 知识图谱API，实体知识
	sess = requests.get(url) # 请求
	text = sess.text # 获取返回的数据
	knowledge = eval(text) # 转为字典类型
	return knowledge

def entity_attribute2value(entity, attribute):
	'''
	 * entity_attribute2value - 实体&属性->属性值
	 * @entity: 	[in]实体名
	 * @attribute:	[in]属性名
	 * 根据实体、属性获取属性值
	'''
	url = 'https://api.ownthink.com/kg/eav?entity={entity}&attribute={attribute}'.format(entity=entity, attribute=attribute)      # 知识图谱API，属性值
	sess = requests.get(url) # 请求
	text = sess.text # 获取返回的数据
	values = eval(text) # 转为字典类型
	return values

if __name__=='__main__':
	mention = '红楼梦'
	entitys = mention2entity(mention)
	print(entitys)
	
	entity = '刘德华'
	knowledge = entity2knowledge(entity)#根据实体获取知识
	print(knowledge)
	
	entity = '苹果'
	attribute = '颜色'
	values = entity_attribute2value(entity, attribute)
	print(values)
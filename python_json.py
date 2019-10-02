import json
input = '''[
	{
		"id":"001",
		"x":"2",
		"name":"Chuck"
	},
	{
		"id":"009",
		"x":"7",
		"name":"Chuck"
	}]'''
info = json.loads(input)
print("Usercount : ", len(info))
for item in info:
	print("Name : {0}".format(item['name']))
	print("Id : {0}".format(item['id']))
	print("Name : {0}".format(item['x']))

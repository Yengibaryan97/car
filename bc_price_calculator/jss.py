import json

t_jss = '''{
"demo" : "hello",
"instructor" : "Anna",
"grade" : 5.0
}'''

print(type(t_jss), t_jss)

data = json.loads(t_jss)
print(type(data),data)

instructor = data["instructor"]
data["instructor"] = "jeff"
new_json = json.dumps(data)
print(type(new_json),new_json)
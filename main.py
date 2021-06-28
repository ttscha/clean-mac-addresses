list1 = ["D46A91E24351","00:04:A5:0C:6A:28"]

response = []

for raw_item in list1:
	item = raw_item.strip()
	temp = ""
	if len(item) == 12:
		temp = item[0:2] + ":" + item[2:4] + ":" + item[4:6] + ":" +item[6:8] + ":" +item[8:10] + ":" +item[10:12]
		print(temp)
		response.append(temp)
	elif item[2] == "-":
		new_item = item.split("-")
		temp = new_item[0] + ":" + new_item[1] + ":" + new_item[2] + ":" + new_item[3] + ":" + new_item[4] + ":" + new_item[5]
		print(temp)
		response.append(temp)
	else:
		print(item)
		response.append(item)

print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)


for i in response:
	print(i)
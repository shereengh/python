Glist = []
item = {}
item["name"] = input("item (enter 'done' when finished):")
while item["name"] != "done":
	item["price"] = input("price: ")
	item["quantity"] = input("quantity: ")
	Glist.append(item)
	item = {}
	item["name"] = input("item (enter 'done' when finished):")

print("-" * 20)
print("receipt")
print("-" * 20)

sum = 0
for i in Glist:
	temp = float(i["price"]) * int(i["quantity"])
	print(i["quantity"], i["name"], str(format(temp, '.3f'))+"KD")
	sum += temp

print("-" * 20)
print("total: "+ str(format(sum, '.3f'))+"KD")
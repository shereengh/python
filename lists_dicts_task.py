skills = ["python", "c++", "javascript", "juggling", "running", "eating"]
cv = {}

print("Welcome to the special recruitment program, please answer the following questions:")
cv["name"] = input("name: ")
cv["age"] = input("age: ")
cv["experience"] = input("how many years of experience do you have? ")
cv["skills"] = []
num = 1
for item in skills:
	print(str(num) + "-", item)
	num+=1

skill1 = input("choose a skill from above: ")
skill2 = input("choose another skill from above: ")
cv["skills"]=skills[int(skill1)-1]
cv["skills"]=skills.append(int(skill2)-1)

b= False
c= False

if int(skill1) == 1 or int(skill1) == 2:
	b= True
if int(skill2) == 1 or int(skill2) == 2:
	c= True
if (b or c) and int(cv["age"]) >= 20 and int(cv["age"])<=40 and int(cv["experience"]) >= 1:
	print("you have been accepted, {}".format(cv["name"]))
else:
	print("Sorry, you have not been accepted, {}".format(cv["name"]))
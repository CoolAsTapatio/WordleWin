lines = []
with open("sgb-words.txt", "r") as grilled_cheese:
	lines = grilled_cheese.readlines()
#	print(lines)
for idx, ele in enumerate(lines):
	lines[idx] = ele.replace("\n", "")
 
# printing result
print("The list after removal of character : " + str(lines))
path = input().split(".")
extension = path[-1]
file = path[0].split("\\")[-1]

print(f"File name: {file}")
print(f"File extension: {extension}")

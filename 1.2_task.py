ans = {id(objects[0])}
for i in range(1, len(objects)):
    if objects[0] is not objects[i]:
        ans.add(id(objects[i]))
print(len(ans))
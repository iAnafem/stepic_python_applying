import csv
result = {}
with open("Crimes.csv") as f:
    for i in csv.reader(f):
        if str(2015) in i[2]:
            if i[5] not in result:
                result[i[5]] = 1
            else:
                result[i[5]] += 1
print(max(result, key=result.get), )

import datetime

result = datetime.date(*[int(num) for num in input().split()]) + datetime.timedelta(int(input()))
print(result.year, result.month, result.day)


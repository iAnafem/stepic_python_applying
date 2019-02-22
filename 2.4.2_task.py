import os.path

with open("lol.txt", "w") as a:
    result = []
    os.chdir("main\\")
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if file.endswith(".py"):
                if current_dir not in result:
                    result.append("".join(current_dir))
    for _str in sorted(result):
        a.write(_str + "\n")

with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            f.write('{}\n'.format(current_dir))




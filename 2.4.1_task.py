with open("D:\\Книги\\dataset_24465_4.txt", "r") as r:
    with open("D:\\Книги\\lol.txt", "a") as w:
        w.write("\n".join(reversed(r.read().splitlines())))

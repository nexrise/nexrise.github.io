class Format:
    def __init__(self, filename):
        self.filename = filename

    def myfunc(self):
        index = open(self.filename, "r", encoding='utf-8')
        txt = index.read()
        index.close()

        x = txt.split("<!-- head -->")
        y = txt.split("<!-- endhead -->")

        head = open("head.html", "r", encoding='utf-8')
        headText = head.read()
        textJoin1 = str(x[0]) + str(headText) + str(y[1])

        x = textJoin1.split("<!-- header -->")
        y = textJoin1.split("<!-- endheader -->")

        header = open("header.html", "r", encoding='utf-8')
        headerText = header.read()
        textJoin2 = str(x[0]) + str(headerText) + str(y[1])

        x = textJoin2.split("<!-- footer -->")
        y = textJoin2.split("<!-- endfooter -->")

        footer = open("footer.html", "r", encoding='utf-8')
        footerText = footer.read()
        textJoin3 = str(x[0]) + str(footerText) + str(y[1])

        index = open(self.filename, "w", encoding='utf-8')
        index.write(textJoin3)
        index.close()


from os import listdir
from os.path import isfile, join


print("Writing header navbar and footer in all files")
navs = [f for f in listdir("../") if isfile(join("../", f))]
for x in navs:
    f1 = Format("../" + x)
    f1.myfunc()
    print(x)
print("Done")

events = [f for f in listdir("../events/") if isfile(join("../events/", f))]
for x in events:
    f1 = Format("../events/" + x)
    f1.myfunc()
    print(x)
print("Done")

print("Completed (2/2)")

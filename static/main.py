navlist = []
appEvent = []

class Events:
    def __init__(self, name, slug, date):
        self.name = name
        self.slug = slug
        self.date = date

    def myfunc(self):
        try:
            txt = open("../events/" + self.slug + ".html", "x", encoding='utf-8')

            eventFormat = open("format.html", "r", encoding='utf-8')
            eventTxt = eventFormat.read()
            eventFormat.close()
            
            txt.write(eventTxt)
            txt.close()
            
            print(x + 1, ". ", self.name, "[File created in Events]")
        except:
            print(x + 1, ". ", self.name, "[File already exists in Events]")

        nav = "<a class='dropdown-item' role='presentation' href='/events/" + self.slug + ".html'>" + self.name + "</a>\n"
        navlist.append(nav)

        eventpage = "<div class='card'>\n\t<div class='card-header bg-dark' role='tab'>\n\t\t<h5 class='mb-0'><a class='text-white' data-toggle='collapse'aria-expanded='false' aria-controls='accordion-1 .item-" + str(x + 1) + "' href='#accordion-1 .item-" + str(x + 1) + "'>" + self.name + "</a></h5>\n\t</div>\n\t<div class='collapse item-" + str(x + 1) + "' role='tabpanel' data-parent='#accordion-1'>\n\t\t<div class='card-body'>\n\t\t\t<p class='card-text'>" + self.date + "</p>\n\t\t\t<p class='card-text'></p>\n\t\t\t<button type='button' class='btn btn-primary'><a class='text-white' href='/events/" + self.slug + ".html'>Click Here</a></button>\n\t\t</div>\n\t</div>\n</div>\n\n"
        appEvent.append(eventpage)


print("Started...")

import event as ev

x = 0
for i in ev.Event:
    event = Events(ev.Event[x][0],ev.Event[x][1],ev.Event[x][2])
    event.myfunc()
    x += 1




## WRITE NAV EVENTS ##
print("drafting Nav Events...")
eventList = open("header.html", "r", encoding='utf-8')
txt = eventList.read()
eventList.close()

x = txt.split("<!-- events -->")
y = txt.split("<!-- endevents -->")

eNav = ""
for item in navlist:
    eNav += item

textJoin = str(x[0]) + "<!-- events -->\n\n"  + str(eNav) + "\n\n<!-- endevents -->" + str(y[1])
print("Writing Nav Events...")
eventList = open("header.html", "w", encoding='utf-8')
eventList.write(textJoin)
eventList.close()

## WRITE EVENT PAGE ##
print("drafting Event page...")
epage = open("../events.html", "r", encoding='utf-8')
txt = epage.read()
epage.close()

x = txt.split("<!-- eventpage -->")
y = txt.split("<!-- endeventpage -->")

eEvt = ""
for itemE in appEvent:
    eEvt += itemE

textJoin = str(x[0]) + "<!-- eventpage -->\n\n" + str(eEvt) + "<!-- endeventpage -->" + str(y[1])
print("Writing Event page...")
epage = open("../events.html", "w", encoding='utf-8')
epage.write(textJoin)
epage.close()

print("Completed (1/2)...")

import run


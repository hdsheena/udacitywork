"""

class Courtenay:
    def __init__(self, status):
        # tell courtenay what she is doing
        print "__init__ status is: " + status

        # just setup a default value i guess
        self.status = "pooping"
        print "self.status is: " + self.status
        
        # now set the value on this object
        print "about to set the status on self in __init__"
        self.status = status
        print "self.status is now: " + self.status

    def reset(self, status2):
        self.status = status2

    def pretty_printer(self):
        print "Courtenay is " + self.status

statuses = ["urinating"]

print "begin the shame machine"

for status in statuses:
    cw = Courtenay(status)
    cw.status = "uriting"
    cw.pretty_printer()
print "@@@@@@@@@@@@@@@@@@@@@@@"
cw001 = Courtenay("swallowing")
cw001.pretty_printer()

cw002 = Courtenay("jerking it? dunno")
cw002.pretty_printer() # <----- cw002 is definitely not cw001

print "all done"

"""

class Courtenay:
    def __init__(self, input_age):
        self.age = input_age

    def age_inquiry(self):
        print "I am " + str(self.age) + " years old."

cw001 = Courtenay(15)
cw001.age_inquiry()
Courtenay.age_inquiry(cw001)

cw002 = Courtenay(20)
cw002.age_inquiry()
Courtenay.age_inquiry(cw002)

Courtenay(16).age_inquiry()

print "$$$$$$$$$$$"
help(cw001)
print "$$$$$$$$$$$"
#dir(cw001)


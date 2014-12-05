__author__ = 'style'

blackColor = "black"
redColor = "red"
greenColor = "green"
yellowColor = "yellow"
blueColor = "blue"
aubergineColor = "Aubergine"
caynColor = "cayn"
whiteColor = "white"
defualColor = "defual"

defualModel = 0
heightLightModel = 1
underlineModel = 4
blinkModel = 5
inverseModel = 7
invisibleModel = 8

class terminalColor(object):
    def __init__(self):
        self.fontColorDict = {"black":30,"red":31,"green":32,"yellow":33,"blue":34,"aubergine":35,"cayn":36,"white":37,"defual":38}
        self.backgroundColorDict = {"black":40,"red":41,"green":42,"yellow":43,"blue":44,"aubergine":45,"cayn":46,"white":47,"defual":48}
        self.displayModel = defualModel
        self.fontColor = defualColor
        self.backgroundColor = defualColor
    def start(self):
        str = '\033[%d;%d;%dm' % (int(self.displayModel), int(self.fontColorDict[self.fontColor]),int(self.backgroundColorDict[self.backgroundColor]))
        print str
    def end(self):
        print '\033[0m'


a = terminalColor()
# a.fontColor = greenColor
# a.backgroundColor = blackColor
# a.displayModel = inverseModel
a.start()
print '*' * 10
print "hello world"
print '*' * 10
a.end()

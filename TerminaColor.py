__author__ = 'style'

blackColor = "black"
redColor = "red"
greenColor = "green"
yellowColor = "yellow"
blueColor = "blue"
aubergineColor = "Aubergine"
caynColor = "cayn"
whiteColor = "white"

defualModel = 0
heightLightModel = 1
underlineModel = 4
blinkModel = 5
inverseModel = 7
unSeeModel = 8

class terminalColor(object):
    def __init__(self):
        self.fontColorDict = {"black":30,"red":31,"green":32,"yellow":33,"blue":34,"aubergineColor":35,"caynColor":36,"whiteColor":37}
        self.backgroundColorDict = {"black":40,"red":41,"green":42,"yellow":43,"blue":44,"aubergineColor":45,"caynColor":46,"whiteColor":47}
        self.displayModel = defualModel
        self.fontColor = blackColor
        self.backgroundColor = whiteColor
    def start(self):
        str = '\033[%d;%d;%dm' % (int(self.displayModel), int(self.fontColorDict[self.fontColor]),int(self.backgroundColorDict[self.backgroundColor]))
        print str
    def end(self):
        print '\033[1;31;40m'


a = terminalColor()
a.fontColor = greenColor
a.backgroundColor = blackColor
a.start()
print '*' * 10
print "hello world"
print '*' * 10
a.end()

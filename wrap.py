import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Text Wrapping Func Test")
displaySurface = pygame.display.set_mode((600, 400), 0)

FPS = 30
fpsClock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)
blue = pygame.Color(0, 0, 255)

myFont = pygame.font.SysFont("Cambria", 12)

displaySurface.fill(blue)

#draw some wrapped text
#surface => surface onto which to draw the text
#rectCoords => tuple (length 4) specifying the text bound
#text => text to draw
#font => font to render the text in
#textColour => colour in which to render the text
#center => bool => aligment to use (false => left; true => center)
def wrapText(surface, rectCoords, text, font, textColour, center=False):
  rect = pygame.Rect(rectCoords) #create a rect object from the coordinates
  lineHeight = font.get_height() #get the height of a single line of text
  lineWidth = 0 #the current line width is 0 as there is no text in the current line
  lineNumber = 0 #the current line is the 0th line
  line = "" #the current line has no content
  
  #get each line one at a time
  for escapeLine in text.split("\n"):
    curLine = escapeLine.split(" ") #get a list of each word in the line
    if len(curLine) == 0: #if there are no words in the current line ie "\n\n" draw a blank space on the current line
      curLine = [" "]
    for word in curLine: #get each woord in the curent line one at a time
      #font.size(word + " ")[0] returns the size of the as a tuple (x, y) and get the x size
      #add the x size to the width of the line and check it is less than or equal to the width of the coordinates specified
      #check if when the word is added to the line the line will still fit in the coordinates specified
      if lineWidth + font.size(word + " ")[0] <= rect.width:
        line += word + " " #add the word to the line together with a space
        lineWidth += font.size(word + " ")[0] #add the size of the word plus a space to the line width
        if word != curLine[-1]: #process the next word if the word is not the last word in the current line
          continue
      
      #if the word will not fit on the line or the word is the last word in the current line then render the line
      if lineWidth + font.size(word + " ")[0] > rect.width or word == curLine[-1]:
        fontSurface = font.render(line, True, textColour) #render the text and get the surface object returned by this function
        fontRect = fontSurface.get_rect() #get the coordinates of the text surface
        if center:
          #align the text centrally
          #rect.top + lineNumber * lineHeight get the y coord of the top of the line of text
          fontRect.midtop = (rect.centerx, rect.top + lineNumber * lineHeight)
        else:
          #align the text to the left
          fontRect.topleft = (rect.left, rect.top + lineNumber * lineHeight)
        surface.blit(fontSurface, fontRect) #place the text surface onto the surface we are drawing onto at the coordinates given in fontRect
        lineNumber += 1 #increment the lineNumber
        line = word + " " #add the word plus a space to the current line
        lineWidth = font.size(word + " ")[0] #set the width of the line to the width of the word
        
        if lineNumber * lineHeight > rect.height: #if the next line will not fit in the space provided don't process any more words
          break
          
    if lineNumber * lineHeight > rect.height: #if breaking break out of both loops
      break

wrapText(displaySurface, (0, 0, 600, 400), "Good Afternoon, I am writing some long text to test my text wrapping functionGood Afternoon, I am writing some long text to test my text wrapping functionGood Afternoon, I am writing some long text to test my text wrapping functionGood Afternoon, I am writing some long text to test my text wrapping functionGood Afternoon, I am writing some long text to test my text wrapping function", myFont, black, True)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
  
  #MainLoop Code
  
  pygame.display.update()
  fpsClock.tick(FPS)
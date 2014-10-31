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

def wrapText(text, rectCoords, font, colour):
  global displaySurface
  rect = pygame.Rect(rectCoords) #create a rect object from the coordinates
  lineHeight = font.get_height() #getthe height of a single line of text
  lineWidth = 0 #the current line width is 0 as there is no text in the current line
  lineNumber = 0
  line = ""
  
  #get each word one at a time
  for escapeLine in text.split("\n"):
    for word in escapeLine.split(" "):
      if lineWidth + font.size(word + " ")[0] <= rect.width: #check if adding the word to the line will result in the line not fitting in the coordiates specified
        line += word + " "
        lineWidth += font.size(word + " ")[0]
      
      if lineWidth + font.size(word + " ")[0] > rect.width or word == text.split(" ")[-1]:
        fontSurface = font.render(line, True, colour)
        fontRect = fontSurface.get_rect()
        fontRect.midtop = (rect.centerx, rect.top + lineNumber * lineHeight)
        displaySurface.blit(fontSurface, fontRect)
        lineNumber += 1
        lineWidth = 0
        line = ""
        
        if lineNumber * lineHeight > rect.height: #if the next line will not fit in the space provided don't process any more words
          break
          
    if lineNumber * lineHeight > rect.height: #if breaking break out of both loops
      break
        
    if line != "":
      fontSurface = font.render(line, True, colour)
      fontRect = fontSurface.get_rect()
      fontRect.midtop = (rect.centerx, rect.top + lineNumber * lineHeight)
      displaySurface.blit(fontSurface, fontRect)
      lineNumber += 1
      lineWidth = 0
      line = ""

wrapText("Good Afternoon, I am writing some long text to test my text wrapping function\n\n Good Afternoon, I am writing some long text to test my text wrapping function\n Good Afternoon, I am writing some long text to test my text wrapping function\n Good Afternoon, I am writing some long text to test my text wrapping function\n Good Afternoon, I am writing some long text to test my text wrapping function", (0, 0, 600, 400), myFont, black)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
  
  #MainLoop Code
  
  pygame.display.update()
  fpsClock.tick(FPS)
from tkinter import filedialog, Tk
from os.path import expanduser

root = Tk()
root.withdraw()

filepath = filedialog.askopenfilename(title="Open File", initialdir=expanduser("~"), filetypes=[])

with open(filepath) as file:
  newLines = []
  for line in file:
    newLines.append("")
    i = 0
    while i < len(line):
      if line[i] == "\t":
        newLines[-1] += "  "
        i += 1
      elif line[i:i+4] == "    ":
        newLines[-1] += "  "
        i += 4
      else:
        newLines[-1] += line[i:-1]
        break
        
with open(filepath, "w") as file:
  file.write("\n".join(newLines))

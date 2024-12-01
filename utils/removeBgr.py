
from rembg import remove as rm
from PIL import Image
class rm1:
    def __init__(self, inputPath, outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath
    def run(self):
        input1 = Image.open(self.inputPath)
        output1 = rm(input1)
        output1.save(self.outputPath, format='PNG')




import json

class File:

    def __init__(self, fileLocation):
        self.file = open(fileLocation)

    def readLine(self):
        while True:
            record = self.file.readline()
            if not record:
                self.file.close()
                yield None
                break
            yield record

            
class JsonTextFile(File):
    
    def __init__(self, fileLocation):
        super().__init__(fileLocation)

    def readJsonTextLine(self):
        for line in self.readLine():
            if line:
                yield json.loads(line)



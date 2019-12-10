import os

class SolutionFinder:
    def __init__(self, directory):
        self.directory = directory
        self.__Solutions = None

    @property
    def Solutions(self):
        if self.__Solutions is None:
            self.__Solutions = self.__Find()
        return self.__Solutions

    def __Find(self):
        self.__Solutions = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".sln"):
                    path = os.path.join(root,file)
                    yield path
class DB():
    def __init__(self):
        self.db = []

    def AddSample(self, sample):
        self.db.append(sample)

    def GetSampleByName(self, name):
        for sample in self.db:
            if sample.name == name:
                return sample
        return None

    def RemoveSample(self, sample):
        self.db.remove(sample)

    def RemoveSampleByName(self, name):
        for sample in self.db:
            if sample.name == name:
                self.db.remove(sample)
                return True
        return False

    def RemoveSampleByOriginalPath(self, path):
        for sample in self.db:
            if sample.original_path == path:
                self.db.remove(sample)
                return True
        return False

    def IsInDB(self, sample):
        return sample in self.db

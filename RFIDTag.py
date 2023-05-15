class RFIDTag:
    def __init__(self, tagID, student):
        self.tagID = tagID
        self.student = student

    def getTagID(self):
        return self.tagID

    def getStudent(self):
        return self.student

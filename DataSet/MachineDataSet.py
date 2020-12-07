import MySQL


class MachineDataSet:
    def __init__(self, PatientID, machine):
        self.PatientID = PatientID
        self.machine = machine
        self.getpath()

    def getpath(self):
        for i in MySQL.getPath(self.PatientID,self.machine):
            print(i)
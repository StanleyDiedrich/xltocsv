class Building:
    def __init__(self,buildingname,btype,peoples,floornumber,floorheight,appartment):
        self.buildingname=buildingname
        self.btype=btype
        self.peoples=peoples
        self.floornumber=floornumber
        self.floorheight=floorheight
        self.appartment=appartment

    def showdata(self):
        return print(f'Name {self.buildingname}, Type {self.btype},...,Appartment {self.appartment}')
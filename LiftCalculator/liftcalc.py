from BuildingClass import Building as bld
class Lift:
    def __init__(self,doorwidth, closedoortimeentry,movdelayentry,movtimeentry,preopendoorentry,opendoorentry,closedoordelayentry,vnomentry):
        self.doorwidth=doorwidth
        self.tdoorclose=closedoortimeentry
        self.tmovdelay=movdelayentry
        self.tmov=movtimeentry
        self.tpropendoor=preopendoorentry
        self.tdoorclosedelay=opendoorentry
        self.tclosedelay=closedoordelayentry
        self.tmovnom=vnomentry
        self.reversefloor
        self.traffic
        self.normaltime
        self.capacity
        self.nominalspeed

    def normtraffic(self,Building):
        if "Офис" in Building.btype:
            self.traffic = 0, 12 * Building.peoples
            self.normaltime = 30
        if "Гостиница" in self.btype:
            self.traffic = 0.12 * Building.peoples
            self.normaltime = 40
        if "Квартиры" in self.btype:
            self.traffic = 0.06 * Building.peoples
            self.normaltime = 60
        self.capacity=self.traffic/self.normaltime
        return self.capacity,self.normaltime,self.traffic

    def nominalspeed(self,Building):
        height=Building.floornumber*Building.floorheight
        self.nominalspeed=height/self.normaltime
        self.tmovnom=self.nominalspeed/self.nominalspeed
        return self.nominalspeed, self.tmovnom

    def showdata(self):
        return print(f'ЛИФТ ПОЛУЧИЛСЯ')
    def lifttime(self):
        return self.tdoorclose+self.tmovdelay+self.tmov-self.tpropendoor+self.tdoorclosedelay+self.tclosedelay-self.tmovnom

    def val_of_stop(self,floornumber,peoples):
        revfloor = floornumber * (1 - (1 - 1 / floornumber) ** peoples)
        return revfloor

    def reversefloor(self,floornumber, peoples):
        prevalue = 0
        for i in range(0, floornumber):
            prevalue = (i / floornumber) ** peoples
        revfloornumber = floornumber - prevalue
        return round(revfloornumber, 0)

    def movtime(self,tpasanger):
        return 2*self.reversefloor(bld.floornumber,bld.peoples)*self.tmov+self.val_of_stop(bld.floornumber,bld.peoples)*self.lifttime()+2*bld.peoples*tpasanger

    def P5func(self,peoples,liftnumbers):
        return 300*peoples*liftnumbers/self.movtime(self.tpasanger)

    def A5func(self,peoples,buildingtype):
        if buildingtype =="Офис":
            return peoples*0.12
        if buildingtype=="Гостиница":
            return peoples*0.12
        if buildingtype=="Жилое здание":
            return peoples*0.06

    def is_valid(self):
        if self.P5func(bld.peoples,bld.liftnumbers)>self.A5func(bld.peoples,bld.buildingtype):
            return True


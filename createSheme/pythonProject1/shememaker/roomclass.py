class Room:
    def __init__ (self, Id, spacenum,secnum,arnum,roomdef,arname,floor, supply, exhaust):
        self.Id=Id
        self.spacenum=spacenum
        self.secnum=secnum
        self.arnum = arnum
        self.roomdef=roomdef
        self.arname=arname
        self.floor=floor
        self.supply=supply
        self.exhaust=exhaust
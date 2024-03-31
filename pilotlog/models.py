from django.db import models


class BaseModel(models.Model):
    Record_Modified = models.IntegerField(null=False, blank=False)

    class Meta:
        abstract = True
        ordering = ('-Record_Modified',)


class aircraft(BaseModel):
    Fin = models.CharField(max_length=100, null=True, blank=True)
    Sea = models.BooleanField(default=False)
    TMG = models.BooleanField(default=False)
    Efis = models.BooleanField(default=False)
    FNPT = models.IntegerField(null=True, blank=True)
    Make = models.CharField(max_length=100, null=True, blank=True)
    Run2 = models.BooleanField(default=False)
    Class = models.IntegerField(null=True, blank=True)
    Model = models.CharField(max_length=100, null=True, blank=True)
    Power = models.IntegerField(null=True, blank=True)
    Seats = models.IntegerField(null=True, blank=True)
    Active = models.BooleanField(default=False)
    Kg5700 = models.BooleanField(default=False)
    Rating = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    Complex = models.BooleanField(default=False)
    CondLog = models.IntegerField(null=True, blank=True)
    FavList = models.BooleanField(default=False)
    Category = models.IntegerField()
    HighPerf = models.BooleanField(default=False)
    SubModel = models.CharField(null=True, blank=True)
    Aerobatic = models.BooleanField(default=False)
    RefSearch = models.CharField(null=True, blank=True)
    Reference = models.CharField(null=True, blank=True)
    Tailwheel = models.BooleanField(default=False)
    DefaultApp = models.IntegerField(null=True, blank=True)
    DefaultLog = models.IntegerField(null=True, blank=True)
    DefaultOps = models.IntegerField(null=True, blank=True)
    DeviceCode = models.IntegerField(null=True, blank=True)
    AircraftCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    DefaultLaunch = models.IntegerField(null=True, blank=True)
    EngType = models.IntegerField(null=True,blank=True)
    EngGroup = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'Aircraft'






class flight(BaseModel):

    class Meta:
        db_table = 'Flight'
    Aircraft= models.ForeignKey(to='AirCraft',on_delete=models.DO_NOTHING,to_field='AircraftCode',db_column='AircraftCode')
    PF = models.BooleanField(default=False)
    Pax = models.IntegerField(null=True, blank=True)
    Fuel = models.IntegerField(null=True, blank=True)
    DeIce = models.BooleanField(default=False)
    Route = models.CharField(max_length=250, null=True, blank=True)
    ToDay = models.IntegerField(null=True, blank=True)
    minU1 = models.IntegerField(null=True, blank=True)
    minU2 = models.IntegerField(null=True, blank=True)
    minU3 = models.IntegerField(null=True, blank=True)
    minU4 = models.IntegerField(null=True, blank=True)
    minXC = models.IntegerField(null=True, blank=True)
    ArrRwy = models.CharField(max_length=250, null=True, blank=True)
    DepRwy = models.CharField(max_length=250, null=True, blank=True)
    LdgDay = models.IntegerField(null=True, blank=True)
    LiftSW = models.IntegerField(null=True, blank=True)
    P1Code = models.CharField(max_length=250, null=True, blank=True)
    P2Code = models.CharField(max_length=250, null=True, blank=True)
    P3Code = models.CharField(max_length=250, null=True, blank=True)
    P4Code = models.CharField(max_length=250, null=True, blank=True)
    Report = models.CharField(max_length=250, null=True, blank=True)
    TagOps = models.CharField(max_length=250, null=True, blank=True)
    ToEdit = models.BooleanField(default=False)
    Cargo = models.CharField(max_length=100, null=True, blank=True)
    minAIR = models.IntegerField(null=True, blank=True)
    minCOP = models.IntegerField(null=True, blank=True)
    minIFR = models.IntegerField(null=True, blank=True)
    minIMT = models.IntegerField(null=True, blank=True)
    minPIC = models.IntegerField(null=True, blank=True)
    minREL = models.IntegerField(null=True, blank=True)
    minSFR = models.IntegerField(null=True, blank=True)
    ArrCode = models.CharField(max_length=250, null=True, blank=True)
    DateUTC = models.CharField(max_length=250, null=True, blank=True)
    DepCode = models.CharField(max_length=250, null=True, blank=True)
    HobbsIn = models.IntegerField(null=True, blank=True)
    Holding = models.IntegerField(null=True, blank=True)
    Pairing = models.CharField(max_length=250, null=True, blank=True)
    Remarks = models.CharField(max_length=250, null=True, blank=True)
    SignBox = models.IntegerField(null=True, blank=True)
    ToNight = models.IntegerField(null=True, blank=True)
    UserNum = models.IntegerField(null=True, blank=True)
    minDUAL = models.IntegerField(null=True, blank=True)
    minEXAM = models.IntegerField(null=True, blank=True)
    CrewList = models.CharField(max_length=250, null=True, blank=True)
    DateBASE = models.DateField(null=True, blank=True)
    FuelUsed = models.IntegerField(null=True, blank=True)
    HobbsOut = models.IntegerField(null=True, blank=True)
    LdgNight = models.IntegerField(null=True, blank=True)
    NextPage = models.BooleanField(default=False)
    TagDelay = models.CharField(max_length=250, null=True, blank=True)
    Training = models.CharField(max_length=250, null=True, blank=True)
    UserBool = models.BooleanField(default=False)
    UserText = models.CharField(max_length=250, null=True, blank=True)
    minINSTR = models.IntegerField(null=True, blank=True)
    minNIGHT = models.IntegerField(null=True, blank=True)
    minPICUS = models.IntegerField(null=True, blank=True)
    minTOTAL = models.IntegerField(null=True, blank=True)
    ArrOffset = models.IntegerField(null=True, blank=True)
    DateLOCAL = models.DateField(null=True, blank=True)
    DepOffset = models.IntegerField(null=True, blank=True)
    TagLaunch = models.CharField(max_length=250, null=True, blank=True)
    TagLesson = models.CharField(max_length=250, null=True, blank=True)
    ToTimeUTC = models.IntegerField(null=True, blank=True)
    ArrTimeUTC = models.IntegerField(null=True, blank=True)
    BaseOffset = models.IntegerField(null=True, blank=True)
    DepTimeUTC = models.IntegerField(null=True, blank=True)
    FlightCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    LdgTimeUTC = models.IntegerField(null=True, blank=True)
    FuelPlanned = models.IntegerField(null=True, blank=True)
    NextSummary = models.BooleanField(default=False)
    TagApproach = models.CharField(max_length=250, null=True, blank=True)
    ArrTimeSCHED = models.IntegerField(null=True, blank=True)
    DepTimeSCHED = models.IntegerField(null=True, blank=True)
    FlightNumber = models.CharField(max_length=250, null=True, blank=True)
    FlightSearch = models.CharField(max_length=250, null=True, blank=True)



    @property
    def AircraftCode(self):
        return self

    @AircraftCode.setter
    def AircraftCode(self, value):
        if isinstance(value,str):
            self.Aircraft_id = value
        elif isinstance(value,self.__class__):
            self.Aircraft = value
        else:
            raise Exception("AircraftCode either should be str or an Aircraft Object")



class airfield(BaseModel):
    AFCat = models.PositiveIntegerField(null=True,blank=True)
    AFCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    AFIATA = models.CharField(null=True,blank=True,max_length=10)
    AFICAO = models.CharField(null=True,blank=True,max_length=10)
    AFName = models.CharField(null=True,blank=True,max_length=100)
    TZCode = models.PositiveIntegerField(null=False,blank=False)
    Latitude = models.IntegerField(null=True,blank=True)
    ShowList = models.BooleanField()
    AFCountry = models.IntegerField(null=True,blank=True)
    Longitude = models.IntegerField(null=True,blank=True)
    NotesUser = models.CharField(null=True,blank=True,max_length=100)
    RegionUser = models.IntegerField(null=True,blank=True)
    ElevationFT = models.IntegerField(null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    AFFAA = models.CharField(max_length=100,null=True,blank=True)
    Notes = models.CharField(max_length=100,null=True,blank=True)
    UserEdit = models.BooleanField(null=True,blank=True)
    class Meta:
        db_table = 'Airfield'

class pilot(BaseModel):
    Notes = models.CharField(null=True,blank=True,max_length=100)
    Active = models.BooleanField()
    Company = models.CharField(null=True,blank=True,max_length=100)
    FavList = models.BooleanField()
    UserAPI = models.CharField(null=True,blank=True,max_length=100)
    Facebook = models.CharField(null=True,blank=True,max_length=100)
    LinkedIn = models.CharField(null=True,blank=True,max_length=100)
    PilotRef = models.CharField(null=True,blank=True,max_length=100)
    PilotCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    PilotName = models.CharField(null=True,blank=True,max_length=100)
    PilotEMail = models.CharField(null=True,blank=True,max_length=100)
    PilotPhone = models.CharField(null=True,blank=True,max_length=100)
    Certificate = models.CharField(null=True,blank=True,max_length=100)
    PhoneSearch = models.CharField(null=True,blank=True,max_length=100)
    PilotSearch = models.CharField(null=True,blank=True,max_length=100)
    RosterAlias = models.CharField(null=True,blank=True,max_length=100)

    class Meta:
        db_table = 'Pilot'


class imagepic(BaseModel):
    FileExt = models.CharField(null=True,blank=True,max_length=50)
    ImgCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    FileName = models.CharField(null=True,blank=True,max_length=50)
    LinkCode = models.CharField(null=True,blank=True,max_length=50)
    Img_Upload = models.BooleanField()
    Img_Download = models.BooleanField()

    class Meta:
        db_table = 'ImagePic'

class limitrules(BaseModel):
    LTo = models.DateField(null=True,blank=True)
    LFrom = models.DateField(null=True,blank=True)
    LType = models.IntegerField(null=True,blank=True)
    LZone = models.IntegerField(null=True,blank=True)
    LMinutes = models.IntegerField(null=True,blank=True)
    LimitCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    LPeriodCode = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'LimitRules'


class myquery(BaseModel):
    Name = models.CharField(max_length=100,null=True,blank=True)
    mQCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    QuickView = models.BooleanField()
    ShortName = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        db_table = 'myQuery'



class myquerybuild(BaseModel):
    Build1 = models.CharField(null=True,blank=True,max_length=100)
    Build2 = models.CharField(null=True,blank=True,max_length=100)
    Build3 = models.CharField(null=True,blank=True,max_length=100)
    Build4 = models.CharField(null=True,blank=True,max_length=100)
    mQ = models.ForeignKey(to='myquery',on_delete=models.DO_NOTHING,to_field='mQCode',db_column='mQCode')
    mQBCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)

    class Meta:
        db_table = 'myQueryBuild'

    @property
    def mQCode(self):
        return self

    @mQCode.setter
    def mQCode(self, value):
        if isinstance(value,str):
            self.mQ_id = value
        elif isinstance(value,self.__class__):
            self.mQ = value
        else:
            raise Exception("AircraftCode either should be str or an Aircraft Object")


class settingconfig(BaseModel):
    Data = models.CharField(null=True,blank=True,max_length=100)
    Name = models.CharField(null=True,blank=True,max_length=100)
    Group = models.CharField(null=True,blank=True,max_length=100)
    ConfigCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)


    class Meta:
        db_table = 'SettingConfig'



class qualification(BaseModel):
    QCode = models.CharField(max_length=100, null=False, blank=False, db_index=True, unique=True)
    RefExtra = models.IntegerField(null=True,blank=True)
    RefModel = models.CharField(null=True,blank=True,max_length=50)
    Validity = models.IntegerField(null=True,blank=True)
    DateValid = models.CharField(null=True,blank=True,max_length=50)
    QTypeCode = models.IntegerField(null=True,blank=True)
    DateIssued = models.CharField(null=True,blank=True,max_length=50)
    MinimumQty = models.IntegerField(null=True,blank=True)
    NotifyDays = models.IntegerField(null=True,blank=True)
    RefAirfield = models.CharField(null=True,blank=True,max_length=100)
    MinimumPeriod = models.IntegerField(null=True,blank=True)
    NotifyComment = models.CharField(null=True,blank=True,max_length=300)

    class Meta:
        db_table = 'Qualification'
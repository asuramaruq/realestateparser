from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import create_engine, Column, String, Float, Boolean, Integer, ARRAY, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import relationship
from .sessions import engine
from .sessions import session


metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Blocks(Base):
    __tablename__ = 'blocks'

    ObjectGUID = Column(UUID(as_uuid=True), primary_key=True)
    ObjectName = Column(String)
    FamilyGUID = Column(UUID(as_uuid=True))    
    FamilyName = Column(String)
    CityGUID = Column(UUID(as_uuid=True))    
    longitude = Column(Float)
    latitude = Column(Float)
    description = Column(String)
    website = Column(String)
    logo = Column(String)
    logoWeb = Column(String)
    foto = Column(String)
    fotoWeb = Column(String)
    DivisionName = Column(String)
    DivisionGUID = Column(UUID(as_uuid=True))    
    ProjectName = Column(String)
    ProjectGUID = Column(UUID(as_uuid=True))    
    ClassGUID = Column(UUID(as_uuid=True))    
    typeOfPlacement = Column(String)
    floors = Column(Integer)
    apartmentsArea = Column(Float)
    entranceQuantity = Column(Integer)
    address = Column(String)
    parking = Column(Boolean)
    group1 = Column(Integer)
    startSaleDate = Column(String)
    deadline = Column(String)
    launchDate = Column(String)
    durationMonth = Column(Integer)
    startDateSMR = Column(String)
    smrDeadlinePlan = Column(String)
    smrDeadlineFact = Column(String)
    stateCommission = Column(String)
    enterDateOperation = Column(String)
    keyHandover = Column(Boolean)
    docDate = Column(String)
    dateDDU = Column(String)
    picApartmentSheets = Column(String)
    picOfficeSheets = Column(String)
    picStorageSheets = Column(String)
    heightOfWall = Column(String)
    outdoorWall = Column(String)
    warmingOutdoorWall = Column(String)
    window = Column(String)
    balcony = Column(String)
    finishWall = Column(String)
    floor = Column(String)
    facingMateriaOftheFacadeOfApartments = Column(String)
    heatingType = Column(String)
    heatingAppliances = Column(String)
    ventBoxe = Column(String)
    vent = Column(String)
    smartHome = Column(Boolean)
    lift = Column(String)
    City = Column(String)
    CountryGUID = Column(UUID(as_uuid=True))    
    Class = Column(String)
    

class Pomeshcheniye(Base):
    __tablename__ = 'pomeshcheniye'

    PomeshcheniyeGUID = Column(UUID(as_uuid=True), primary_key=True)
    Pomeshcheniye = Column(String)
    ObjectName = Column(String)
    PomeshcheniyeType = Column(String)
    Podezd = Column(Integer)
    Etazh = Column(Integer)
    RoomsCount = Column(Integer)
    ChistovayaOtdelka = Column(Boolean)
    Orient = Column(String)
    Likvidnost = Column(String)
    Potolki = Column(String)
    Moshnost = Column(String)
    deletionMark = Column(Boolean)
    PloshadVnutrenaya = Column(Integer)
    PloshadBalkonov = Column(Integer)
    Balcony = Column(ARRAY(String))
    ObjectGUID = Column(UUID(as_uuid=True))    
    ObjectName = Column(String)
    PomeshcheniyeTypeGUID = Column(UUID(as_uuid=True))    
    PomeshcheniyeType = Column(String)
    LikvidnostGUID = Column(UUID(as_uuid=True))    
    Likvidnost = Column(String)


class DopolnitelnyeRekvizity(Base):
    __tablename__ = 'dopolnitelnye_rekvizity'

    id = Column(Integer, primary_key=True)
    ssylka = Column(String)
    nomerStroki = Column(Integer)
    svoistvo = Column(String)
    znachenie = Column(String)
    # znachenie = Column(Boolean)
    textovoePole = Column(String)

    PomeshcheniyeGUID = Column(UUID, ForeignKey('pomeshcheniye_full.PomeshcheniyeGUID'))
    pomeshcheniye_full = relationship("PomeshcheniyeFull", back_populates="DopolnitelnyeRekvizity")
    
            
class FO(Base):
    __tablename__ = 'fo'

    id = Column(Integer, primary_key=True)
    Sebestoimost = Column(BIGINT)
    Rentabelnost = Column(Integer)
    StoimostPoFinModeli = Column(BIGINT)
    MinStoimostPoDDU = Column(BIGINT)

    PomeshcheniyeGUID = Column(UUID, ForeignKey('pomeshcheniye_full.PomeshcheniyeGUID'))
    pomeshcheniye_full = relationship("PomeshcheniyeFull", back_populates="fo")
    
class PomeshcheniyeFull(Base):
    __tablename__ = 'pomeshcheniye_full'

    PomeshcheniyeGUID = Column(UUID(as_uuid=True), primary_key=True)
    Pomeshcheniye = Column(String)
    ObjectGUID = Column(UUID(as_uuid=True))    
    ObjectName = Column(String)
    Data = Column(DateTime)
    TypeId = Column(UUID(as_uuid=True))
    Price = Column(BIGINT)
    Etazh = Column(Integer)
    FirstPrice = Column(Integer)
    Uglovaya = Column(Boolean)
    StoronySveta = Column(String)
    Vidovaya = Column(Boolean)
    Cost = Column(BIGINT)
    Area = Column(Float)
    PloshadVnutrenaya = Column(Float)
    RoomsCount = Column(Integer)
    KolichestvoStoron = Column(String)
    SkidkaProcent = Column(Float)
    SkidkaNachalnikaOPProcent = Column(Float)
    Natsenka = Column(Integer)
    Podezd = Column(Integer)
    Class_ = Column(String)
    City = Column(String)
    Status = Column(String)
    AgreementDate = Column(DateTime)
    SalePrice = Column(BIGINT)
    Summa = Column(BIGINT)
    ProcentVznosa = Column(Integer)
    Aktsiya = Column(String)
    AktsiyaGUID = Column(UUID(as_uuid=True))
    DateOfSalesStart = Column(DateTime)
    PloshadVnutrenayaPoTP = Column(Float)
    PloshadBalkonaPoTP = Column(Float)
    ZhilayaPloshadPoTP = Column(Float)
    StartovayaTsena = Column(BIGINT)
    
    Kod = Column(String)
    Divizion = Column(String)
    DataDogovora = Column(DateTime)
    Mestonahozhdenie = Column(String)
    TipRassrochki = Column(String)
    ObjectNaimeovanie = Column(String)
    DivizionNaimeovanie = Column(String)
    Dolgota = Column(Float)
    Shirota = Column(Float)
    StaroeNaimeovanie = Column(String)
    NovoeNaimeovanie = Column(String)
    Investitsionnaya = Column(Boolean)
    ChistovayaOtdelka = Column(Boolean)
    TipChistovoyOtdelki = Column(String)
    TipPlanirovki = Column(String)
    Orientatsiya = Column(String)
    Likvidnost = Column(String)
    PloshadBalkona = Column(Float)
    ZhilayaPloshad = Column(Integer)
    VysotaPotolkovKvartira = Column(String)
    Moshchnost = Column(String)
    Prodano = Column(Integer)
    Svetovaya = Column(Boolean)
    DataZayavki = Column(DateTime)
    VariantIspolneniya = Column(String)
    PrizhataKUglu = Column(Boolean)
    StoronaSvetaMaks = Column(String)
    StoronaSvetaMin = Column(String)
    LodgiyaNaKuhne = Column(Boolean)
    SovmeshchennyySanuzel = Column(Boolean)
    KolichestvoSanuzlov = Column(Integer)
    DataDSPoAktu = Column(DateTime)
    DataDkp = Column(DateTime)
    DataDp = Column(DateTime)
    Studiya = Column(Boolean)
    
    Type_ = Column(String)
    DopolnitelnyeRekvizity = relationship("DopolnitelnyeRekvizity", back_populates="pomeshcheniye_full")
    ToSale = Column(Boolean)
    
    fo = relationship("FO", uselist=False, back_populates="pomeshcheniye_full")




# korter.kz

class Building(Base):
    __tablename__ = 'building'
    
    buildingId = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    address = Column(String)
    minPriceSqm = Column(Float)
    minPrice = Column(Float)
    minPriceSqmByLayouts = Column(Float)
    status = Column(String)
    salesStatus = Column(String)
    hasTaxInclusion = Column(Boolean)
    isDeveloperPhoneShown = Column(Boolean)
    developerCallTracking = Column(Boolean)
    realtyCount = Column(Integer)
    phone = Column(String)
    subLocalityNominative = Column(String)
    constructionStatus = Column(String)
    whatsAppPhone = Column(String)
    
    developers = relationship('Developer', back_populates='building')
    attributes = relationship('BuildingAttributes', back_populates='building')
    location = relationship("Location", uselist=False, back_populates="building")

class Developer(Base):
    __tablename__ = 'developer'

    id = Column(Integer, primary_key=True)
    buildingId = Column(Integer, ForeignKey('building.buildingId'))
    
    name = Column(String)
    link = Column(String)
    developerId = Column(Integer)
    isBranded = Column(Boolean)
    hexColor = Column(String)
    logoWhiteNoTextSvg = Column(String)
    
    building = relationship("Building", back_populates="developers")

class BuildingAttributes(Base):
    __tablename__ = 'building_attributes'

    id = Column(Integer, primary_key=True)
    buildingId = Column(Integer, ForeignKey('building.buildingId'))
    
    att_name = Column(String)
    att_value = Column(String)
    
    building = relationship("Building", back_populates="attributes")
    
class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    buildingId = Column(Integer, ForeignKey('building.buildingId'))
    
    lat = Column(Float)
    lng = Column(Float)
    
    building = relationship("Building", back_populates="location")


class TestBuilding(Base):
    __tablename__ = 'test_building'
    
    buildingId = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    address = Column(String)
    minPriceSqm = Column(Float)
    minPrice = Column(Float)
    minPriceSqmByLayouts = Column(Float)
    status = Column(String)
    salesStatus = Column(String)
    hasTaxInclusion = Column(Boolean)
    isDeveloperPhoneShown = Column(Boolean)
    developerCallTracking = Column(Boolean)
    realtyCount = Column(Integer)
    phone = Column(String)
    subLocalityNominative = Column(String)
    constructionStatus = Column(String)
    whatsAppPhone = Column(String)
    
    # relationships
    developers = relationship('TestDeveloper', backref='building')
    attributes = relationship('TestBuildingAttributes', backref='building')
    location = relationship("TestLocation", uselist=False, backref="building")

class TestDeveloper(Base):
    __tablename__ = 'test_developer'

    id = Column(Integer, primary_key=True)
    buildingId = Column(Integer, ForeignKey('test_building.buildingId'))
    
    name = Column(String)
    link = Column(String)
    developerId = Column(Integer)
    isBranded = Column(Boolean)
    hexColor = Column(String)
    logoWhiteNoTextSvg = Column(String)
    
    # relationship not needed as it is backref'd in TestBuilding

class TestBuildingAttributes(Base):
    __tablename__ = 'test_building_attributes'

    id = Column(Integer, primary_key=True)
    buildingId = Column(Integer, ForeignKey('test_building.buildingId'))
    
    att_name = Column(String)
    att_value = Column(String)
    
    # relationship not needed as it is backref'd in TestBuilding
    
class TestLocation(Base):
    __tablename__ = 'test_location'

    id = Column(Integer, primary_key=True)
    buildingId = Column(Integer, ForeignKey('test_building.buildingId'))
    
    lat = Column(Float)
    lng = Column(Float)
    
    # relationship not needed as it is backref'd in TestBuilding
        
# Base.metadata.create_all(bind=engine)

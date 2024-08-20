from typing import List, Optional
from pydantic import BaseModel, validator, UUID4
from datetime import datetime


class Block(BaseModel):
    ObjectGUID: str
    ObjectName: str
    CityGUID: str
    City: str
    DivisionName: str
    DivisionGUID: str
    ClassGUID: str
    Class: str
    floors: int
    group1: int
    startSaleDate: str
    
    class Config:
        orm_mode = True    
        
    @validator('ObjectGUID', pre=True)
    def convert_object_guid(cls, value):
        return str(value)

    @validator('CityGUID', pre=True)
    def convert_city_guid(cls, value):
        return str(value)

    @validator('DivisionGUID', pre=True)
    def convert_division_guid(cls, value):
        return str(value)
    
    @validator('ClassGUID', pre=True)
    def convert_class_guid(cls, value):
        return str(value)            
    
    

class Pomeshcheniye(BaseModel):
    PomeshcheniyeGUID: str
    Pomeshcheniye: str
    ObjectName: str
    PomeshcheniyeType: str
    Podezd: int
    Etazh: int
    RoomsCount: int
    ChistovayaOtdelka: bool
    Orient: str
    Potolki: str
    Moshnost: str
    deletionMark: bool
    PloshadVnutrenaya: int
    PloshadBalkonov: int
    Balcony: Optional[List[str]] 
    ObjectGUID: str
    ObjectName: str
    PomeshcheniyeTypeGUID: str
    PomeshcheniyeType: str
    LikvidnostGUID: str
    Likvidnost: str    

    class Config:
        orm_mode = True    
    
    
    @validator('PomeshcheniyeGUID', pre=True)
    def convert_pomeshcheniye_guid(cls, value):
        return str(value)

    @validator('ObjectGUID', pre=True)
    def convert_object_guid(cls, value):
        return str(value)

    @validator('PomeshcheniyeTypeGUID', pre=True)
    def convert_pomeshcheniye_type_guid(cls, value):
        return str(value)

    @validator('LikvidnostGUID', pre=True)
    def convert_likvidnost_guid(cls, value):
        return str(value)


class CreatePomeshcheniye(BaseModel):
    PomeshcheniyeGUID: UUID4
    Pomeshcheniye: str
    ObjectName: str
    PomeshcheniyeType: str
    Podezd: int
    Etazh: int
    RoomsCount: int
    ChistovayaOtdelka: bool
    Orient: str
    Potolki: str
    Moshnost: str
    deletionMark: bool
    PloshadVnutrenaya: int
    PloshadBalkonov: int
    Balcony: Optional[List[str]] 
    ObjectGUID: UUID4
    ObjectName: str
    PomeshcheniyeTypeGUID: UUID4
    PomeshcheniyeType: str
    LikvidnostGUID: UUID4
    Likvidnost: str    

    class Config:
        orm_mode = True    


class DopolnitelnyeRekvizity(BaseModel):
    id: Optional[int]
    ssylka: Optional[str]
    nomerStroki: Optional[int]
    svoistvo: Optional[str]
    znachenie: Optional[str]
    textovoePole: Optional[str]

                
class FO(BaseModel):
    id: Optional[int]
    Sebestoimost: Optional[int]
    Rentabelnost: Optional[int]
    StoimostPoFinModeli: Optional[int]
    MinStoimostPoDDU: Optional[int]


class PomeshcheniyeFull(BaseModel):
    PomeshcheniyeGUID: Optional[str]
    Pomeshcheniye: Optional[str]
    ObjectGUID: Optional[str]    
    ObjectName: Optional[str]
    Data: Optional[datetime]
    TypeId: Optional[str]
    Price: Optional[int]
    Etazh: Optional[int]
    FirstPrice: Optional[int]
    Uglovaya: Optional[bool]
    StoronySveta: Optional[str]
    Vidovaya: Optional[bool]
    Cost: Optional[int]
    Area: Optional[float]
    PloshadVnutrenaya: Optional[float]
    RoomsCount: Optional[int]
    KolichestvoStoron: Optional[str]
    SkidkaProcent: Optional[float]
    SkidkaNachalnikaOPProcent: Optional[float]
    Natsenka: Optional[int]
    Podezd: Optional[int]
    Class_: Optional[str]
    City: Optional[str]
    Status: Optional[str]
    AgreementDate: Optional[datetime]
    SalePrice: Optional[int]
    Summa: Optional[int]
    ProcentVznosa: Optional[int]
    Aktsiya: Optional[str]
    AktsiyaGUID: Optional[str]
    DateOfSalesStart: Optional[datetime]
    PloshadVnutrenayaPoTP: Optional[float]
    PloshadBalkonaPoTP: Optional[float]
    ZhilayaPloshadPoTP: Optional[float]
    StartovayaTsena: Optional[int]
    
    Kod: Optional[str]
    Divizion: Optional[str]
    DataDogovora: Optional[datetime]
    Mestonahozhdenie: Optional[str]
    TipRassrochki: Optional[str]
    ObjectNaimeovanie: Optional[str]
    DivizionNaimeovanie: Optional[str]
    Dolgota: Optional[float]
    Shirota: Optional[float]
    StaroeNaimeovanie: Optional[str]
    NovoeNaimeovanie: Optional[str]
    Investitsionnaya: Optional[bool]
    ChistovayaOtdelka: Optional[bool]
    TipChistovoyOtdelki: Optional[str]
    TipPlanirovki: Optional[str]
    Orientatsiya: Optional[str]
    Likvidnost: Optional[str]
    PloshadBalkona: Optional[float]
    ZhilayaPloshad: Optional[int]
    VysotaPotolkovKvartira: Optional[str]
    Moshchnost: Optional[str]
    Prodano: Optional[int]
    Svetovaya: Optional[bool]
    DataZayavki: Optional[datetime]
    VariantIspolneniya: Optional[str]
    PrizhataKUglu: Optional[bool]
    StoronaSvetaMaks: Optional[str]
    StoronaSvetaMin: Optional[str]
    LodgiyaNaKuhne: Optional[bool]
    SovmeshchennyySanuzel: Optional[bool]
    KolichestvoSanuzlov: Optional[int]
    DataDSPoAktu: Optional[datetime]
    DataDkp: Optional[datetime]
    DataDp: Optional[datetime]
    Studiya: Optional[bool]
    
    Type_: Optional[str]
    ToSale: Optional[bool]
    # DopolnitelnyeRekvizity: Optional[List[DopolnitelnyeRekvizity]] = List
    fo: Optional[FO] = dict

    @validator('PomeshcheniyeGUID', pre=True)
    def convert_pomeshcheniye_guid(cls, value):
        return str(value)

    @validator('ObjectGUID', pre=True)
    def convert_object_guid(cls, value):
        return str(value)

    @validator('TypeId', pre=True)
    def convert_typeid(cls, value):
        return str(value)

    @validator('AktsiyaGUID', pre=True)
    def convert_aktsiya_guid(cls, value):
        return str(value)
        
    class Config:
        orm_mode = True       
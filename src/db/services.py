from sqlalchemy.exc import IntegrityError, PendingRollbackError
from .sessions import session
from src.db import schemas as db_sch


def save_blocks_df(raw_blocks):
    for raw_block in raw_blocks:
        try:
            data = db_sch.Blocks(**raw_block)
            session.add(data)
            session.commit()
        except (IntegrityError, PendingRollbackError) as e:
            print(f"\n\n ObjectGUID == {raw_block['ObjectGUID']}")
            continue
    
def get_blocks_all():
    return session.query(
        db_sch.Blocks.ObjectGUID,
        db_sch.Blocks.ObjectName,
        db_sch.Blocks.CityGUID,
        db_sch.Blocks.City,
        db_sch.Blocks.DivisionGUID,
        db_sch.Blocks.DivisionName,
        db_sch.Blocks.ClassGUID,
        db_sch.Blocks.Class,
        db_sch.Blocks.floors,
        db_sch.Blocks.group1,
        db_sch.Blocks.startSaleDate
    ).all()

def get_blocks_without_full_info(limit=None):
    subquery = session.query(
        db_sch.Blocks.ObjectGUID
    ).except_(session.query(
        db_sch.PomeshcheniyeFull.ObjectGUID
    ))
    if limit:
        subquery = subquery.limit(limit)
    return [result[0] for result in subquery.all()]


def get_block(block_id):
    return session.query(
        db_sch.Blocks.ObjectGUID,
        db_sch.Blocks.ObjectName,
        db_sch.Blocks.CityGUID,
        db_sch.Blocks.City,
        db_sch.Blocks.DivisionGUID,
        db_sch.Blocks.DivisionName,
        db_sch.Blocks.ClassGUID,
        db_sch.Blocks.Class,
        db_sch.Blocks.floors,
        db_sch.Blocks.group1,
        db_sch.Blocks.startSaleDate
    ).filter(db_sch.Blocks.ObjectGUID == block_id).first()
    

def save_draft_pomeshcheniye(pomeshcheniye):    
    new_xdata = db_sch.Pomeshcheniye(**pomeshcheniye.dict())
    session.add(new_xdata)
    session.commit()
    session.refresh(new_xdata)
    return new_xdata


def get_draft_pomeshcheniye(pomeshcheniye_id):
    return session.query(
        db_sch.Pomeshcheniye
    ).filter(db_sch.Pomeshcheniye.PomeshcheniyeGUID == pomeshcheniye_id).first()


def save_pomeshcheniye_full_info(pomeshcheniya):
    for input_dict in pomeshcheniya:
        additional_attributes = input_dict.pop('ДополнительныеРеквизиты', [])
        fo = input_dict.pop('FO', None)
        input_dict['Class_'] = input_dict.pop('Class', None)
        input_dict['Type_'] = input_dict.pop('Type', None)
        
        input_dict['Kod'] = input_dict.pop('Код', None)
        input_dict['Divizion'] = input_dict.pop('Дивизион', None)
        input_dict['DataDogovora'] = input_dict.pop('ДатаДоговора', None)
        input_dict['Mestonahozhdenie'] = input_dict.pop('Местонахождение', None)
        input_dict['TipRassrochki'] = input_dict.pop('ТипРассрочки', None)
        input_dict['ObjectNaimeovanie'] = input_dict.pop('ОбъектНаименование', None)
        input_dict['DivizionNaimeovanie'] = input_dict.pop('ДивизионНаименование', None)
        input_dict['Dolgota'] = input_dict.pop('Долгота', None)
        input_dict['Shirota'] = input_dict.pop('Широта', None)
        input_dict['StaroeNaimeovanie'] = input_dict.pop('СтароеНаименование', None)
        input_dict['NovoeNaimeovanie'] = input_dict.pop('НовоеНаименование', None)
        input_dict['Investitsionnaya'] = input_dict.pop('Инвестиционная', None)
        input_dict['ChistovayaOtdelka'] = input_dict.pop('ЧистоваяОтделка', None)
        input_dict['TipChistovoyOtdelki'] = input_dict.pop('ТипЧистовойОтделки', None)
        input_dict['TipPlanirovki'] = input_dict.pop('ТипПланировки', None)
        input_dict['Orientatsiya'] = input_dict.pop('Ориентация', None)
        input_dict['Likvidnost'] = input_dict.pop('Ликвидность', None)
        input_dict['PloshadBalkona'] = input_dict.pop('ПлощадьБалкона', None)
        input_dict['ZhilayaPloshad'] = input_dict.pop('ЖилаяПлощадь', None)
        input_dict['VysotaPotolkovKvartira'] = input_dict.pop('ВысотаПотолковКвартира', None)
        input_dict['Moshchnost'] = input_dict.pop('Мощность', None)
        input_dict['Prodano'] = input_dict.pop('Продано', None)
        input_dict['Svetovaya'] = input_dict.pop('Световая', None)
        input_dict['DataZayavki'] = input_dict.pop('ДатаЗаявки', None)
        input_dict['VariantIspolneniya'] = input_dict.pop('ВариантИсполнения', None)
        input_dict['PrizhataKUglu'] = input_dict.pop('ПрижатаКУглу', None)
        input_dict['StoronaSvetaMaks'] = input_dict.pop('СторонаСветаМакс', None)
        input_dict['StoronaSvetaMin'] = input_dict.pop('СторонаСветаМин', None)
        input_dict['LodgiyaNaKuhne'] = input_dict.pop('ЛоджияНаКухне', None)
        input_dict['SovmeshchennyySanuzel'] = input_dict.pop('СовмещенныйСанузел', None)
        input_dict['KolichestvoSanuzlov'] = input_dict.pop('КоличествоCанузлов', None)
        input_dict['DataDSPoAktu'] = input_dict.pop('ДатаДСПоАкту', None)
        input_dict['DataDkp'] = input_dict.pop('ДатаДКП', None)
        input_dict['DataDp'] = input_dict.pop('ДатаДП', None)
        input_dict['Studiya'] = input_dict.pop('Студия', None)
        input_dict['ToSale'] = input_dict.pop('toSale', None)

        try:
            pomeshcheniye_full = db_sch.PomeshcheniyeFull(**input_dict)
            session.add(pomeshcheniye_full)

            
            if additional_attributes:
                for additional_attribute in additional_attributes:
                    if "Ссылка" in additional_attribute:
                        additional_attribute["ssylka"] = additional_attribute.pop("Ссылка")
                    if "НомерСтроки" in additional_attribute:
                        additional_attribute["nomerStroki"] = additional_attribute.pop("НомерСтроки")
                    if "Свойство" in additional_attribute:
                        additional_attribute["svoistvo"] = additional_attribute.pop("Свойство")
                    if "Значение" in additional_attribute:
                        additional_attribute["znachenie"] = str(additional_attribute.pop("Значение"))
                    if "ТекстоваяСтрока" in additional_attribute:
                        additional_attribute["textovoePole"] = additional_attribute.pop("ТекстоваяСтрока")

                    aa = db_sch.DopolnitelnyeRekvizity(**additional_attribute)
                    pomeshcheniye_full.DopolnitelnyeRekvizity.append(aa)

            if fo:
                ff = db_sch.FO(**fo)
                pomeshcheniye_full.fo = ff
            

            session.commit()
            session.refresh(pomeshcheniye_full)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()        


def get_pomeshcheniye_full(pomeshcheniye_id):
    return session.query(
        db_sch.PomeshcheniyeFull
    ).filter(db_sch.PomeshcheniyeFull.PomeshcheniyeGUID == pomeshcheniye_id).first()

def get_block_full(ObjectGUID):
    return session.query(
        db_sch.PomeshcheniyeFull
    ).filter(db_sch.PomeshcheniyeFull.ObjectGUID == ObjectGUID).all()


def get_buildings_without_full_info(limit=None):
    subquery = session.query(
        db_sch.Building.buildingId,
    ).except_(session.query(
        db_sch.BuildingAttributes.buildingId
    )).subquery()
    subquery = session.query(
        db_sch.Building.buildingId,
        db_sch.Building.url
    ).filter(db_sch.Building.buildingId.in_(subquery))
    
    if limit:
        subquery = subquery.limit(limit)
    return subquery.all()

def save_building_info(building_id, attributes):
    try:
        # Retrieve the user by user_id
        building = session.query(db_sch.Building).filter(db_sch.Building.buildingId == building_id).first()
        
        # Create and assign roles if provided
        if attributes:
            for attribute in attributes:
                att = db_sch.BuildingAttributes(att_name=attribute[0], att_value=attribute[1])
                session.add(att)
                building.attributes.append(att)
                

        session.commit()
        session.refresh(building)
        return building
    except IntegrityError as e:
        session.rollback()  # Rollback the changes
        print(f"[EXISTS]  :: {building_id=:<5}")
        return
    except Exception as e:
        session.rollback()
        session.close()
        raise e
        


def get_buildings_without_full_info_test(limit=None):
    subquery = session.query(
        db_sch.TestBuilding.buildingId,
    ).except_(session.query(
        db_sch.TestBuildingAttributes.buildingId
    )).subquery()
    subquery = session.query(
        db_sch.TestBuilding.buildingId,
        db_sch.TestBuilding.url
    ).filter(db_sch.TestBuilding.buildingId.in_(subquery))
    
    if limit:
        subquery = subquery.limit(limit)
    return subquery.all()

def save_building_info_test(building_id, attributes):
    try:
        # Retrieve the user by user_id
        building = session.query(db_sch.TestBuilding).filter(db_sch.TestBuilding.buildingId == building_id).first()
        
        # Create and assign roles if provided
        if attributes:
            for attribute in attributes:
                att = db_sch.TestBuildingAttributes(att_name=attribute[0], att_value=attribute[1])
                session.add(att)
                building.attributes.append(att)
                

        session.commit()
        session.refresh(building)
        return building
    except IntegrityError as e:
        session.rollback()  # Rollback the changes
        print(f"[EXISTS]  :: {building_id=:<5}")
        return
    except Exception as e:
        session.rollback()
        session.close()
        raise e
        

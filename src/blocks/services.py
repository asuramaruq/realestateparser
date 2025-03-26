from src.db import services as db_srv
from src.api_ones import requests as ones_req

def get_blocks_all():
    return db_srv.get_blocks_all()

def get_block(block_id):
    return db_srv.get_block(block_id)

def save_draft_pomeshcheniye(pomeshcheniye):
    return db_srv.save_draft_pomeshcheniye(pomeshcheniye)

def get_draft_pomeshcheniye(PomeshcheniyeGUID):
    return db_srv.get_draft_pomeshcheniye(PomeshcheniyeGUID)

def save_pomeshcheniye_full(pomeshcheniye_full):
    return db_srv.save_pomeshcheniye_full_info(pomeshcheniye_full)

def get_pomeshcheniye_full(PomeshcheniyeGUID):
    return db_srv.get_pomeshcheniye_full(PomeshcheniyeGUID)

def get_block_full(ObjectGUID):
    return db_srv.get_block_full(ObjectGUID)

def get_blocks_without_full_info(limit=None):
    return db_srv.get_blocks_without_full_info(limit)

def save_pomeshcheniye_full_info(pomeshcheniye_full):
    return db_srv.save_pomeshcheniye_full_info(pomeshcheniye_full)

def download_blocks_full_info(limit=None):
    blocks_without_full_info = get_blocks_without_full_info(limit)
    left = len(blocks_without_full_info)
    index = 1
    for ObjectGUID in blocks_without_full_info:
        data = ones_req.get_full_information_pomesheniye(str(ObjectGUID))
        save_pomeshcheniye_full_info(data)
        print(f"{index}/{left} {ObjectGUID=}")
        index += 1
    
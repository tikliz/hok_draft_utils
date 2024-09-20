import json
from pathlib import Path

def update_field_in_json(file_path, target_field, new_value):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if "data" in data and "heroList" in data["data"]:
        for item in data["data"]["heroList"]:
            if target_field in item:
                extension = Path(item["icon"]).suffix
                item[target_field] = new_value.format(item["heroName"], extension)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    return data

# Usage example
file_path = './res/heros/hero-data-ptBr.json'
target_field = 'icon'
new_value = 'https://raw.githubusercontent.com/tikliz/hok_draft_utils/refs/heads/main/res/heros/Images/image_hero_head-{}{}'  # The new value you want to set

updated_data = update_field_in_json(file_path, target_field, new_value)
print("Updated data:", updated_data)
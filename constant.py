import json

API_key = '1792666018:AAFdMxINeAY06Thw8aR--DGTqgrObpzrono'
admin_list=[-1001323642182,496530156,-1001229538530]
groups_list=[]

def read_file():
    with open('responses.json', encoding="utf8") as f:
        data = f.read()
    response_dict = json.loads(data, strict=False)
    f.close()
    return dict(response_dict)


def update_file(new_dict):
    with open('responses.json', 'r+', encoding="utf8") as file:
            file.seek(0)
            json.dump(new_dict, file, indent=4,ensure_ascii=False)
            file.truncate()
            return f"the response {new_dict} added"


def remove_response(remove_response):
    with open('responses.json', 'r+', encoding="utf8") as file:
        file_data = json.load(file)
        if remove_response in file_data:
            file_data.pop(remove_response)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            return_ = "the response added"
        else: return None


import json
import pickle
import requests

admin_list = [-1001323642182, 496530156, -1001229538530]
groups_list = []


def read_file():
    with open('responses.json', encoding="utf8") as f:
        data = f.read()
    response_dict = json.loads(data, strict=False)
    f.close()
    return dict(response_dict)


def update_file(new_dict):
    with open('responses.json', 'r+', encoding="utf8") as file:
        file.seek(0)
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
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
        else:
            return None


def add_to_list(msg_id):
    file = "report_id.pkl"
    list_file = open(file, "rb")
    loaded_list = pickle.load(list_file)
    for i in range(len(loaded_list) - 1, 0, -1):
        loaded_list[i] = loaded_list[i - 1]
    loaded_list[0] = msg_id
    list_file.close()
    list_file_ = open(file, "wb")
    pickle.dump(loaded_list, list_file_)
    list_file_.close()
    return loaded_list


def get_from_list(num):
    file = "report_id.pkl"
    list_file = open(file, "rb")
    return list_file[num-1]


def send_message(msg,chat_id):
    URL=f"https://api.telegram.org/bot1792666018:AAFdMxINeAY06Thw8aR--DGTqgrObpzrono/sendMessage?chat_id\
    ={chat_id}&text={msg}"
    r = requests.get(URL)#, auth=('user', 'pass') r.status_code



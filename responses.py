from datetime import datetime

from constant import read_file, update_file, admin_list
from databaseposgrete import save_,check,remove_,del_

response_dict=read_file()


def if_time_date(response):
    now = datetime.now()
    time = now.strftime('%I:%M:%S')  # ("%H:%M:%S")
    date = now.strftime("%d/%m/%y")
    if response == 'time':
        response = time
    if response == 'date':
        response = date
    return response

def check_dict(userinput):
    print("check_dict")
    if userinput in response_dict:
        response=response_dict[userinput]
        # print(userinput, "from response_dict")
        response=if_time_date(response)
        return response

    for key in response_dict:
        if key in userinput:
            response=response_dict[key]
            response=if_time_date(response)
            print(response)
            return response
    return None


def sample_responses(input_massage, chat_id):
    userinput = str(input_massage.lower())
    print(userinput)
    print("sample_response")
    admin_add_list = list(admin_list)
    admin_add_list.remove(-1001323642182)
    if chat_id in admin_add_list: # ==496530156 or chat_id == -1001229538530:
        print("from admin")
        if 'addrespone ' in userinput or 'addresponellink ' in userinput:
            # print("from addres")
            userinput=remove_(userinput,'addrespone ')
            if userinput[:4]=='link':
                userinput=remove_(userinput,'link ')
                key, value = userinput.split(",")
            else: key, value = userinput.split(":")
            response_dict[key]=value
            update_file(response_dict)
            print("the response insert succesfully.")
            return f"the response {userinput} inserted"
        elif 'removerespone ' in userinput:
            print("from remove")
            userinput=remove_(userinput,'removerespone ')
            del response_dict[userinput]
            try:
                print(response_dict[userinput])
            except: print("Dome!")
            update_file(response_dict)
            print("the response removed succesfully.")
            return f"the response {userinput} removed"

        elif 'addvoices ' in userinput or 'addstickers ' in userinput or'addpictures ' in userinput:
            print("from addrevoices")
            return userinput

        elif userinput == 'save': save_(); return 'Done!'

        elif 'removesaive ' in userinput :
            userinput=remove_(userinput,'removesaive ')
            print(userinput,"remove")
            del_(userinput)
            # print(del_(userinput))
            return "remove"

    if 'نفر ' in userinput :
        # print("im here نفر")
        userinput_=remove_(userinput,'نفر ')
        message_id=check(userinput_)
        print("from نفر \n",userinput,message_id)
        if message_id=='didnt work':return 'منورني ياوردة انت ماكو هيج كلاوات عدنه'
        return message_id

    else:
        # print("else")
        message_id = check(userinput)
        print("messag_id \n",message_id)
        if type(message_id) is int:
            return message_id
        check_dict_ = check_dict(userinput)
        if check_dict_ is not None:
            return check_dict_

        # else:
            # return userinput

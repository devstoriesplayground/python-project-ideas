from datetime import datetime as dt
import json


def main():
    global total
    a = True
    to_do_list = []
    while a:
        print("WELCOME TO DEVSTORIES PLAYGROUND")
        print("***** M E N U ******")
        print("[L] GET TO DO LIST")
        print("[N] CREATE A TO DO")
        print("[D] DELETE A NOTE")
        print("[E] EXIT")
        user_menu_choice = input('Choose your menu option: ')
        try:
            if user_menu_choice == "L":
                print("GET TO DO LIST")
                print(to_do_list)
            elif user_menu_choice == "N":
                print("CREATE A TO DO NOTE")
                add_title = input('Create a title: ')
                add_body = input('Create a body: ')
                add_note = {
                    "title": add_title,
                    "body": add_body,
                    "created_at": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": dt.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                to_do_list.append(add_note.copy())
                print(json.dumps(to_do_list))
            elif user_menu_choice == "D":
                print("DELETE A TO DO NOTE")
                print(to_do_list)
                length_todo_list = len(to_do_list) - 1
                delete_note = input(f'Choose which note you want to delete from [0 - {length_todo_list}]: ')
                to_do_list.pop(int(delete_note))
            elif user_menu_choice == "E":
                print("THANK YOU FOR USING TO DO LIST APPLICATION - DEVSTORIES PLAYGROUND")
                break
        except Exception as ex:
            continue


if __name__ == "__main__":
    main()
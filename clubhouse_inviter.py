from clubhouse.clubhouse.clubhouse import Clubhouse
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('clubhouse/setting.ini')
    user_device = config.get('Account', 'user_device')
    user_id = config.get('Account', 'user_id')
    user_token = config.get('Account', 'user_token')

    clubhouse = Clubhouse(
        user_id=user_id,
        user_token=user_token,
        user_device=user_device
    )
    # print(clubhouse.me())
    name = input('Enter the name of the person to invite : ')
    phone_number = input('Enter the phone number of the person to invite with \"+\" as +79991234567: ')
    print(clubhouse.invite_to_app(name=name, phone_number=phone_number))

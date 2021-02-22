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
    name = input('Input invited person\'s name: ')
    phone_number = input('Input invited person\'s phone number with \"+\" as +79991234567: ')
    print(clubhouse.invite_to_app(name=name, phone_number=phone_number))

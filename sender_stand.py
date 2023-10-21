import configuration
import requests
import data

#Создаем новый заказ
def create_order(user_body):
    return requests.post(configuration.URL + configuration.CREATE_USER_ORDER,
                         json=user_body)

#Создаем новый заказ и записываем его трек номер
def get_track_number_from_new_order():
    response_new_order = create_order(data.user_body)
    track_number = str(response_new_order.json()['track'])
    return track_number

#Получаем набор по треку заказа
def get_order_by_track():
    return requests.get(configuration.URL + configuration.GET_ORDER_BY_NUMBER + '?t=' + get_track_number_from_new_order())

response_order = get_order_by_track()


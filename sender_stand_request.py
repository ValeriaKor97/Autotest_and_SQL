import configuration
import requests
import data


# функция для создания заказа c заданным телом
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=data.headers)


# Запрос на получение информацию о заказе по его трек-номеру
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track))


# В переменную response сохраняется результат запроса на создание заказа
response = create_order(data.order_body)
# Вывести номер track
print(response.json())

import requests
from data_json import DataJson 

class TestInsitechAPI:
    
    def test_insitech_post_order(self):
        #Step 1
        url = "https://opm-website.iot-asm-test1.insitech.live/api/strapi/cart-item"
        #Step 2
        response = requests.post(url, json=DataJson.data)
        #Step 3
        responseJson = response.json()

        #Asserts
        assert response.status_code == 200, 'Запрос на добавление товара в избранное не завершился успешно!'
        assert isinstance(responseJson, int), 'Тело ответа некорректно!'
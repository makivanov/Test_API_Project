import allure


class CheckStatus:
    def __init__(self):
        self.response = None

    def check_that_status_is_value(self, value):
        assert self.response.status_code == value

    @allure.step('Проверка что код ответа 200')
    def check_that_status_is_200(self):
        self.check_that_status_is_value(200)

    @allure.step('Проверка что код ответа 400')
    def check_that_status_is_400(self):
        self.check_that_status_is_value(400)

    @allure.step('Проверка что код ответа 401')
    def check_that_status_is_401(self):
        self.check_that_status_is_value(401)

    @allure.step('Проверка что код ответа 403')
    def check_that_status_is_403(self):
        self.check_that_status_is_value(403)

    @allure.step('Проверка что код ответа 404')
    def check_that_status_is_404(self):
        self.check_that_status_is_value(404)

    @allure.step('Проверка что код ответа 405')
    def check_that_status_is_405(self):
        self.check_that_status_is_value(405)
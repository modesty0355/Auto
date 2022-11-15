from selenium import webdriver


class ymw_login():

    def __init__(self):
        # 进入首页，点击登录
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/EasyBuy/Home?action=index")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/span/a[1]").click()
        self.delay()

    def login(self):
        # 输入管理员账号密码登录
        self.driver.find_element_by_id("loginName").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input").click()

    def delay(self):
        # 延迟
        self.driver.implicitly_wait(5)


if __name__ == '__main__':
    lg = ymw_login()
    lg.login()

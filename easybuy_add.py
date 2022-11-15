from easybuy_login import ymw_login
from selenium.webdriver.support.select import Select


class ymw_add():

    def __init__(self):
        # 点击后台管理
        self.lg = ymw_login()
        self.lg.login()
        self.lg.driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/span[2]/a").click()
        self.delay()

    def delay(self):
        # 延迟
        self.lg.delay()

    def add(self):
        # 添加华为mate50rs
        self.lg.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[4]/ul/li[3]/a").click()
        self.delay()
        sel1 = self.lg.driver.find_element_by_xpath("//*[@id=\"productCategoryLevel1\"]")
        sel2 = self.lg.driver.find_element_by_xpath("//*[@id=\"productCategoryLevel2\"]")
        sel3 = self.lg.driver.find_element_by_xpath("//*[@id=\"productCategoryLevel3\"]")
        no1 = Select(sel1)
        no2 = Select(sel2)
        no3 = Select(sel3)
        no1.select_by_value("670")
        no2.select_by_value("671")
        no3.select_by_value("672")
        self.lg.driver.find_element_by_id("name").send_keys("HUAWEI mate50 RS")
        self.lg.driver.find_element_by_name("photo").send_keys("C:\\Users\\Administrator\\Desktop\\mate50rs.png")
        self.lg.driver.find_element_by_id("price").send_keys("10000")
        self.lg.driver.find_element_by_id("stock").send_keys("1000")
        self.lg.driver.find_element_by_xpath("//*[@id=\"productAdd\"]/table/tbody/tr[9]/td[2]/input").click()

    def __del__(self):
        self.lg.driver.close()


if __name__ == '__main__':
    ymw = ymw_add()
    ymw.add()

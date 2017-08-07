import time


class LoginPage:

    # element location
    username_id = 'usernameInput'
    password_id = 'passwordInput'
    login_button_id = 'loginButton'
    personal_name_xpath = '//*[@id="personalInfoDropdownMenu"]/span' 


    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def type_username(self, username):
        username_text = self.driver.find_element_by_id(self.username_id)
        username_text.clear()
        username_text.send_keys(username)

    def type_password(self, password):
        password_text = self.driver.find_element_by_id(self.password_id)
        password_text.clear()
        password_text.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element_by_id(self.login_button_id)
        login_button.click()

    # def alert_msg_hint(self):
    #     alert_msg = self.driver.find_element_by_tag_name(self.login_alert_msg_tagname)
    #     return alert_msg.text

    # 登陆失败信息提示
    def personal_name_show(self):
        personal_name = self.driver.find_element_by_xpath(self.personal_name_xpath)
        return personal_name.text

    # 登陆成功用户名展示
    def login(self, username, password):
        self.driver.get(self.url)
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()
        time.sleep(2)
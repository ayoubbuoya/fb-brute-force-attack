import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as fir_op
from selenium.webdriver.chrome.options import Options as ch_op
from time import sleep
from bs4 import BeautifulSoup


class Facebook():
    def __init__(self, browser="firefox", gui="yes", exec_path="default") -> None:
        self.browser = browser
        self.gui = gui
        self.exec_path = exec_path
        self.fb_info = {}
        if self.browser == "chrome":
            if self.exec_path == "default":
                self.exec_path = "/bin/chromedriver"
            if self.gui.lower() == "no":
                op = ch_op()
                op.add_argument("--headless")
                self.br = webdriver.Chrome(
                    executable_path=self.exec_path,
                     options=op
                )
            else:
                self.br = webdriver.Chrome(executable_path=self.exec_path)
        elif self.browser == "firefox":
            if self.exec_path == "default":
                self.exec_path = "/bin/geckodriver"
            if self.gui.lower() == "no":
                op = fir_op()
                op.add_argument("--headless")
                self.br = webdriver.Firefox(
                    executable_path=self.exec_path,
                    options=op
                )
            else:
                self.br = webdriver.Firefox(executable_path=self.exec_path)

    def go_to_profile(self):
        print("Going To Profile Page ...")
        profile_html = self.br.find_element(
            by="id",
            value="profile_tab_jewel"
        ).get_attribute("outerHTML")
        soup = BeautifulSoup(profile_html, "html.parser")
        prof_url = "https://m.facebook.com" + soup.find("a")["href"]
        prof_url = prof_url.split("?")[0]
        self.br.get(prof_url)
        print("Going To Profile Page Success")

    def sync_fb_info(self):
        self.go_to_profile()
        user_id = self.br.current_url.split("/")[-1]
        name_html = self.br.find_element(
            by="id", value="cover-name-root").get_attribute("outerHTML")
        name = BeautifulSoup(name_html, "html.parser").find("h3").getText()

        self.fb_info["id"] = user_id
        self.fb_info["name"] = name
        self.fb_info["email"] = self.email
        self.fb_info["password"] = self.passwd

    def extract_prof_intro_sec(self, filename="prof_intro_sec.html"):
        if "https://m.facebook.com/" + self.fb_info["id"] not in self.br.current_url:
            self.go_to_profile()
        html_data = self.br.find_element(
            by="id", value="profile_intro_card").get_attribute("outerHTML")
        with open(filename, "w") as f:
            f.write(html_data)
            f.close()

    def extract_info_to(self, filename="fb_info.json"):
        self.sync_fb_info()
        self.extract_prof_intro_sec()
        json_data = json.dumps(self.fb_info)
        with open(filename, "w") as f:
            f.write(json_data)
            f.close()

    def download_prof_pict(self):
        pass

    def login(self, email, passwd):

        self.br.get("https://m.facebook.com/login")

        email_field = self.br.find_element(by="name", value="email")
        passwd_field = self.br.find_element(by="name", value="pass")
        login_butt = self.br.find_element(by="name", value="login")

        email_field.send_keys(email)
        passwd_field.send_keys(passwd)
        login_butt.click()

        sleep(4)

        self.br.get("https://m.facebook.com/")

        if self.br.title == "Facebook":
            self.email = email
            self.passwd = passwd
            # if self.gui != "yes":
            #     self.br.close()
            return 200

        else:
            # if self.gui != "yes":
            #     self.br.quit()
            return 404

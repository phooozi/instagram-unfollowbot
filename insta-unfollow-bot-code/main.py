from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        self.username = username
        self.driver.get("https://www.instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)
     
    def get_unfollowers(self):
        self.driver.get("https://www.instagram.com/phooozi/")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self._get_names()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()
        unfollowers = [user for user in following if user not in followers]
        print(unfollowers)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        last_ht, ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        return names
        
        
    
    sleep(20)
username = input("Username: ")
pw = input("Password: ")
my_bot = InstaBot(username, pw)
my_bot.get_unfollowers()

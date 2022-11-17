# Author: A. Ulm, ITE

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class LinkedinBot:

    def __init__(self):
        # Chromedriver path
        # Chromedriver is version specific, the current version in the repository is for Chrome 107
        path = r'C:\**\**\PycharmProjects\pythonProject\Linkedin bot\assets\webdriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()  # For maximizing window

        # ender you email and password for LinkedIn
        self.email = "***"
        self.password = "***"
        self.contentFile = open("listKeywords.txt").readlines()

    def LinkedinLogin(self):
        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(1)
        text_area1 = self.driver.find_element(by=By.ID, value='username')
        text_area1.clear()
        text_area1.send_keys(self.email)
        time.sleep(1)


        text_area = self.driver.find_element(by=By.ID, value='password')
        text_area.clear()
        text_area.send_keys(self.password)
        text_area.send_keys(Keys.ENTER)
        time.sleep(1)

    def checkLinkedinLogin(self):
        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        return self.check_exists_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " logged-out")]')

    def searchCompany(self):
        time.sleep(2)
        try:

            self.actions = ActionChains(self.driver)
            search = self.driver.find_element(by=By.XPATH, value="//input[@placeholder = 'Search']")
            content = self.getListKeywords()
            time.sleep(1)

            # Random KeywordList
            Company = random.choice(content)

            search.send_keys(Company)
            time.sleep(1)
            search.send_keys(Keys.ENTER)
            time.sleep(3)

            Companies = self.driver.find_element(by=By.XPATH, value="//button[text()='Companies']")
            Companies.click()
            time.sleep(1)
            Company_link = self.driver.find_element(by=By.XPATH, value="//img[@class = 'ivm-view-attr__img--centered EntityPhoto-square-3  lazy-image ember-view']")
            Company_link.click()
            time.sleep(3)
            posts_link = self.driver.find_element(by=By.XPATH, value="//a[text() = 'Posts']")
            posts_link.click()

        except NoSuchElementException as e:
            print("Error in searchKeyword: " + str(e))
        except Exception as i:
            print("Uncontrolled error: " + str(i))

    def likePost(self):
        time.sleep(2)
        try:
            # Most Recent posts
            posts_to_like = self.driver.find_elements(by=By.XPATH, value="//div/li-icon[contains(@type, 'thumbs-up-outline')]")
            print(posts_to_like)
            for post in posts_to_like:
                post.click()
                time.sleep(2)

        except Exception as e:
            ("Uncontrolled error: " + str(e))

    def getListKeywords(self):
        try:
            # Content of the listKeywords.txt
            content = [x.strip() for x in self.contentFile]
            return content
        except Exception as e:
            # print(e)
            input("Press any key to continue...")

if __name__ == "__main__":

      # Initialize
      lBot = LinkedinBot()
      lBot.LinkedinLogin()

      lBot.searchCompany()
      lBot.likePost()


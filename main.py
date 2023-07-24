from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import constants as cos
import time

class github(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        os.environ['PATH'] += cos.path
        super(github, self).__init__()

    def webpage_url(self):
        self.get(cos.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def rep_link_click(self):
        time.sleep(3)
        repos = self.find_element(By.CSS_SELECTOR, cos.repositories_tab)
        repos.click()
        time.sleep(2)

    def repos_click(self):
        self.reps = self.find_elements(By.CSS_SELECTOR, cos.repositories_list)
        self.reps = [x.text for x in self.reps]
        print(self.reps)
        time.sleep(2)

    def repos_data(self):
        for x in self.reps:
            self.implicitly_wait(30)
            rep = self.find_element(By.CSS_SELECTOR, f'a[href*="/SamQxd/{x}"]')
            rep.click()
            time.sleep(3)

            try:
                # Execute the script using pure JavaScript
                repository_id = self.execute_script(cos.repository_id)
                info = self.execute_script('return document.title')

            except Exception as e:
                print("An error occurred:", str(e))

            print(x,"|", repository_id,"|", info)

            self.implicitly_wait(30)

            def download_button_click():
                download_button = self.find_element(By.CSS_SELECTOR, cos.download_button)
                download_button.click()
                time.sleep(3)

            download_button_click()

            download_zip = self.find_element(By.CSS_SELECTOR, f'a[href*="/SamQxd/{x}/archive/refs/heads/main.zip"]')
            download_zip.click()

            download_button_click()

            self.implicitly_wait(30)
            back = self.find_element(By.CSS_SELECTOR, cos.account)
            back.click()
            time.sleep(3)

            self.implicitly_wait(30)
            repositories = self.find_element(By.CSS_SELECTOR, cos.repositories_tab)
            repositories.click()
            time.sleep(3)











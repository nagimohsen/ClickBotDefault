from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import inspect
from selenium.webdriver.chrome.options import Options

class WebDriver:

    def __init__(self,proxy='36.89.191.73:23500',use_proxy=False):
        self.project_dir = os.path.dirname(__file__)
        
        self.chromedriver_path = os.path.join(self.project_dir, 'chromedriver')
        
        self.chrome_options = Options()
        self.chrome_options.add_argument('log-level=3')
        self.proxy_to_use=proxy
        if use_proxy:
            self.chrome_options.add_argument('--proxy-server=http://%s' % self.proxy_to_use)
        else:
            pass
        self.chrome_options.add_argument('--disable-infobars')
        self.driver = webdriver.Chrome(self.chromedriver_path, options=self.chrome_options)
        self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(180)
        self.driver.set_script_timeout(500)
        self.driver.maximize_window()

    def wait_until_page_loaded(self):
        return WebDriverWait(self.driver, 20).until(lambda driver:
                                                    driver.execute_script('return document.readyState'))

    def wait_until_ajax_response(self):
        return WebDriverWait(self.driver, 20).until(lambda driver:
                                                    driver.execute_script(
                                                        'return !!window.jQuery && jQuery.active == 0'))

    def wait_until_page_url(self, url):
        return WebDriverWait(self.driver, 20).until(lambda driver:
                                                    driver.current_url.startswith(url))

    def wait_until_page_url_not(self, url):
        return WebDriverWait(self.driver, 20).until(lambda driver:
                                                    not driver.current_url.startswith(url))

    def wait_until_page_url_ends_with(self, url):
        return WebDriverWait(self.driver, 20).until(lambda driver:
                                                    driver.current_url.endswith(url))

    def send_slow_key(self, element=None, keys=None):
        for key in keys:
            element.send_keys(key)
            time.sleep(0.1)

    def wait_element(self, by=None, element=None):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((by, element)))

    def get_element(self, by=None, element=None):
        return self.driver.find_element(by, element)

    def get_parent_node(self, by=None, element=None, n=1):
        element = self.get_element(by, element)
        repeated_str = ''
        for i in range(n):
            repeated_str = repeated_str + '.parentNode'
        script = 'return arguments[0]{};'.format(repeated_str)
        return self.driver.execute_script(script, element)

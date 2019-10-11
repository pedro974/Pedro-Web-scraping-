from selenium import webdriver


class google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com.br'
    def navigate(self):
        self.driver.get(self.url)


        
gg = webdriver.Chrome()
g = google(gg)
g.navigate()

b = gg.find_element_by_name('q')
print(b)
b.send_keys('Gostoso')


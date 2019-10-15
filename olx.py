from selenium import  webdriver
import csv
#f = open('olx.csv','w')
class google:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'https://www.olx.com.br'
        self.search_b = 'q'
        self.pesquisar_boton = 'submitBtn'              
        self.titulo= 'OLXad-list-title' #class titulo
        self.local = 'text detail-region' #classe local
        self.categoria = 'text detail-category' #class categoria
        self.preco = 'OLXad-list-price' #class preco
        self.horario = 'col-4' #class horario
    def navigate(self):
         self.driver.get(self.url)
    def search(self, word = 'None'):
        self.driver.find_element_by_name(self.search_b).send_keys(word)
        self.driver.find_element_by_class_name(self.pesquisar_boton).click()
    def printx(self):
        a =self.driver.find_elements_by_class_name(self.titulo)
        for g in a:
                t =()
                gx = g.text
                f =[gx]
                t = f
                print(t)
        b =self.driver.find_elements_by_class_name(self.preco)
        c =self.driver.find_elements_by_class_name(self.local)
        d =self.driver.find_elements_by_class_name(self.horario)
        e =self.driver.find_elements_by_class_name(self.categoria)
        h = [a,b,c,d,e]
       
        

         

        
        
                    
  
  
gg = webdriver.Chrome() #abre o driver
g = google(gg) #abre o google
g.navigate() #abre navegador
g.search('Celular') #c
g.printx()
gg.close()
#f = csv.write(f)
#write.writerow(gx)
f.close()

"""for local in c:
#print(local.text)
for horario in d:
#print(horario.text)
for categoria in f:""
                            """

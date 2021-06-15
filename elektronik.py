import pandas as pd
import requests
from bs4 import BeautifulSoup
from ftfy import fix_encoding

# Lesson hours
hours = []

# Days
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []

# CTR
lista = []
lista_href = []

# Scrapping - Scrap lesson table
def fetch_table(query):
   return pd.read_html("http://plan.elektronik.edu.pl/" + lista_href[lista.index(query)])
def scrap_table(plan):
   plan = plan[2].values.tolist()
   for i in plan:
      iter = 0
      for x in i:
         if iter == 0:
            pass
         if iter == 1:
            hours.append(x)
         if iter == 2:
            d1.append(x)
         if iter == 3:
            d2.append(x)
         if iter == 4:
            d3.append(x)
         if iter == 5:
            d4.append(x)
         if iter == 6:
            d5.append(x)
         iter = iter + 1

# Scrapping - Scrap CTR List
def fetch_list():
   return  requests.get("http://plan.elektronik.edu.pl/lista.html")
def scrap_list(plan2):
   plan2 = BeautifulSoup(plan2.text, 'html.parser')
   plan2 = plan2.findAll('a')
   for i in plan2:
      lista_href.append(i.get('href'))
      lista.append(fix_encoding(i.get_text()))

# Outputs - List of Classes, Teachers and Rooms (links)
def href_list():
   scrap_list(fetch_list())
   return lista_href

# Outputs - List of Classes, Teachers and Rooms (pure text)
def text_list():
   scrap_list(fetch_list())
   return lista

def text2href(query):
   scrap_list(fetch_list())
   return lista_href[lista.index(query)]

# Outputs - Main query, returns data from lesson table
def query(query, data):
   output = []
   # Scrap CTR List
   try:
      scrap_list(fetch_list())
   except:
      print("Error connecting to the site !")
   # Scrap Class Table
   try:
      scrap_table(fetch_table(query))
   except:
      print("Error connecting to the site !")
   if data == "all":
      return alltable()
   if type(data) == list:
      for i in data:
         output.append(eval(i))
      return output
   else:
      return eval(data)

# Outputs - Return all data scrapper can handle (support for query())
def alltable():
   output = []
   output.append(hours)
   output.append(d1)
   output.append(d2)
   output.append(d3)
   output.append(d4)
   output.append(d5)
   return output

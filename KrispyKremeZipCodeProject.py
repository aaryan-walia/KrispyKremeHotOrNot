# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:26:10 2022

@author: aarya
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

#########################################
#################
#Coded by Aaryan Walia
#This project was designed with Python, originally coded on Spyder, this project
#Took nearly 8 hours for me to learn how to use selenium(A library you will need for this code)
#and to be able to code this project


#You will need to import the selenium library, I use Anaconda so the import was much easier for me


#Project Description: Python has a multitude of uses, and I wanted to code something
#that can help with something I'm interested in: Donuts! This project also helped
#teach me how to webscrape, and how to do it with some finesse! The user will 
#enter their zip code, and then will be given the code nearest to them

#The inspiration I had became the groundwork for me to make this project

#Why this project uses Zip Code: It was an additional challenge for me to code that
#in, and I enjoyed doing it! You could re-purpose this code and make it work
#with cities or even states as well!

#Let me know of any errors, and I will do my best to work on them!

#################
#########################################



search_url_kk_incomplete = "https://krispykreme.com/shop/order-select-store?location="
#incomplete url above, the zip code is added, which makes it complete



def getZipCode():
    condition_five_zip_code = False
    while condition_five_zip_code == False: #start of while loop to test Zip Code
    #The conditional boolean to check for a valid zip code
        try:
            zip_code = int(input("Enter the Zip Code nearest to you! : "))
            if (len(str(zip_code)) == 5) and (zip_code >= 1) and (zip_code <= 99950):
            #Zip Code must be 5 numbers long, and must be a valid integer between 1 and 99950
                condition_five_zip_code = True
                return str(zip_code)
            else:
                print("Error, Zip Code Invalid")
                condition_five_zip_code = False
        except ValueError:
                print("Error, Zip Code Invalid")
                condition_five_zip_code = False
#When the condition becomes True, the loop ends, or else it keeps going till a valid Zip Code is entered

print("Find out if your Krispy Cream has the hot sign on!")
#Title Message

zip_code = getZipCode()
print("")
#runs the getZipCode function and acquires a valid zip code

search_url_kk_complete = "https://krispykreme.com/shop/order-select-store?location=" + zip_code
#the complete URL that the code scrapes data from, the zip code is autofilled
    #in the location bar and the resulting website is printed

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#makes it so that the user can't see a web page being opened

KrispyKremeWebPage = webdriver.Chrome(r"YOUR PATH TO CHROMEDRIVER", options = options)
#The address will be changed for you to wherever your chromedriver.exe is
KrispyKremeWebPage.implicitly_wait(30)
KrispyKremeWebPage.get(search_url_kk_complete)
#opens the web page, and waits 30 seconds to see if the zip code can produce anything


try:
    content = KrispyKremeWebPage.find_element(By.CSS_SELECTOR, 'section.order-store .shop-search-container .locations-container .location-card .btn-hotlight')
    checker = content.text
    address = KrispyKremeWebPage.find_element(By.CSS_SELECTOR, 'section.order-store .shop-search-container .locations-container .location-card address')
    address_checker = address.text
    print("The nearest Krispy Kreme within your zip code is {}, and it currently has its {}!".format(address_checker, checker))
        
except:
    print("There is no Krispy Kreme near you, enter a different zip code! (Run code again)")

KrispyKremeWebPage.close()


    

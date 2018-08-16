#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

is_webdriver_loaded = False
is_user_logged_in = False
driver = None

def get_input():
    global driver
    to_be_returned_value = input()
    if to_be_returned_value == "EXIT":
        if driver != None:
            driver.close() 
        print("Bye!")
        exit()
    
    return to_be_returned_value

def app_method_2():
    global driver
    print("Loading https://web.whatsapp.com/ ...")
    driver.get("https://web.whatsapp.com/")
    print("... Done!")

    print("Checking whether user has already logged in or not...")
    is_user_logged_in = False
    
    while True:
        try:
            scan_image = driver.find_element(By.XPATH, "//img[@alt='Scan me!']")
            is_user_logged_in = False
        except NoSuchElementException:
            is_user_logged_in = True
            break

        if is_user_logged_in == False:
            print("Please log in to WhatsApp via phone and then enter anything to continue")
            get_input()
    
    while True:
        
        is_contact_located = False
        print("Enter name of the person : ")
        contact_name = get_input()
        contact_name_card = None
        try:

            placeholder_maal = driver.find_element(By.XPATH,"//button[@class='C28xL']")
            placeholder_maal.click()

            contact_search_field = driver.find_element(By.XPATH, "//input[@class='jN-F5 copyable-text selectable-text']")
            contact_search_field.click()
            contact_search_field.send_keys(contact_name)
            contact_search_field.click()
            contact_search_field.send_keys(Keys.RETURN)
            
            main_contact_card = driver.find_element(By.XPATH, "//span[@title='"+contact_name+"']")
            
            is_contact_located = True
        except NoSuchElementException:
            is_contact_located = False

        if is_contact_located == False:
            print("There is no such Contact... Please Try Again!")
        else:                
            print("Enter Spam Message : ")
            spam_msg = get_input()
            print("Enter no of times to send : ")
            no_of_times_to_send = int(get_input())

            print("*********************************************************")
            print("                      ATTACK SUMMARY")
            print("Victim : "+contact_name)
            print("Spam Message : "+spam_msg)
            print("No. of times to send : "+str(no_of_times_to_send))
            print("*********************************************************")
            print("START ATTACK ? [Y/N]")
            final_confirmation = get_input()
            
            if final_confirmation != "Y":
                print("Aborted!\n\n\n")
                continue

            try:
                text_field = driver.find_element(By.XPATH,"//div[@class='_2S1VP copyable-text selectable-text']")
                for i in range(no_of_times_to_send):
                    print("Sending message #"+str(i))
                    text_field.send_keys(spam_msg)
                    text_field.send_keys(Keys.RETURN)
                    
                print("Task Done!")
                print("SUCCESS!")
            except Exception:
                print(Exception)
                print("UNSUCCESSFUL!")

            print("Run Again? [Y/N]")
            str_input_2 = get_input()
            if(str_input_2 == "Y"):
                app_method_1()
            
            driver.close()
            print("Bye!")
            break  
        
            

    
    
    

def app_method_1():
    global driver
    global is_webdriver_loaded

    print("Checking for WebDriver...")

    if is_webdriver_loaded:
        print("Web Driver already loaded ...")
    else:
        while True:
            print("Please select any one of the Web Drivers : ")
            print("1. Mozilla FireFox (Gecko Driver)")
            input_str = get_input()
            if input_str == "1":
                print("Loading Gecko Web Driver ...")
                driver = webdriver.Firefox()
                is_webdriver_loaded = True
                print("... Done!")
                break
            else:
                print("Invalid Input!")
                print("You can enter 'EXIT' to quit ...")
    
    app_method_2()

print("*************************************************************")
print("*                       WhatsApp Bomber                     *")
print("*                         Version 1.1                       *")
print("*                  Made By Debayan Sutradhar                *")
print("*                   (ladiesman6969, DX_BETA)                *");
print("*                     OPEN SOURCE IS LOVE                   *")
print("*       https://github.com/ladiesman6969/whatsappBomber     *")
print("*                          16/08/2018                       *")     
print("*************************************************************")
app_method_1()

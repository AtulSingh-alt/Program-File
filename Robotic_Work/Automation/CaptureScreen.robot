*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
Screenshot Test
        Open Browser    https://opensource-demo.orangehrmlive.com/      chrome
        Maximize Browser Window
        #Input Text    xpath://*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input    admin
        #Input Text    xpath://*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input    admin123

        Capture Element Screenshot    xpath://*[@id="app"]/div[1]/div/div[1]/div/div[1]/img      C:/Users/atul.singh/PycharmProjects/My_robotic_work/logo.png
        Capture Page Screenshot         loginTC.png

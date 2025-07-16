*** Settings ***

Library     SeleniumLibrary


*** Test Cases ***
MultipleBrowser
        Open Browser    https://demo.nopcommerce.com/   chrome
        Maximize Browser Window

        Open Browser    https://rahulshettyacademy.com/AutomationPractice/  chrome
        Maximize Browser Window

        #Close Browser
        Close All Browsers
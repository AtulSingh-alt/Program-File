*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
HandlingAlerts
        Open Browser    https://testautomationpractice.blogspot.com/    chrome
        Maximize Browser Window
        Click Element    xpath://*[@id="confirmBtn"]    #open alert
        Sleep    3

        #Handle Alert    accept
        #Handle Alert    dismiss
        #Handle Alert     leave
        #Alert Should Be Present     Press a button!
        Alert Should Not Be Present  Press a button!



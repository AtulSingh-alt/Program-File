*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}          https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Testing Radio buttons and Check Boxes
        ${spead}=   Get Selenium Speed
        Log To Console    ${spead}
        Open Browser        ${url}      ${browser}
        Maximize Browser Window
        Set Selenium Speed    2

        #Selecting the radio buttons
        Select Radio Button    radioButton    radio1
        Select Radio Button    radioButton    radio3

        #Selecting the checkBoxes
        Select Checkbox    xpath://*[@id="checkBoxOption1"]
        Unselect Checkbox    xpath://*[@id="checkBoxOption1"]
        Select Checkbox    xpath://*[@id="checkBoxOption3"]

        #Selecting the Drop Downs
        Select From List By Label    dropdown-class-example     Option2
        #Sleep    2
        Select From List By Index    dropdown-class-example     1
        ${spead}=   Get Selenium Speed
        Log To Console    ${spead}


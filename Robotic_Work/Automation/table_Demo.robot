*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***
TableValidation
        Open Browser        https://testautomationpractice.blogspot.com/    chrome
        Maximize Browser Window
        ${rows}=    Get Element Count    xpath://*[@id="HTML1"]/div[1]/table/tbody/tr
        ${cols} =   Get Element Count    xpath://*[@id="HTML1"]/div[1]/table/tbody/tr/th
        Log To Console    ${rows}
        Log To Console    ${cols}

        ${data}=      Get Text    xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[1]
        Log To Console    ${data}

        Table Column Should Contain    xpath://*[@id="HTML1"]/div[1]/table/tbody    2    Author
        Table Row Should Contain       xpath://*[@id="HTML1"]/div[1]/table/tbody    4    Learn JS
        #Table Cell Should Contain      xpath://*[@id="HTML1"]/div[1]/table/tbody    4   2   Animesh
        Table Header Should Contain    xpath://*[@id="HTML1"]/div[1]/table/tbody    BookName
        Close Browser
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Fill Guest Details
    Wait Until Element Is Visible    xpath=//button[@actiontype='button']       timeout=10s
    Click Element    xpath=//button[@actiontype='button']

    Wait Until Element Is Enabled    xpath=//input[@id='contact.contactFirstName']
    Input Text    xpath=//input[@id='contact.contactFirstName']    ATP
    Input Text    xpath=//input[@id='contact.contactLastName']    STK
    Input Text    xpath=//input[@id='contact.contactEmail']    ats012@gmail.com

    Wait Until Element Is Visible    xpath=//button[@data-testid='shimmer-cta']
    Click Element    xpath=//button[@data-testid='shimmer-cta']
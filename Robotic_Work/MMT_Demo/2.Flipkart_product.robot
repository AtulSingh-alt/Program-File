*** Settings ***
Library     SeleniumLibrary
Test Setup  Open URL
Test Teardown   Close Browser
Test Template   Login Flipkart

*** Variables ***
${Base_URL}      https://www.flipkart.com/
${Browser}       Chrome

*** Test Cases ***
Get The Product
    Login Flipkart


*** Keywords ***
Open URL
    Open Browser    ${Base_URL}     ${Browser}
Login Flipkart
    [Arguments]     ${Mob_num}
    Maximize Browser Window
    Click Element    xpath://*[@id="container"]/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/a/div/div/div[1]/picture/img
    Sleep    2
    Click Element    xpath://*[@id="container"]/div/div[3]/div/div[2]/div[3]/div/div[1]/div/a/div[1]/div/div/div/img
    Sleep    2
    Switch Window   xpath://*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]c
    Sleep    5
    ${text}     Page Should Contain    Men Flip Flops  (Multicolor , 9)
    Log To Console    ${text}
#    ${Text}=    Get Text    xpath://*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]
#    Log To Console    ${Text}
    Sleep    10

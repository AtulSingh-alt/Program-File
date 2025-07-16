*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${Url}      https://demo.itlearn360.com/
${Browser}  Chrome
${Time}     10 seconds
${User}     Demo12
${Password}     Test123456$

*** Test Cases ***
ElearningWebsite
    Itlearn360 Login Code



*** Keywords ***
Itlearn360 Login Code
    Open Browser    ${Url}    ${Browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    ${Time}
    Click Element    id:loginlabel
    Input Text    id:user_login    ${User}
    Input Text    id:user_pass    ${Password}
    Click Element    id:wp-submit

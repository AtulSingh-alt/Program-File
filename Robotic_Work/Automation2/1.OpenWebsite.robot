*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***
ElearningWebsite
    Open Browser    https://demo.itlearn360.com/    Chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10seconds
    Click Element    id:loginlabel
    Input Text    id:user_login    Demo12
    Input Text    id:user_pass    Test123456$
    Click Element    id:wp-submit
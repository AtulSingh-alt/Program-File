*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***
GoogleTest
    Open Browser    https://demo.nopcommerce.com/   chrome
    Click Link    xpath://a[@class='ico-login']
    Input Text    id:Email          pavanoltraining@gmail.com
    Input Text    id:Password       test@123
    Click Element    xpath://*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]
    Close Browser

*** Keywords ***
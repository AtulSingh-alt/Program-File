*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}          https://rahulshettyacademy.com/

*** Test Cases ***
LoginTest
        Open Browser    ${url}      ${browser}
        Maximize Browser Window
        Click Link    xpath:/html/body/div/header/div[2]/div/div/div[2]/div[2]/a
        Input Text    id:email    atulat@gmail.com
        Click Element    xpath://*[@id="otp-login-btn"]/span
        Close Browser

***Keywords***


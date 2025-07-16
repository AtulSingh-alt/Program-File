*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/resources.robot

*** Variables ***
${url}          https://rahulshettyacademy.com/
${browser}      chrome

*** Test Cases ***
UserDefinedKeywords Test
        ${PageTitle}=    LaunchBrowser   ${url}      ${browser}
        Log To Console    ${PageTitle}
        Log    ${PageTitle}
        Click Element    xpath:/html/body/div/header/div[2]/div/div/div[2]/div[2]/a




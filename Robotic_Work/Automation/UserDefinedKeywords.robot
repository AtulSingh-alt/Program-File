*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}          https://rahulshettyacademy.com/
${browser}      chrome

*** Test Cases ***
UserDefinedKeywords Test
        LaunchBrowser
        Click Element    xpath:/html/body/div/header/div[2]/div/div/div[2]/div[2]/a

*** Keywords ***
LaunchBrowser
        Open Browser        ${url}      ${browser}
        Maximize Browser Window


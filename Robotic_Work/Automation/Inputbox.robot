*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}          https://rahulshettyacademy.com/

*** Test Cases ***
TestingInputBox
        Open Browser        ${url}      ${browser}
        Maximize Browser Window
        Title Should Be    Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy
        Click Link    xpath:/html/body/div/header/div[2]/div/div/div[2]/div[2]/a
        ${"email_txt"}  Set Variable    id:email
        
        Element Should Be Visible    ${"email_txt"}
        Element Should Be Enabled    ${"email_txt"}

        Input Text    ${"email_txt"}    atbhai@gmail.com
        Sleep    5
        Clear Element Text    ${"email_txt"}
        Sleep    3
        Close Browser




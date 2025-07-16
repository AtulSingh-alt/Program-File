*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${LOGIN URL}        https://admin-demo.nopcommerce.com/
${BROWSER}          chrome

*** Keywords ***
Open my Browser
    Open Browser        ${LOGIN URL}        ${BROWSER}
    Maximize Browser Window

Close Browsers
    Close All Browsers

Open Login Page
    Go To    ${LOGIN URL}

Input Username
    [Arguments]     ${username}
    Input Text    xpath://*[@id="Email"]    ${username}

Input pwd
    [Arguments]     ${password}
    Input Text    xpath://*[@id="Password"]    ${password}

click login button
    Click Element    xpath://*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button

click logout link
    Click Link    xpath://*[@id="navbarText"]/ul/li[3]/a

Error message should be visible
    Page Should Contain    Login was unsuccessful.

Dashboard page should be visible
    Page Should Contain    Dashboard
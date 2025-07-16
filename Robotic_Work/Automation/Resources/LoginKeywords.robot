*** Settings ***
Library     SeleniumLibrary
Variables   ../PageObjects/Locators.py


*** Keywords ***
Open My Browser
    [Arguments]     ${SiteUrl}      ${Browser}
    Open Browser    ${SiteUrl}      ${Browser}
    Maximize Browser Window

Enter UserName
    [Arguments]     ${username}
    Input Text      ${txt_loginUserName}    ${username}

Enter Password
    [Arguments]     ${password}
    Input Text    ${txt_loginpassword}    ${password}

Click SignIn
    Click Button    ${btn_signin}

Verify Successfull Login
    Element Should Be Visible    //div[@class="content-header"]

close my browser
    Close All Browsers
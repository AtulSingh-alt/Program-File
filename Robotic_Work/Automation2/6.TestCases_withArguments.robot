*** Settings ***
Library     SeleniumLibrary
Test Setup      Open the Url
Test Teardown   Close Browser


Resource    4.resource.robot

*** Variables ***
${Time}     10 seconds
${User}     Demo12
${Password}     Test123456$

*** Test Cases ***
ElearningWebsite
    Itlearn360 Login Code   ${User}     ${Password}



*** Keywords ***
Itlearn360 Login Code
    [Arguments]     ${User}     ${Password}
    Maximize Browser Window
    Set Selenium Implicit Wait    ${Time}
    Click Element    id:loginlabel
    Input Text    id:user_login    ${User}
    Input Text    id:user_pass    ${Password}
    Click Element    id:wp-submit
    Element Text Should Be    xpath://*[@id="login-list"]/li[1]/a    Dashboard

    ${alllinks} =   Get Element Count    xpath://a
    Log To Console    ${alllinks}


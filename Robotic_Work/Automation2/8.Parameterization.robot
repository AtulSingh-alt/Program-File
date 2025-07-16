*** Settings ***
Library     SeleniumLibrary
Test Setup      Open the Url
Test Teardown   Close Browser
Resource    4.resource.robot
Test Template   Itlearn360 Login Code

*** Variables ***
${Time}     10 seconds
${User}     Demo12
${Password}     Test123456$

*** Test Cases ***      username    password
Invalid username        Demo1234    Test123456$
Invalid password        Dem012      Test12344454
Invalid characters      abc@#       Test123456$



*** Keywords ***
Itlearn360 Login Code
    [Arguments]     ${username}     ${password}
    Maximize Browser Window
    Set Selenium Implicit Wait    ${Time}
    Click Element    id:loginlabel
    Input Text    id:user_login    ${username}
    Input Text    id:user_pass    ${password}
    Click Element    id:wp-submit

    ${alllinks} =   Get Element Count    xpath://a
    Log To Console    ${alllinks}

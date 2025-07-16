*** Settings ***
Library     SeleniumLibrary
Test Setup  Open URL
Test Teardown   Close Browser
Test Template   Login Flipkart

*** Variables ***
${Base_URL}      https://www.flipkart.com/
${Browser}       Chrome

*** Test Cases ***      ${Mob_num}
Login Scenario_1        9098779876
Login Scenario_2        8768779876
Login Scenario_3        7898779876
Login Scenario_4        5598779876


*** Keywords ***
Open URL
    Open Browser    ${Base_URL}     ${Browser}
Login Flipkart
    [Arguments]     ${Mob_num}
    Maximize Browser Window
    Click Element    xpath://*[@id="container"]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[2]/div[2]/div/div/div/div/a/span
    Input Text      xpath://*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input    ${Mob_num}
    Click Element    xpath://*[@id="container"]/div/div[3]/div/div[2]/div/form/div[3]/button
    Sleep    2

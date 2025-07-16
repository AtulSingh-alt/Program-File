*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/login_resources.robot
Library     DataDriver  ../TestData/NEW.xlsx    sheet_name=Sheet1

Suite Setup     Open my Browser
Suite Teardown      Close Browsers

*** Test Cases ***
LoginTestwithExcel using ${username} and ${password}



*** Keywords ***
Invalid login
    [Arguments]     ${username}     ${password}
    Input Username    ${username}
    Input pwd    ${password}
    click login button
    Error message should be visible
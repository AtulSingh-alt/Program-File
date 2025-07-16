*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/LoginKeywords.robot

*** Variables ***
${browser}  chrome
${SiteUrl}  https://admin-demo.nopcommerce.com/
${user}     admin@yourstore.com
${pwd}      admin

*** Test Cases ***
LoginTest
    Open My Browser    ${SiteUrl}    ${browser}
    Enter UserName    ${user}
    Enter Password    ${pwd}
    Click SignIn
    Sleep    20s
    Verify Successfull Login
    close my browser
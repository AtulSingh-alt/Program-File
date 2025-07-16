*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/RegistrationKeywords.robot

*** Variables ***
${SiteUrl}      https://www.facebook.com/
${Browser}      chrome

*** Test Cases ***
RegistrationTest
    Open My Browser     ${SiteUrl}      ${Browser}
    Click Register link
    Enter FirstName     Ashu
    Enter LastName      Singh
    Enter DOB Day       16
    Enter DOB Month     05
    Enter DOB Year      1981
    Select Gender       Male
    Enter Phone         9887897656
    Enter Password      rdfghjk54@
    Click Submit
    Verify Succesful Registration
    Close my browser

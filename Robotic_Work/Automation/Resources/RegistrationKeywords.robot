*** Settings ***
Library     SeleniumLibrary
Variables   ../PageObjects/Locators.py

*** Keywords ***
Open My Browser
    [Arguments]     ${SiteUrl}      ${Browser}
    Open Browser    ${SiteUrl}      ${Browser}
    Maximize Browser Window

Click Register link
    Click Link    ${link_Reg}

Enter FirstName
    [Arguments]     ${firstname}
    Input Text    ${txt_firstname}    ${firstname}

Enter LastName
    [Arguments]     ${lastname}
    Input Text    ${txt_lastname}    ${lastname}

Enter DOB Day
    [Arguments]     ${day}
    Select From List By Label    ${txt_day}     ${day}

Enter DOB Month
    [Arguments]     ${month}
    Select From List By Label    ${txt_month}     ${month}

Enter DOB Year
    [Arguments]     ${year}
    Select From List By Label    ${txt_year}     ${year}

Select Gender
    [Arguments]     ${gender}
    Select Radio Button    ${txt_gender}    ${gender}

Enter Phone
    [Arguments]     ${phone}
    Input Text    ${txt_phone}    ${phone}

Enter Password
    [Arguments]     ${password}
    Input Text    ${txt_password    ${password}

Click Submit
    Click Button    ${txt_submit}

Verify Succesful Registration
    Page Should Contain    facebook

Close my browser
    Close All Browsers
*** Settings ***
Library     SeleniumLibrary
Library    String
Library    Collections

Test Teardown   Close Browser

*** Variables ***
${BASE_URL}     https://www.agoda.com/en-in/
${BROWSER}      Chrome
@{HOTEL_NAMES}
@{HOTEL_PRICES}
&{HOTEL_KEY_VALUE}


*** Test Cases ***
AGODA Full Flow
        Happy Flow



*** Keywords ***
Happy Flow
    Open Browser        ${BASE_URL}     ${BROWSER}
    Maximize Browser Window
    Input Text    xpath=//input[contains(@data-selenium,'textInput')]    Delhi
    Wait Until Element Is Visible    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]
    Click Element    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]

    Wait Until Element Is Visible    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Click Element    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Wait Until Element Is Visible    xpath=//button[contains(@data-selenium,'searchButton')]/div/div/span
    Click Element    xpath=//button[contains(@data-selenium,'searchButton')]/div/div/span

    ${hotel_count}=     Get Element Count    xpath=//h3[contains(@data-selenium,'hotel-name')]

    FOR    ${i}    IN RANGE    0    25
        Execute Javascript  window.scrollBy(0,1000)
        Sleep    4
        ${hotel_count}=     Get Element Count    xpath=//h3[contains(@data-selenium,'hotel-name')]
    END
    Log To Console    Total Hotels counts:${hotel_count}
    Sleep    5

    #Get hotel name
    ${name}=      Get WebElements    xpath=//h3[contains(@data-selenium,'hotel-name')]
    ${price}=     Get WebElements    xpath=//span[contains(@data-selenium,'display-price')]

    FOR    ${i}    IN RANGE    0    25
        ${hotel_name_text}=  Get Text    ${name[${i}]}
        ${hotel_name_strip}=  Replace String    ${hotel_name_text}    ,    ${EMPTY}
        ${hotel_name}=  Convert To String    ${hotel_name_strip}
        Append To List    ${HOTEL_NAMES}    ${hotel_name}

        ${price_value}=     Get Text    ${price[${i}]}
        ${price_new}=   Replace String    ${price_value}    ,    ${EMPTY}
        ${hotel_price}=     Convert To Integer    ${price_new}
        Append To List    ${HOTEL_PRICES}   ${hotel_price}
        Set To Dictionary    ${HOTEL_KEY_VALUE}         ${hotel_name}=${hotel_price}
    END
    Log To Console    ${HOTEL_KEY_VALUE}


    #Sort the price
    Sort List    ${HOTEL_PRICES}
    Log To Console    ${HOTEL_PRICES}

    #Get Cheapest price
    ${cheapest}=    Get From List    ${HOTEL_PRICES}    0

#    FOR    ${i}    IN    @{HOTEL_NAMES}
#        ${price_match}=     Get From Dictionary    ${HOTEL_KEY_VALUE}    ${i}
#        Run Keyword If    '${price_match}' == '${cheapest}'    Log To Console    The cheapest Hotel: ${i} - ₹${price_match}
#
#    END

    FOR    ${index}    IN RANGE    0    25
        ${hotel_name}=    Get From List    ${HOTEL_NAMES}    ${index}
        ${hotel_price}=   Get From Dictionary    ${HOTEL_KEY_VALUE}    ${hotel_name}
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Scroll Element Into View    xpath=(//h3[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Sleep    2
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Click Element    xpath=(//h3[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Log To Console    Opening cheapest Hotel: ${hotel_name} - ₹${hotel_price}
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Exit For Loop
    END
    Sleep    5
    Switch Window   NEW

    Click Element    xpath=//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 fLRAkl']/div/button

    Wait Until Element Is Visible    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[19]
    Click Element    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[19]
    Sleep    5
    Click Element    xpath=//div[@data-element-name='hotel-gallery-close-button']
    Sleep    5

    Wait Until Element Is Visible    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]
    Click Element    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]
    Sleep    5
    Click Element    xpath=(//div[@class='Box-sc-kv6pi1-0 iyqcnt ChildRoomsList-reserveNow'])[1]

    Sleep    10

    Wait Until Element Is Visible    xpath=//button[@actiontype='button']
    Click Element    xpath=//button[@actiontype='button']
#    Scroll Element Into View    xpath=//button[@actiontype='button']
#    Click Element    xpath=//button[@actiontype='button']
    Sleep    3
#    FOR    ${i}    IN RANGE    0    10
#        Execute Javascript  window.scrollBy(0,1000)
#        Sleep    4
#    END

    Wait Until Element Is Enabled    xpath=//input[@id='contact.contactFirstName']
    Input Text    xpath=//input[@id='contact.contactFirstName']    ATS
    Input Text    xpath=//input[@id='contact.contactLastName']    STA
    Wait Until Element Is Visible    xpath=//input[@id='contact.contactEmail']
    Input Text    xpath=//input[@id='contact.contactEmail']    ats12@gmail.com
#    Select From List By Label    xpath=//select[@searchplaceholdertext='Search']    India
#    Wait Until Element Is Visible    xpath=(//span[@class='sc-eDDNvR Typographystyled__TypographyStyled-sc-1uoovui-0 dVAttZ lfSBCC FormFieldstyled__InputTypographyStyled-sc-11x6xcu-1 kUuTYs'])[5]
#    Input Text    xpath=(//span[@class='sc-eDDNvR Typographystyled__TypographyStyled-sc-1uoovui-0 dVAttZ lfSBCC FormFieldstyled__InputTypographyStyled-sc-11x6xcu-1 kUuTYs'])[5]    8765435678
#    Sleep    5
#    Wait Until Element Is Visible    xpath=(//label[@data-element-name='Smoking']/div)[1]
#    Select Radio Button    xpath=(//label[@data-element-name='Smoking']/div)[1]    Smoking
    Wait Until Element Is Visible    xpath=//button[@data-testid='shimmer-cta']
    Click Element    xpath=//button[@data-testid='shimmer-cta']
    Sleep    10
*** Settings ***
Library           SeleniumLibrary
Library           String
Library           Collections

Test Setup        Open Browser To Agoda
Test Teardown     Close Browser

*** Variables ***
${BASE_URL}       https://www.agoda.com/en-in/
${BROWSER}        Chrome
@{HOTEL_NAMES}
@{HOTEL_PRICES}
&{HOTEL_KEY_VALUE}

*** Test Cases ***
Verify Agoda Booking Flow
    Search Hotels In Delhi
    Collect Hotel Details
    Sort Hotels By Price
    Open Cheapest Hotel
    Select Room And Proceed To Booking
    Fill Guest Details And Continue

*** Keywords ***

Open Browser To Agoda
    Open Browser        ${BASE_URL}     ${BROWSER}
    Maximize Browser Window

Search Hotels In Delhi
    Input Text    xpath=//input[contains(@data-selenium,'textInput')]    Delhi
    Wait Until Element Is Visible    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]
    Click Element    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]
    Wait Until Element Is Visible    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Click Element    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Wait Until Element Is Visible    xpath=//button[contains(@data-selenium,'searchButton')]
    Click Element    xpath=//button[contains(@data-selenium,'searchButton')]

Collect Hotel Details
    FOR    ${i}    IN RANGE    0    10
        Execute Javascript    window.scrollBy(0,1000)
        Sleep    2
    END
    ${name_elements}=      Get WebElements    xpath=//h3[contains(@data-selenium,'hotel-name')]
    ${price_elements}=     Get WebElements    xpath=//span[contains(@data-selenium,'display-price')]

    FOR    ${i}    IN RANGE    0    10
        ${hotel_name}=    Get Text    ${name_elements[${i}]}
        ${clean_name}=    Replace String    ${hotel_name}    ,    ${EMPTY}
        Append To List    ${HOTEL_NAMES}    ${clean_name}

        ${hotel_price_text}=    Get Text    ${price_elements[${i}]}
        ${clean_price}=    Replace String    ${hotel_price_text}    ,    ${EMPTY}
        ${hotel_price}=    Convert To Integer    ${clean_price}
        Append To List    ${HOTEL_PRICES}    ${hotel_price}

        Set To Dictionary    ${HOTEL_KEY_VALUE}    ${clean_name}=${hotel_price}
    END

Sort Hotels By Price
    Sort List    ${HOTEL_PRICES}
    ${cheapest}=    Get From List    ${HOTEL_PRICES}    0
    Set Suite Variable    ${CHEAPEST_PRICE}    ${cheapest}

Open Cheapest Hotel
    FOR    ${index}    IN RANGE    0    10
        ${hotel_name}=    Get From List    ${HOTEL_NAMES}    ${index}
        ${hotel_price}=   Get From Dictionary    ${HOTEL_KEY_VALUE}    ${hotel_name}
        Run Keyword If    '${hotel_price}' == '${CHEAPEST_PRICE}'    Scroll Element Into View    xpath=(//h3[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${CHEAPEST_PRICE}'    Click Element    xpath=(//h3[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${CHEAPEST_PRICE}'    Exit For Loop
    END
    Switch Window    NEW
    Sleep    3

Select Room And Proceed To Booking
    Click Element    xpath=//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 fLRAkl']/div/button
    Wait Until Element Is Visible    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[19]
    Click Element    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[19]
    Sleep    2
    Click Element    xpath=//div[@data-element-name='hotel-gallery-close-button']
    Wait Until Element Is Visible    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]
    Click Element    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]
    Click Element    xpath=(//div[@class='Box-sc-kv6pi1-0 iyqcnt ChildRoomsList-reserveNow'])[1]
    Sleep    3

Fill Guest Details And Continue
    Wait Until Element Is Visible    xpath=//button[@actiontype='button']
    Click Element    xpath=//button[@actiontype='button']
    Wait Until Element Is Enabled    xpath=//input[@id='contact.contactFirstName']
    Input Text    xpath=//input[@id='contact.contactFirstName']    ATS
    Input Text    xpath=//input[@id='contact.contactLastName']     STA
    Input Text    xpath=//input[@id='contact.contactEmail']        ats12@gmail.com
    Wait Until Element Is Visible    xpath=//button[@data-testid='shimmer-cta']
    Click Element    xpath=//button[@data-testid='shimmer-cta']
    Sleep    10

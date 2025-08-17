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
Full Flow
    #Check All Section
    Open Browser    ${BASE_URL}     ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//button[contains(@data-element-name,'prominent-app-download-floating-button')]      timeout=10s
    Click Element    xpath=//button[contains(@data-element-name,'prominent-app-download-floating-button')]
    Sleep    2

    ${criteria} =   Get Element Count    xpath=//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography ']
    Log To Console    ${criteria}

    FOR    ${i}    IN RANGE    1    6
        Wait Until Element Is Visible    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[${i}]
        Click Element    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[${i}]
        Sleep    2
    END
    #Happy Flow

    Wait Until Element Is Visible    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[1]
    Click Element    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[1]
    Input Text    xpath=//input[contains(@data-selenium,'textInput')]    Delhi
    Sleep    2
    Wait Until Element Is Visible    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]
    Click Element    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]

    Wait Until Element Is Visible    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Click Element    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Sleep    2
    Wait Until Element Is Visible    xpath=//button[contains(@data-selenium,'searchButton')]/div/div/span
    Click Element    xpath=//button[contains(@data-selenium,'searchButton')]/div    #/div/span

    Wait Until Element Is Visible    xpath=//a[contains(@data-selenium,'hotel-name')]       timeout=30s
    ${hotel_count}=     Get Element Count    xpath=//a[contains(@data-selenium,'hotel-name')]
    Log To Console    ${hotel_count}

    FOR    ${i}    IN RANGE    1    10
        Execute Javascript  window.scrollBy(0,1000)
        Sleep    2
        ${hotel_count}=     Get Element Count    xpath=//a[contains(@data-selenium,'hotel-name')]
    END
    Log To Console    Total Hotels counts:${hotel_count}
    Sleep    3

    #Get hotel name
    ${name}=      Get WebElements    xpath=//a[contains(@data-selenium,'hotel-name')]
    ${price}=     Get WebElements    xpath=//span[contains(@data-selenium,'display-price')]


    FOR    ${i}    IN RANGE    1    10
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

    FOR    ${index}    IN RANGE    1    10
        ${hotel_name}=    Get From List    ${HOTEL_NAMES}    ${index}
        ${hotel_price}=   Get From Dictionary    ${HOTEL_KEY_VALUE}    ${hotel_name}
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Scroll Element Into View    xpath=(//a[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Sleep    2
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Click Element    xpath=(//a[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Log To Console    Opening cheapest Hotel: ${hotel_name} - ₹${hotel_price}
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Exit For Loop
    END
    Sleep    3
    Switch Window   NEW

    Click Element    xpath=//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 fLRAkl']/div/button

    Wait Until Element Is Visible    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[19]
    Click Element    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[19]
    Sleep    3
    Click Element    xpath=//div[@data-element-name='hotel-gallery-close-button']
    Sleep    3

    Wait Until Element Is Visible    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]
    Click Element    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]
    Sleep    3
    Click Element    xpath=(//button[contains(@data-element-name,'book-btn')])[1]

    Sleep    5

    Wait Until Element Is Visible    xpath=//button[@actiontype='button']
    Click Element    xpath=//button[@actiontype='button']
    Sleep    3


    Wait Until Element Is Enabled    xpath=//input[@id='contact.contactFirstName']
    Input Text    xpath=//input[@id='contact.contactFirstName']    ATP
    Input Text    xpath=//input[@id='contact.contactLastName']    STK
    Wait Until Element Is Visible    xpath=//input[@id='contact.contactEmail']
    Input Text    xpath=//input[@id='contact.contactEmail']    ats012@gmail.com

    Wait Until Element Is Visible    xpath=//button[@data-testid='shimmer-cta']
    Click Element    xpath=//button[@data-testid='shimmer-cta']
    Sleep    10
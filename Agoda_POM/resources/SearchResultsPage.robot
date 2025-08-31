*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Collections
Resource    ../variables/variables.robot

*** Keywords ***
Wait For Hotels
    Wait Until Element Is Visible    xpath=//h3[contains(@data-selenium,'hotel-name')]    timeout=30s

Scroll And Count Hotels
    FOR    ${i}    IN RANGE    1    10
        Execute Javascript    window.scrollBy(0,1000)
        Sleep    2
    END
    ${hotel_count}=     Get Element Count    xpath=//h3[contains(@data-selenium,'hotel-name')]
    Log To Console    Total Hotels counts:${hotel_count}

Extract Hotel Names And Prices
    ${names}=    Get WebElements    xpath=//h3[contains(@data-selenium,'hotel-name')]
    ${prices}=   Get WebElements    xpath=//span[contains(@data-selenium,'display-price')]

    FOR    ${i}    IN RANGE    1    10
        ${hotel_name_text}=  Get Text    ${names[${i}]}
        ${hotel_name_strip}=  Replace String    ${hotel_name_text}    ,    ${EMPTY}
        ${hotel_name}=  Convert To String    ${hotel_name_strip}
        Append To List    ${HOTEL_NAMES}    ${hotel_name}

        ${price_text}=  Get Text    ${prices[${i}]}
        ${price_clean}=  Replace String    ${price_text}    ,    ${EMPTY}
        ${hotel_price}=  Convert To Integer    ${price_clean}
        Append To List    ${HOTEL_PRICES}   ${hotel_price}
        Set To Dictionary    ${HOTEL_KEY_VALUE}    ${hotel_name}=${hotel_price}
    END

Select Cheapest Hotel
    Sort List    ${HOTEL_PRICES}
    ${cheapest}=    Get From List    ${HOTEL_PRICES}    0
    FOR    ${index}    IN RANGE    1    10
        ${hotel_name}=    Get From List    ${HOTEL_NAMES}    ${index}
        ${hotel_price}=   Get From Dictionary    ${HOTEL_KEY_VALUE}    ${hotel_name}
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Scroll Element Into View    xpath=(//h3[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Click Element    xpath=(//h3[contains(@data-selenium,'hotel-name')])[${index + 1}]
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Log To Console    Opening cheapest Hotel: ${hotel_name} - ₹${hotel_price}
        Run Keyword If    '${hotel_price}' == '${cheapest}'    Exit For Loop
    END
    Switch Window    NEW

*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           String

Suite Setup       Open Browser To Agoda
Suite Teardown    Close Browser

*** Variables ***
${BASE_URL}             https://www.agoda.com/en-in/
${BROWSER}              Chrome
${LOCATION}             Noida
${HOTEL_NAME_LOCATOR}   //h3[@data-selenium='hotel-name']
${HOTEL_PRICE_LOCATOR}  //span[@class='PropertyCardPrice__Value']
@{HOTEL_NAMES}
@{HOTEL_PRICES}
&{HOTEL_PRICE_MAP}

*** Test Cases ***
Get Cheapest Hotel
    Search For Hotels
    Scroll Until Minimum Hotels Are Loaded    25
    Extract Hotel Names And Prices
    Display Cheapest Hotel

*** Keywords ***
Open Browser To Agoda
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.5s
    Set Selenium Timeout  10s

Search For Hotels
    Wait Until Element Is Visible    xpath=//input[@id='textInput']
    Input Text    xpath=//input[@id='textInput']    ${LOCATION}
    Wait Until Element Is Visible    xpath=//li[contains(@class, 'Suggestion')][1]
    Click Element    xpath=//li[contains(@class, 'Suggestion')][1]

    Wait Until Element Is Visible    xpath=//div[@id='check-in-box']/div/span/i
    Click Element    xpath=//div[@id='check-in-box']/div/span/i
    Wait Until Element Is Visible    xpath=//div[@id='Tabs-Container']/button/div
    Click Element    xpath=//div[@id='Tabs-Container']/button/div

Scroll Until Minimum Hotels Are Loaded
    [Arguments]    ${min_count}
    ${loaded}=    Get Element Count    ${HOTEL_NAME_LOCATOR}
#    WHILE    ${loaded} < ${min_count}
    FOR    ${i}    IN RANGE    0    ${min_count}
        Execute JavaScript    window.scrollBy(0, 1000)
#        Wait Until Keyword Succeeds    5x    2s    Element Should Be Visible    ${HOTEL_NAME_LOCATOR}
        ${loaded}=    Get Element Count    ${HOTEL_NAME_LOCATOR}
    END
    Log    Total Hotels Loaded: ${loaded}

Extract Hotel Names And Prices
    @{names}=    Get WebElements    ${HOTEL_NAME_LOCATOR}
    @{prices}=   Get WebElements    ${HOTEL_PRICE_LOCATOR}

#    ${count}=    Get Length    ${names}
#    Log    Total items to extract:clsc ${count}

    FOR    ${i}    IN RANGE    0    25
        ${hotel_name}=    Get Text    ${names[${i}]}
        ${hotel_name}=    Replace String    ${hotel_name}    ,    ${EMPTY}
        ${hotel_name}=    Convert To String    ${hotel_name}
        Append To List    ${HOTEL_NAMES}    ${hotel_name}

        ${price_text}=    Get Text    ${prices[${i}]}
        ${price_text}=    Replace String    ${price_text}    ,    ${EMPTY}
        ${price}=    Convert To Integer    ${price_text}
        Append To List    ${HOTEL_PRICES}    ${price}
        Set To Dictionary    ${HOTEL_PRICE_MAP}    ${hotel_name}=${price}
    END

    Log To Console    Hotel Names: ${HOTEL_NAMES}
#    Log    Hotel Prices: ${HOTEL_PRICES}
#    Log    Hotel-Price Map: ${HOTEL_PRICE_MAP}

Display Cheapest Hotel
    Sort List    ${HOTEL_PRICES}
    ${cheapest}=    Get From List    ${HOTEL_PRICES}    0
    Log    Cheapest Price: ₹${cheapest}

    FOR    ${hotel}    IN    @{HOTEL_NAMES}
        ${price}=    Get From Dictionary    ${HOTEL_PRICE_MAP}    ${hotel}
        Run Keyword If    '${price}' == '${cheapest}'    Log To Console    Cheapest Hotel: ${hotel} - ₹${price}
    END
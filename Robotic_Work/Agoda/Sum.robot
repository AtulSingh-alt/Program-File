*** Settings ***
Library    SeleniumLibrary
Library    String

*** Variables ***
${URL}                 http://example.com/cart
${PRODUCT1_PRICE}      xpath=//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div/a[2]/div/div[1]
${PRODUCT2_PRICE}      xpath=//*[@id="contentContainer"]/div[3]/ol[1]/li[2]/div/a/div/div[2]/div[3]/div/div[2]/aside[2]/ul/li[2]/div/span[3]
${TOTAL_PRICE}         xpath=//span[@id='total-price']

*** Test Cases ***
Verify Cart Total Matches Sum Of Product Prices
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    ${price1_text}=    Get Text    ${PRODUCT1_PRICE}
    ${price2_text}=    Get Text    ${PRODUCT2_PRICE}
    ${total_text}=     Get Text    ${TOTAL_PRICE}

    ${price1}=    Convert Price To Number    ${price1_text}
    ${price2}=    Convert Price To Number    ${price2_text}
    ${expected_total}=    Evaluate    ${price1} + ${price2}
    ${actual_total}=      Convert Price To Number    ${total_text}

    Should Be Equal As Numbers    ${expected_total}    ${actual_total}
    [Teardown]    Close Browser

*** Keywords ***
Convert Price To Number
    [Arguments]    ${price_text}
    ${cleaned}=    Strip String    ${price_text}    $    # Remove dollar sign
    ${number}=     Convert To Number    ${cleaned}
    [Return]       ${number}
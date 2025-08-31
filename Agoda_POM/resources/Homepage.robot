*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Dismiss App Popup
    Wait Until Element Is Visible    xpath=//button[contains(@data-element-name,'prominent-app-download-floating-button')]    timeout=10s
    Click Element    xpath=//button[contains(@data-element-name,'prominent-app-download-floating-button')]
    Sleep    2

Click All Sections
    ${criteria} =   Get Element Count    xpath=//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography ']
    Log To Console    ${criteria}
    FOR    ${i}    IN RANGE    1    6
        Wait Until Element Is Visible    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[${i}]
        Click Element    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[${i}]
        Sleep    2
    END

Search For City
    [Arguments]    ${city}
    Wait Until Element Is Visible    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[1]
    Click Element    xpath=(//h6[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 lcQfEu kite-js-Typography '])[1]
    Input Text    xpath=//input[contains(@data-selenium,'textInput')]    ${city}
    Sleep    2
    Click Element    xpath=(//li[contains(@data-selenium,'autosuggest-item')])[1]

Click Search
    Click Element    xpath=(//i[contains(@data-selenium,'ficon-icon-box')])[2]
    Sleep    2
    Click Element    xpath=//button[contains(@data-selenium,'searchButton')]/div

*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Handle Image Popup
    Wait Until Element Is Visible    xpath=//div[contains(@class,'GridItem__GridItemStyled-sc-3btv1u-0 fLRAkl')]/div/button     timeout=10s
    Click Element    xpath=//div[contains(@class,'GridItem__GridItemStyled-sc-3btv1u-0 fLRAkl')]/div/button
    Wait Until Element Is Visible    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[17]
    Click Element    xpath=(//div[@class='GridItem__GridItemStyled-sc-3btv1u-0 bXKJWd']/button)[17]
    Click Element    xpath=//div[@data-element-name='hotel-gallery-close-button']

Go To Cheapest Room
    Wait Until Element Is Visible    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]   timeout=10s
    Click Element    xpath=(//button[@data-element-name='jump-nav-cheapest-room-btn'])[2]

Click Book Now
    Click Element    xpath=(//button[contains(@data-element-name,'book-btn')])[1]
*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
GetAllLinksTest
        Open Browser    https://www.countries-ofthe-world.com/flags-of-the-world.html       chrome
        Maximize Browser Window
        ${AllLinksCount}=   Get Element Count    xpath://a
        Log To Console    ${AllLinksCount}

        @{AllLinksCount}    Create List
        FOR    ${i}    IN    @{AllLinksCount}
            Log    ${AllLinksCount}
        ${linkText}    Get Text    xpath:(//a)[${i}]
         Log To Console    ${linkText}


        END


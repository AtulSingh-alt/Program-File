*** Settings ***
Library     SeleniumLibrary
Library    Collections

*** Variables ***
${Base_url}     https://testautomationpractice.blogspot.com/
${Browser}      Chrome
${image}        C:/Users/atul.singh/OneDrive - SDET TECH/Pictures/download (1).jpg
${image1}       C:/Users/atul.singh/OneDrive - SDET TECH/Pictures/download (6).jpg
${source}       xpath://div[@id='draggable']/p
${Destination}      id:droppable

*** Test Cases ***
Automation Practice
    Open the browser
#    Input Fields
#    Select Gender Radio Button
#    Select Drop Down
#    Selct the list
#    Select Date1
#    Select Date2
#    Select Date3
#    Window Handle
#    Upload File
#    Upload multiple File
#    Reloading the page
#    Static Web Table
#    Dynamic Web Table
#    Pagination Web Table
#    Search Bar
#    Dynamic Button Handle
#    Alerts & Popups
#    New Tab Handle
#    POP Up Window
#    Mouse Hover Handle
#    Double click Handle
#    Drag and Drop Handle
#    Handle Slider
##    Handle SVG
#    Handle Scrolling DropDown
#    Mobile Labels
    Laptop Links



*** Keywords ***
Open the browser
    Open Browser        ${Base_url}     ${Browser}
    Maximize Browser Window
    #Sleep    5
Input Fields
    Input Text    id:name    Name
    Input Text    id:email    Email
    Input Text    id:phone    Phone
    Input Text    id:textarea    Noida, 201301
Select Gender Radio Button
    Select Radio Button    gender    male
    #Sleep    5
Select Drop Down
    Select Checkbox    id:tuesday
    Select Checkbox    id:saturday
    #Sleep    5
Selct the list
    Select From List By Value    id:country     germany
    #Sleep    5
    Select From List By Value    id:colors      green
    #Sleep    5
    Select From List By Value    id:animals     cheetah
    #Sleep    5
Select Date1
    Input Text    id:datepicker    27/08/2025
    #Sleep    5
Select Date2
    Click Element    id:txtDate
    Select From List By Value    xpath://select[@class='ui-datepicker-month']   4
    Select From List By Value    class:ui-datepicker-year       2025
Select Date3
    Click Element    xpath://a[@data-date='27']
    #Sleep    5
    Input Text    id:start-date    08/27/2025
    Input Text    id:end-date       08/30/2025
    Click Button    xpath://button[@class='submit-btn']
    #Sleep    5
Window Handle
    Click Element    xpath://a[@class='home-link']
    #Sleep    5
    Click Element    xpath://a[@class='feed-link']
    Switch Window
    #Sleep    5
Upload File
    Choose File    id:singleFileInput    ${image}
    Click Button    xpath://form[@id='singleFileForm']/button
    #Sleep    5
Upload multiple File
    Choose File    id:multipleFilesInput    ${image}
    Choose File    id:multipleFilesInput    ${image1}
    Click Button    xpath://form[@id='multipleFilesForm']/button
    #Sleep    5
Reloading the page
    Reload Page
    #Sleep    5
Static Web Table
#    Table Cell Should Contain    //table[@name='BookTable']    4    2    Animesh
#    Table Cell Should Contain    //table[@name='BookTable']    5    4    3000
#    #Sleep    5
    ${rows}=    Get WebElements    //table[@name='BookTable']//tr
    ${columns}=    Get WebElements    xpath=//table[@name='BookTable']//td
    ${headers}=    Get WebElements    xpath=//table[@name='BookTable']//th
    ${line1}=   Set Variable    ${EMPTY}
    ${line}=    Set Variable    ${EMPTY}

    FOR    ${header}    IN    @{headers}
    ${header_txt}=  Get Text    ${header}
    ${line1}=   Catenate    SEPARATOR=|    ${line1}    ${header_txt}
    END
    Log To Console    ${line1}

    FOR    ${column}    IN    @{columns}
            ${text}=    Get Text    ${column}
            ${line}=    Catenate    SEPARATOR= |    ${line}    ${text}
    END
    Log To Console    ${line}

Dynamic Web Table
    ${row1}=    Get WebElements    //table[@id='taskTable']//tr
    ${columns1}=    Get WebElements    xpath=//table[@id='taskTable']//td
    ${headers1}=    Get WebElements    xpath=//table[@id='taskTable']//th
    ${line2}=   Set Variable    ${EMPTY}
    ${line3}=    Set Variable    ${EMPTY}

    FOR    ${head}    IN    @{headers1}
    ${header_txt1}=  Get Text    ${head}
    ${line2}=   Catenate    SEPARATOR=|    ${line2}    ${header_txt1}
    END
    Log To Console    ${line2}

    FOR    ${col}    IN    @{columns1}
            ${text1}=    Get Text    ${col}
            ${line3}=    Catenate    SEPARATOR= |    ${line3}    ${text1}
    END
    Log To Console    ${line3}

Pagination Web Table
    ${total_peg}=   Get Element Count    xpath:(//ul[@class='pagination']/li/a)
    Log To Console    ${total_peg}

    FOR    ${peg}    IN RANGE    1    ${total_peg + 1}
        Click Link    xpath:(//ul[@class='pagination']/li/a)[${peg}]
        Wait Until Element Is Visible    xpath://div[@class='table-container']
        Sleep    3

        ${row_data}=    Get Element Count    xpath://div[@class='table-container']//tr
        Log To Console    ${row_data} rows on page ${peg}

        ${header_data}=     Get WebElements    xpath://div[@class='table-container']//th
        ${column_data}=     Get WebElements    xpath://div[@class='table-container']//td
        ${head_line}=   Set Variable    ${EMPTY}
        ${col_line}=    Set Variable    ${EMPTY}
        FOR    ${h}    IN    @{header_data}
            ${header_txt_peg}=  Get Text    ${h}
            ${head_line}=   Catenate    SEPARATOR=|    ${head_line}    ${header_txt_peg}
        END
        Log To Console    ${head_line}

        FOR    ${c}    IN    @{column_data}
            ${col_data_peg}=    Get Text    ${c}
            ${col_line}=    Catenate    SEPARATOR= |    ${col_line}    ${col_data_peg}
        END
        Log To Console    ${col_line}
    END

Search Bar
    Input Text    id:Wikipedia1_wikipedia-search-input    Atul
    Click Element    xpath://input[@class='wikipedia-search-button']
    Sleep    5
    Reload Page
    Sleep    5

Dynamic Button Handle
    Click Button    xpath://button[@name='start']
    Sleep    5
    Click Button    xpath://button[@name='stop']
    Sleep    5

Alerts & Popups
    Scroll Element Into View    id:alertBtn
    Click Button    id:alertBtn
    ${text}=    Alert Should Be Present
    Log To Console    ${text}
    Sleep    4

    Scroll Element Into View    id:confirmBtn
    Click Button    id:confirmBtn
    Sleep    5
    Handle Alert    action=ACCEPT
    Sleep    5

    Scroll Element Into View    id:confirmBtn
    Click Button    id:confirmBtn
    Sleep    5
    Handle Alert    action=DISMISS
    Sleep    5
    
    
    Scroll Element Into View    id:promptBtn
    Sleep    3
    Click Button    id:promptBtn
    Sleep    3
    Input Text Into Alert    Hi , I am Atul Singh
    Sleep    3
    Handle Alert    action=ACCEPT
    Sleep    3

New Tab Handle
    Wait Until Element Is Visible    xpath:(//div[@class='widget-content']/button)[5]
    Click Button    xpath:(//div[@class='widget-content']/button)[5]
    Sleep    5
    ${handles}=     Get Window Handles
    Log To Console    ${handles}
    Switch Window       ${handles}[1]
    ${Title}=   Get Title
    Log To Console    ${Title}
    Should Be Equal    ${Title}    SDET-QA Blog
    Switch Window
    Sleep    5

POP Up Window
    Wait Until Element Is Visible    id:PopUp
    Click Button    id:PopUp
    Sleep    5
    ${pop_handles}=     Get Window Handles
    Switch Window       ${pop_handles}[1]
    ${pop_title}=       Get Title
    Log To Console    ${pop_title}
    Sleep    5

Mouse Hover Handle
    Scroll Element Into View    xpath://div[@class='dropdown']/button
    Mouse Over    xpath://div[@class='dropdown']/button
    Sleep    5
    Click Element    xpath://div[@class='dropdown-content']/a[2]
    Sleep    5

Double click Handle
    Wait Until Element Is Visible    xpath://button[@ondblclick='myFunction1()']
    Double Click Element    xpath://button[@ondblclick='myFunction1()']
    Sleep    5

Drag and Drop Handle
    Drag And Drop    ${source}    ${Destination}
    Sleep    5

Handle Slider
    Scroll Element Into View    (//div[@id='slider-range']/span)[1]
    Drag And Drop By Offset    (//div[@id='slider-range']/span)[1]    50    0
    Sleep    5

    Scroll Element Into View    (//div[@id='slider-range']/span)[2]
    Drag And Drop By Offset    (//div[@id='slider-range']/span)[2]    50    0
    Sleep    5

#Handle SVG
#    Scroll Element Into View    xpath://div[@class='svg-container']
#    Click Element    xpath://div[@class='svg-container']
#    ${fill}=    Get Element Attribute    xpath://div[@class='svg-container']    fill
#    Log To Console    ${fill}
#    Should Be Equal    ${fill}    red

Handle Scrolling DropDown
    Scroll Element Into View    id:comboBox
    Click Element    id:comboBox
    Sleep    5
    FOR    ${sc}    IN RANGE    1    15
       Scroll Element Into View       (//div[@id='dropdown']/div)[${sc}]
    END

Mobile Labels
    ${Sam}=     Get Text    id:samsung
    Log To Console    ${Sam}
    ${Real}=    Get Text    id:realme
    Log To Console    ${Real}
    ${Moto}=    Get Text    id:moto
    Log To Console    ${Moto}

Laptop Links
    Click Element    id:apple
    Sleep    2
    Go Back
    Sleep    2
    
    Click Element    id:lenovo
    Sleep    2
    Go Back
    Sleep    2
    
    Click Element    id:dell
    Sleep    2
    Go Back
    Sleep    2


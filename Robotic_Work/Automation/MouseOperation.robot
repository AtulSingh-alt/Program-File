*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
MouseAction Test
        #Right Click/Open Context Menu
        Open Browser        https://swisnl.github.io/jQuery-contextMenu/demo.html       chrome
        Maximize Browser Window
        Open Context Menu    xpath:/html/body/div/section/div/div/div/p/span
        Sleep    3

        #Double Click action
        Go To    https://testautomationpractice.blogspot.com/
        Maximize Browser Window
        Double Click Element    xpath://*[@id="HTML10"]/div[1]/button
        Sleep    3
        
        #Drag & drop action
        Go To    https://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
        Maximize Browser Window
        Drag And Drop    id:box6    id:box106
        Sleep    3





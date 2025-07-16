*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
ScrollingTest
        Open Browser        https://www.countries-ofthe-world.com/flags-of-the-world.html       chrome
        Maximize Browser Window
        #scroll from up to down
        #Execute Javascript  window.scrollTo(0,3500)
        #Scroll until the element is visible
        #Scroll Element Into View    xpath://*[@id="ct-list"]/table[1]/tbody/tr[86]/td[1]/img
        #Scroll to down
        Sleep    4
        Execute Javascript      window.scrollTo(0,document.body.scrollHeight)
        Sleep    4
        #Scroll down to up
        Execute Javascript      window.scrollTo(0,-document.body.scrollHeight)
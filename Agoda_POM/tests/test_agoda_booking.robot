*** Settings ***
Library           SeleniumLibrary
Resource          ../resources/Common.robot
Resource          ../resources/Homepage.robot
Resource          ../resources/SearchResultsPage.robot
Resource          ../resources/HotelDetailsPage.robot
Resource          ../resources/BookingPage.robot
Resource          ../variables/variables.robot

Test Teardown     Close App

*** Test Cases ***
Agoda Hotel Booking Flow
    Open Agoda
    Dismiss App Popup
    Click All Sections
    Search For City    Delhi
    Click Search

    Wait For Hotels
    Scroll And Count Hotels
    Extract Hotel Names And Prices
    Select Cheapest Hotel

    Handle Image Popup
    Go To Cheapest Room
    Click Book Now

    Fill Guest Details
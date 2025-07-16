*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://maps.googleapis.com
${req_uri}      /maps/api/place/nearbysearch/json?

*** Test Cases ***
GoogleMapPlacesAPITC
        ${params}   Create Dictionary   location=-33.8670522,151.1957362    radius=500  types=food  name=harbour    key=YOUR_API_KEY
        ${response}=    GET     ${base_url}${req_uri}   params=${params}

        Log To Console    ${response.status_code}
        Log To Console    ${response.content}
# Google-Calender-with-Django
Implementing the Google calender with django using Oauth-2

Problem: In this assignment you have to implement google calendarintegration using django rest api. You need to use the OAuth2 mechanism toget users calendar access.

For run this project on a local machine: 

```sh
pip install - r requriments.txt
```

- Endpoint:
```
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
```
This view should start step 1 of the OAuth. Which will prompt user for his/her credentials

```
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
```
This view will do two things
1. Handle redirect request sent by google with code for token. You
need to implement mechanism to get access_token from given
code
2. Once got the access_token get list of events in users calendar


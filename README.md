467-final-project
=================
Usage:
Run a server, then open.

The data source is our own browsing histories and calendars, but we have
provided tools for you to visualize your own if you would like.

How to get the data from database:

```
$ sqlite3 ~/Library/Application\ Support/Google/Chrome/Default/History
sqlite> SELECT urls.url, urls.title, datetime((visits.visit_time/1000000)-11644473600, 'unixepoch', 'localtime') FROM urls, visits WHERE urls.id = visits.url;
```

You can retrieve your calendar data through the utility in
calendar-util.

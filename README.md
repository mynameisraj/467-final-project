467-final-project
=================

How to get the data from database:

```
$ sqlite3 ~/Library/Application\ Support/Google/Chrome/Default/History
sqlite> SELECT urls.url, urls.title, datetime((visits.visit_time/1000000)-11644473600, 'unixepoch', 'localtime') FROM urls, visits WHERE urls.id = visits.url;
```

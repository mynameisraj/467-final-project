467-final-project
=================

How to get the data from database:

```
$ cd ~/Library/Application\ Support/Google/Chrome/Default`
$ sqlite3 History
sqlite> SELECT urls.url, urls.title, datetime((visits.visit_time/1000000)-11644473600, 'unixepoch', 'localtime') FROM urls, visits WHERE urls.id = visits.url;
```

chrome.browserAction.onClicked.addListener(function(tab) {
    if(tab.url.match("google.com") && tab.url.match("calendar")) {
      console.log("Starting test on " + tab.url + ".");
      chrome.tabs.executeScript(
        null,
        { file: "content_script.js" }
      );
    }
});

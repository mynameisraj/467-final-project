chrome.browserAction.onClicked.addListener(function(tab) {
    console.log("Starting test on " + tab.url + ".");
    chrome.tabs.executeScript({
        code: 'document.body.style.backgroundColor="blue"'
    });
});

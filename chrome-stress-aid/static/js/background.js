chrome.runtime.onMessage.addListener(function (msg, sender) {
  // First, validate the message's structure
  if ((msg.from === 'content')) {
    alert(msg.subject);
    var http = new XMLHttpRequest();
    var url = "http://104.198.249.148:5000/updatetemp";
    var params = JSON.stringify({
      'account_id': 456,
      'message': msg.subject
    });
    http.open("POST", url, true);

    //Send the proper header information along with the request
    http.setRequestHeader("Content-type", "application/json");

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }
    http.send(params);
  }
});
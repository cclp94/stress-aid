chrome.runtime.onMessage.addListener(function (msg, sender) {
  // First, validate the message's structure
  if ((msg.from === 'content')) {
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
            chrome.runtime.sendMessage({
              from:    'stressData',
              subject: http.responseText
          });
        }
    }
    http.send(params);
  }
});


function getRandomToken() {
    // E.g. 8 * 32 = 256 bits token
    var randomPool = new Uint8Array(32);
    crypto.getRandomValues(randomPool);
    var hex = '';
    for (var i = 0; i < randomPool.length; ++i) {
        hex += randomPool[i].toString(16);
    }
    // E.g. db18458e2782b2b77e36769c569e263a53885a9944dd0a861e5064eac16f1a
    return hex;
}

chrome.storage.sync.get('userid', function(items) {
    var userid = items.userid;
    console.log(userid);
    if (!userid) {
        userid = getRandomToken();
         console.log(userid);
        chrome.storage.sync.set({userid: userid}, function() {
            useToken(userid);
        });
    }
    function useToken(userid) {
        // TODO: Use user id for authentication or whatever you want.
        // Create user on backend
        var http = new XMLHttpRequest();
        var url = "http://104.198.249.148:5000/insertuser";
        var params = JSON.stringify({
          'account_id': userid
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
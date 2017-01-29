//https://www.youtube.com/watch?v=fRh_vgS2dFE&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj
//youtube playlist


function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

httpGetAsync("https://www.googleapis.com/youtube/v3/playlists", function(data){
     return JSON.stringify(data);
});

chrome.runtime.onMessage.addListener(function (msg, sender) {
  // First, validate the message's structure
  if ((msg.from === 'stressData')) {
      var mood;
      if(msg.subject < -0.2 && msg.subject > -0.5)
        document.getElementById("mood").innerHTML = 'Moody';
      else if(msg.subject <= -0.5)
        document.getElementById("mood").innerHTML ='stressed';
      else if(msg.subject >= -0.2 && msg.subject < 0.3)
        document.getElementById("mood").innerHTML ='Ok';
      else
        document.getElementById("mood").innerHTML ='Happy';
  }
});

//
// var playListURL = 'http://gdata.youtube.com/feeds/api/playlists/B2A4E1367126848D?v=2&alt=json&callback=?';
// var videoURL= 'http://www.youtube.com/watch?v=';
// $.getJSON(playListURL, function(data) {
//     var list_data="";
//     $.each(data.feed.entry, function(i, item) {
//         var feedTitle = item.title.$t;
//         var feedURL = item.link[1].href;
//         var fragments = feedURL.split("/");
//         var videoID = fragments[fragments.length - 2];
//         var url = videoURL + videoID;
//         var thumb = "http://img.youtube.com/vi/"+ videoID +"/default.jpg";
//         if (videoID !='videos') {
// list_data += '<li><a href="'+ url +'" title="'+ feedTitle +'"><img alt="'+ feedTitle+'" src="'+ thumb +'"</a></li>';
// }
//     });
//     $(list_data).appendTo(".cont");
// });
//https://www.youtube.com/watch?v=fRh_vgS2dFE&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj
//youtube playlist
// function changeColor(){
//           document.getElementById("mood").innerHTML = 'Feeling Okay &#128528;',
//
//
// }

// changeColor();
var background = chrome.extension.getBackgroundPage();


$("#show-vid").click(function(){
    $("#vid").slideToggle();
});

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

setInterval(function(){
   if(background.moodData){
    var mood = JSON.parse(background.moodData)["total_value"];
      if(mood < '-0.2' && mood > '-0.5')
        document.getElementById("mood").innerHTML = 'Moody';
      else if(mood <= '-0.5')
        document.getElementById("mood").innerHTML ='stressed';
      else if(mood >= '-0.2' && mood < '0.3')
        document.getElementById("mood").innerHTML ='Ok';
      else
        document.getElementById("mood").innerHTML ='Happy';
  }
  }, 1000);

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
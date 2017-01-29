window.keyBuffer = [];

window.onkeyup = function(e) {
   var key = e.keyCode;
   if(key == 13){
       if(window.keyBuffer.length > 0){
           var text = window.keyBuffer.join('');
       chrome.runtime.sendMessage({
            from:    'content',
            subject: text
        });
        window.keyBuffer = [];
       }
       
   }else if(key == 8){
       if(window.keyBuffer.length > 0) window.keyBuffer.pop();
   }else{
       window.keyBuffer.push(String.fromCharCode(e.which).toLocaleLowerCase());
   }
}
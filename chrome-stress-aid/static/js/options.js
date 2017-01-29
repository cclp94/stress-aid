// Saves options to chrome.storage
function save_options() {
  var moodPredictOption = document.getElementById('moodPredict').checked;
  var recommendedContentOption = document.getElementById('recommendedContent').checked;
  var moodUpdateOption = document.getElementById('moodUpdate').value;
  chrome.storage.sync.set({
    moodPredict: moodPredictOption,
    recommendedContent: recommendedContentOption, 
    moodUpdate: moodUpdateOption
  }, function() {
    // Update status to let user know options were saved.
    var status = document.getElementById('status');
    status.textContent = 'Options saved.';
    setTimeout(function() {
      status.textContent = '';
    }, 750);
  });
}

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
function restore_options() {
  chrome.storage.sync.get({
    moodPredict: true,
    recommendedContent: true,
    moodUpdate: 'weekly'
  }, function(items) {
    document.getElementById('moodPredict').checked = items.moodPredict;
    document.getElementById('recommendedContent').checked = items.recommendedContent;
    document.getElementById('moodUpdate').value = items.moodUpdate;
  });
}
document.addEventListener('DOMContentLoaded', restore_options);
document.getElementById('save').addEventListener('click',
    save_options);
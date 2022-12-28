console.log("Chrome extention ready to go");
function getData(url){
window.setTimeout( function() {
    window.location.reload();
}, 10000);
  console.log("Started GetDATA");
  url = document.URL
  match_info = document.querySelector("#page-wrapper > div.cb-col.cb-col-100.cb-bg-white > div.cb-nav-main.cb-col-100.cb-col.cb-bg-white > div.cb-nav-subhdr.cb-font-12 > a:nth-child(2) > span")
  var match_name = match_info.textContent.split(' ')[1]
  console.log(match_name)
  if (match_name == 'Premier')
  {
    console.log("we are in")
  //"https://www.cricbuzz.com/api/html/cricket-scorecard/43966";
    fetch(url).then(response=> response.text())
    .then(data=> postData(data));
  }
}

function postData(data){
  url = "http://127.0.0.1:5000/"
  // params = {
  //   method:'post',
  //   headers:{
  //             'content-type':'application/json'
  //           },
  //   body:JSON.stringify(data)
  // }

  var xhr = new XMLHttpRequest();
    xhr.open("POST", url , true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(data);
    console.log("data sent")


xhr.onload = function() {
  console.log("HELLO")
  console.log(this.responseText);
  var received_data = JSON.parse(this.responseText);
  console.log(received_data);
  chrome.runtime.sendMessage(received_data);
}
  // fetch(url, params).then(response=> response.json()).then(data=> console.log(data));
  //   console.log('SUCCESS!');
    console.log(data);
}
getData();






// def model(inps):
//     df = pd.DataFrame(inps,index=[0])
//     df =pd.get_dummies(df)
//     df = df.reindex(columns = column_sequence, fill_value=0)
//     display(df)
// model({"team2":"csk","score":23})

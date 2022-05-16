
// let bgpage = chrome.extension.getBackgroundPage();
// // console.log(bgpage.team1_pred);
// let pred1 = bgpage.team1_pred;
// let pred2 = bgpage.team2_pred;
// let team1 = bgpage.team1;
// let team2 = bgpage.team2;
// console.log(pred1)
// console.log(pred2)
// console.log(team1)
// console.log(team2)

console.log("this is background script!")
chrome.runtime.onMessage.addListener(receiver);
function receiver(request, sender,sendResponse)
{
  console.log("HOLA")
  console.log(request.Win)
var i
img_sources = {"Chennai Super Kings": "https://www.pngall.com/wp-content/uploads/2017/04/Chennai-Super-Kings-Logo-PNG.png",
"Kolkata Knight Riders":"https://www.pngall.com/wp-content/uploads/2017/04/Kolkata-Knight-Riders-Logo-PNG.png",
"Royal Challengers Bangalore":"https://www.vhv.rs/dpng/d/417-4175849_royal-challengers-bangalore-new-logo-hd-png-download.png",
"Rajasthan Royals":"https://www.pngall.com/wp-content/uploads/2017/04/Rajasthan-Royals-Logo-PNG.png",
"Gujarat Titans":"https://blogger.googleusercontent.com/img/a/AVvXsEjafImVAQfB7gxNPruavRGxqK6cJ0sSklxgqYXpW1geK9Su2Z9w7FUP-EV4B82WisoMn75NUNKlD6COpHdWlHwa5MjNDw6y8Htbr51uUT-VFilUkFx7QGlGE7m015fI5O3M3P5sGE0iqbYQQ39WFNC_pwVi-OZkw9J6laUWIsk68u5E0zSvYUMtnXof=w1200-h630-p-k-no-nu",
"Lucknow Super Giants":"https://upload.wikimedia.org/wikipedia/commons/3/30/Lucknow_supergiants_logo.png",
"Delhi Capitals":"https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/Delhi_Capitals_Logo.svg/1200px-Delhi_Capitals_Logo.svg.png",
"Sunrisers Hyderabad":"https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Sunrisers_Hyderabad.svg/1200px-Sunrisers_Hyderabad.svg.png",
"Mumbai Indians":"https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Mumbai_Indians_Logo.svg/1280px-Mumbai_Indians_Logo.svg.png",
"Punjab Kings":"https://logoeazy.com/wp-content/uploads/2021/05/punjab-kings-new-logo.png"}

document.getElementById("teamlogo1").src = img_sources[request.Team1];
document.getElementById('team1').innerHTML = request.Team1;
document.getElementById("teamlogo2").src = img_sources[request.Team2];
document.getElementById('team2').innerHTML = request.Team2;
document.getElementById('data1').setAttribute("value", request.team1_probability, "max","1");
document.getElementById('data2').setAttribute("value", request.team2_probability, "max","1");
var progress1 = document.getElementById('data1').position;
// document.getElementById('%1').innerHTML = Math.floor(progress1*100) + "%"
document.getElementById('%1').innerHTML = (progress1*100).toFixed(2) + "%"

var progress2 = document.getElementById('data2').position;
// document.getElementById('%2').innerHTML = Math.floor(progress2*100) + "%"
document.getElementById('%2').innerHTML = (progress2*100).toFixed(2) + "%"
// const g = document.createElement("progress");
// g.setAttribute("value", request.team1_probability);
// g.setAttribute("max", "1");
// g.setAttribute("position", true);
// document.getElementById("data1").append(g);
// document.getElementById("%1").append(Math.floor(g.position*100) + '%');
// const f = document.createElement("progress");
// f.setAttribute("value", request.team2_probability);
// f.setAttribute("max", "1");
// f.setAttribute("position", true);
// document.getElementById("data2").append(f);
// document.getElementById("%2").append(Math.floor(f.position*100) + '%');
//
//
}

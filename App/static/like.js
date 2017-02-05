// 
// if (document.addEventListener ){
//     document.addEventListener("click", function(event){
//         var targetElement = event.target || event.srcElement;
//         targetElement.setAttribute("id", "liked")
//     });

function like(album_id, user_id, page)
{
  div = document.getElementById("main");
  var alert = document.createElement("div");
  alert.setAttribute("class","alert alert-success");
  alert.setAttribute("role","alert");
  alert.setAttribute("id","alert");
  alert.textContent = "Album liké !";
  div.insertBefore(alert, document.getElementsByClassName('grid')[0]);

  var http = new XMLHttpRequest();
  if (page == "home.html")
  {
    var url = "/";
  }
  else
  {
    var url = page;

  }
  var params = "albumId="+album_id+"&userId="+user_id+"";
  http.open("POST", url, true);

  //Send the proper header information along with the request
  http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  // http.onreadystatechange = function() {//Call a function when the state changes.
  //     if(http.readyState == 4 && http.status == 200) {
  //         alert(http.responseText);
  //     }
  // }
  http.send(params);

  setTimeout(destroy,1000);

}

function destroy()
{
  elem = document.getElementById("main");
  elem.removeChild(document.getElementById('alert'));
}

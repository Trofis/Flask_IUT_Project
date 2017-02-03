function like(album_id, user_id, page)
{
  div = document.getElementById("main");
  var alert = document.createElement("div");
  alert.setAttribute("class","alert alert-success");
  alert.setAttribute("role","alert");
  alert.textContent = "Texte ajouté !";
  div.insertBefore(alert, document.getElementById("zic")));

  var http = new XMLHttpRequest();
  var url = page;
  var params = "albumId=+"album_id+"&userId="+user_id+"";
  http.open("POST", url, true);

  //Send the proper header information along with the request
  http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  // http.onreadystatechange = function() {//Call a function when the state changes.
  //     if(http.readyState == 4 && http.status == 200) {
  //         alert(http.responseText);
  //     }
  // }
  http.send(params);
}

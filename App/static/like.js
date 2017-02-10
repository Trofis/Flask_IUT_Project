
function like(album_id, user_id, page)
{

  div = document.getElementById("main");
  var alert = document.createElement("div");
  alert.setAttribute("class","alert alert-success");
  alert.setAttribute("role","alert");
  alert.setAttribute("id","alert");
  alert.textContent = "Album liké !";

  if (page == "home")
  {
    div.insertBefore(alert, document.getElementById('grid'));

  }
  else if (page == "SearchAlbum")
    div.insertBefore(alert, document.getElementById('SearchContain'));
  var http = new XMLHttpRequest();
  if (page == "home")
  {
    var url = "/";
  }
  else
  {
    var url = page;

  }
  var params = "albumId="+album_id+"&userId="+user_id+"";
  http.open("POST", url, true);

  http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  http.send(params);

  setTimeout(destroy,1000);

}

function likeAlt(album_id, page)
{
  div = document.getElementById("main");
  var al = document.createElement("div");
  al.setAttribute("class","alert alert-danger");
  al.setAttribute("role","alert");
  al.setAttribute("id","alert");
  al.textContent = "Veuillez vous connecter !";
  if (page == "home.html")
    div.insertBefore(al, document.getElementById('grid'));
  else if (page == "SearchAlbum")
    div.insertBefore(al, document.getElementById('SearchContain'));
  setTimeout(destroy,1000);
}
function destroy()
{
  elem = document.getElementById("main");
  elem.removeChild(document.getElementById('alert'));
}

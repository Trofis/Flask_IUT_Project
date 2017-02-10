function searchForm()
{
  form = document.getElementById('SearchForm');
  text = form.children[0];

  res = "album/"+text.value;
  form.setAttribute("action", res);
}

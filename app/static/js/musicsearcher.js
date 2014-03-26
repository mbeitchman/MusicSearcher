function validateSearchForm()
{
	var searchrequest = document.getElementById('search').value;
	if (!searchrequest || 0 === searchrequest.length)
    {
	  return false;
	}

	return true;
}
function updateHpiValue(val) {
  document.getElementById('hpiValue').innerText = val;
}

document.getElementById('searchInput').addEventListener('input', function () {
  const query = this.value;
  if (query.length >= 3) {
    fetch(`/search-person?q=${encodeURIComponent(query)}`)
      .then((response) => response.json())
      .then((data) => {
        const resultsContainer = document.getElementById(
          'searchResultsContainer'
        );
        // Clear previous results
        resultsContainer.innerHTML = '';

        // Check if the response contains a 'message' key
        if (data.message) {
          resultsContainer.textContent = data.message; // Display "No people found"
        } else {
          // Check again if the input length is >= 3 before updating the DOM
          if (document.getElementById('searchInput').value.length >= 3) {
            data.results.forEach((person) => {
              const personElement = document.createElement('div');
              personElement.textContent = `${person.name} (${person.birthyear} - ${person.deathyear})`;
              personElement.addEventListener(
                'click',
                () => (window.location.href = `/select-person/${person.id}`)
              );
              resultsContainer.appendChild(personElement);
            });
          }
        }
      });
  } else {
    document.getElementById('searchResultsContainer').innerHTML = '';
  }
});

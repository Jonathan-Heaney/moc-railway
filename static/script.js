const hpiValue = document.getElementById('hpiValue');
const searchInput = document.getElementById('searchInput');
const searchResultsContainer = document.getElementById(
  'searchResultsContainer'
);

function updateHpiValue(val) {
  hpiValue.innerText = val;
}

searchInput.addEventListener('input', function () {
  const query = this.value;
  if (query.length >= 3) {
    fetch(`/search-person?q=${encodeURIComponent(query)}`)
      .then((response) => response.json())
      .then((data) => {
        // Clear previous results
        searchResultsContainer.innerHTML = '';

        // Check if the response contains a 'message' key
        if (data.message) {
          searchResultsContainer.textContent = data.message; // Display "No people found"
        } else {
          // Check again if the input length is >= 3 before updating the DOM
          if (searchInput.value.length >= 3) {
            data.results.forEach((person) => {
              const personElement = document.createElement('div');
              personElement.textContent = `${person.name} (${person.birthyear} - ${person.deathyear})`;
              personElement.addEventListener(
                'click',
                () => (window.location.href = `/select-person/${person.id}`)
              );
              searchResultsContainer.appendChild(personElement);
            });
          }
        }
      });
  } else {
    searchResultsContainer.innerHTML = '';
  }
});

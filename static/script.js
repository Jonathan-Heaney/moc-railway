const hpiValue = document.getElementById('hpiValue');
const searchInput = document.getElementById('searchInput');
const searchResultsContainer = document.getElementById(
  'searchResultsContainer'
);

function updateHpiValue(val) {
  hpiValue.innerText = val;
}

const formatYears = (birthyear, deathyear) => {
  // If both years are AD, omit AD suffix
  if (birthyear > 0) {
    return `${birthyear} - ${deathyear}`;
  }

  const formatYear = (year) => Math.abs(year) + (year < 0 ? ' BC' : ' AD');

  let formattedBirthyear = formatYear(birthyear);
  let formattedDeathyear = formatYear(deathyear);

  return `${formattedBirthyear} - ${formattedDeathyear}`;
};

searchInput.addEventListener('input', searchPeople);

function searchPeople() {
  const query = this.value;
  if (query.length >= 3) {
    fetch(`/search-person?q=${encodeURIComponent(query)}`)
      .then((response) => response.json())
      .then((data) => {
        // Clear previous results
        searchResultsContainer.innerHTML = '';

        // Check if the response contains a 'message' key
        if (data.message) {
          const noResults = document.createElement('div');
          noResults.textContent = data.message;
          noResults.className = 'no-results';
          searchResultsContainer.appendChild(noResults);
        } else {
          // Check again if the input length is >= 3 before updating the DOM
          if (searchInput.value.length >= 3) {
            data.results.forEach((person) => {
              const personElement = document.createElement('li');
              personElement.textContent = `${person.name} (${formatYears(
                person.birthyear,
                person.deathyear
              )})`;
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
}

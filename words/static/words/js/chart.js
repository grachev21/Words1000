 const ctx1 = document.getElementById('myChart');

  new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: [1,2,3,4,5,6,7,],
      datasets: [{
        label: 'График выученых слов',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
        backgroundColor: '#69bfbb'
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });


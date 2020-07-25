window.addEventListener('load', (event) => {
    var barChart = document.getElementById("barChart").getContext('2d');
    var doughnutChart = document.getElementById('doughnutChart').getContext('2d');
    var myChart = document.getElementById('myChart').getContext('2d');
    var myChart1 = document.getElementById('myChart1').getContext('2d');
    var myChart2 = document.getElementById('myChart2').getContext('2d');
    var myBarChart = new Chart(barChart, {
        type: 'bar',
        data: {
            labels: ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
            datasets : [{
                label: "Number of responses",
                backgroundColor: 'rgb(23, 125, 255)',
                borderColor: 'rgb(23, 125, 255)',
                data: [3, 2, 9, 5, 4, 6, 4, 6, 7, 8, 7, 4],
            }],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
        }
    });

    var myDoughnutChart = new Chart(doughnutChart, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [10, 20, 30],
                backgroundColor: ['#f3545d','#fdaf4b','#1d7af3']
            }],

            labels: [
            'Transportation',
            'Facility',
            'Service'
            ]
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            legend : {
                position: 'bottom'
            },
            layout: {
                padding: {
                    left: 20,
                    right: 20,
                    top: 20,
                    bottom: 20
                }
            }
        }
    });

    var myBarChart = new Chart(myChart, {
        type: 'bar',
        data: {
            labels: ["C1", "C5", "C6", "C7", "C8"],
            datasets : [{
                label: "Number of responses",
                backgroundColor: 'rgb(23, 125, 255)',
                borderColor: 'rgb(23, 125, 255)',
                data: [3, 2, 2, 5, 4],
            }],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
        }
    });

    var myBarChart = new Chart(myChart1, {
        type: 'bar',
        data: {
            labels: ["C1", "C2", "C3", "C7", "C8"],
            datasets : [{
                label: "Number of responses",
                backgroundColor: 'rgb(23, 125, 255)',
                borderColor: 'rgb(23, 125, 255)',
                data: [3, 2, 9, 5, 4],
            }],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
        }
    });

    var myBarChart = new Chart(myChart2, {
        type: 'bar',
        data: {
            labels: ["C1", "C2", "C3", "C4", "C5", "C6"],
            datasets : [{
                label: "Number of responses",
                backgroundColor: 'rgb(23, 125, 255)',
                borderColor: 'rgb(23, 125, 255)',
                data: [3, 2, 9, 5, 4, 6],
            }],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
        }
    });

    
  });	

 
    

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';




var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Hot", "Warm", "Cold", "Freeze"],
    datasets: [{
      data: [2, 1, 1, 1],
      backgroundColor: ["#e74c3c", 'orange', 'lightblue', '#0984e3'],
      hoverBackgroundColor: ["#e74c3c", 'orange', 'lightblue','#0984e3'],
      hoverBorderColor: ["#e74c3c", 'orange', 'lightblue', '#0984e3'],
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

Highcharts.chart("containerHincha", {
    chart: {
      type: "bar",
    },
    title: {
      text: "Total de hinchas por deporte",
    },
    xAxis: {
      categories: [], // Aquí almacenaremos los nombres de deportes
      title: {
        text: "Deporte",
      },
    },
    yAxis: {
      title: {
        text: "Cantidad de hinchas",
      },
    },
    legend: {
      align: "left",
      verticalAlign: "top",
      borderWidth: 0,
    },
  
    series: [
      {
        name: "Hinchas",
        data: [], // Aquí almacenaremos la cantidad de hinchas por deporte
        lineWidth: 1,
        marker: {
          enabled: true,
          radius: 4,
        },
        color: "#5FC26B", 
      },
    ],
  });
  
  fetch("http://localhost:5000/get-hincha-stats-data")
    .then((response) => response.json())
    .then((data) => {
      const categories = data.map((item) => item.tipo);
      const counts = data.map((item) => item.hinchas);
  
      const chartHincha = Highcharts.charts.find(
        (chart) => chart && chart.renderTo.id === "containerHincha"
      );
  
      chartHincha.update({
        xAxis: {
          categories,
        },
        series: [
          {
            data: counts,
          },
        ],
      });
    })
    .catch((error) => console.error("Error:", error));
  

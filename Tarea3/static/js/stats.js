Highcharts.chart("container", {
  chart: {
    type: "bar",
  },
  title: {
    text: "Total de artesanos por tipo de artesanía",
  },
  xAxis: {
    categories: [], // Aquí almacenaremos los tipos de artesanía
    title: {
      text: "Tipo de artesanía",
    },
  },
  yAxis: {
    title: {
      text: "Cantidad de artesanos",
    },
  },
  legend: {
    align: "left",
    verticalAlign: "top",
    borderWidth: 0,
  },

  series: [
    {
      name: "Artesanos",
      data: [], // Aquí almacenaremos la cantidad de artesanos
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color: "#FC2865",
    },
  ],
});

fetch("http://localhost:5000/get-stats-data")
  .then((response) => response.json())
  .then((data) => {
    // Extraemos los tipos de artesanía y la cantidad de artesanos de los datos
    const categories = data.map((item) => item.tipo);
    const counts = data.map((item) => item.artesanos);

    // Obtenemos el gráfico por ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Actualizamos el gráfico con los nuevos datos
    chart.update({
      xAxis: {
        categories, // Actualizamos los tipos de artesanía
      },
      series: [
        {
          data: counts, // Actualizamos la cantidad de artesanos
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));

document.addEventListener('DOMContentLoaded', function() {
    // Obtén los datos del contexto de Django
    var barData = JSON.parse(document.getElementById('bar-data').textContent);
    var lineData = JSON.parse(document.getElementById('line-data').textContent);
    var pieData = JSON.parse(document.getElementById('pie-data').textContent);
  
    // Configuración y renderizado del gráfico de barras
    var barChart = echarts.init(document.getElementById('bar-chart'));
    var barOption = {
      title: {
        text: 'Week Task Completed'
      },
      xAxis: {
        type: 'category',
        data: barData.labels
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        data: barData.completed,
        type: 'bar'
      }]
    };
    barChart.setOption(barOption);
  
    // Configuración y renderizado del gráfico de líneas
    var lineChart = echarts.init(document.getElementById('line-chart'));
    var lineOption = {
      title: {
        text: 'Month Task Completed'
      },
      xAxis: {
        type: 'category',
        data: lineData.labels
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        data: lineData.completed,
        type: 'line'
      }]
    };
    lineChart.setOption(lineOption);
  
    // Configuración y renderizado del gráfico de pastel
    var pieChart = echarts.init(document.getElementById('pie-chart'));
    var pieOption = {
      tooltip: {
        trigger: 'item'
      },
      legend: {
        orient: 'vertical',
        left: 'left'
      },
      series: [{
        name: 'Tareas',
        type: 'pie',
        radius: '50%',
        data: pieData,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }]
    };
    pieChart.setOption(pieOption);
  });
  
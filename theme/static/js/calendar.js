document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      events: taskEvents,  // Aquí se asigna la variable taskEvents
      eventClick: function(info) {
          window.location.href = info.event.url;  // Redirige al hacer clic en el evento
      }
  });

  calendar.render();
});

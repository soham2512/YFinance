const startdatepicker = document.getElementById('startdate');
startdatepicker.addEventListener('input', function(e){
  var day = new Date(this.value).getUTCDay();
  if([6,0].includes(day)){
    e.preventDefault();
    this.value = '';
    alert('The lumber data doesnt have weekends stock values,\nPlease select weekdays date from the calendar');
  }
});

const enddatepicker = document.getElementById('enddate');
enddatepicker.addEventListener('input', function(e){
  var day = new Date(this.value).getUTCDay();
  if([6,0].includes(day)){
    e.preventDefault();
    this.value = '';
    alert('The lumber data doesnt have weekends stock values,\nPlease select weekdays date from the calendar in-order to display the chart.');
  }
});
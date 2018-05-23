$(document).ready(function() {
    $( ".datepicker" ).datepicker({
      changeMonth: true,
      changeYear: true,
      autoSize: true
    });
});

$(document).ready(function() {
    $( ".future-datepicker" ).datepicker({
        minDate : 0,
        changeMonth: true,
        changeYear: true,
        autoSize: true
    });
});
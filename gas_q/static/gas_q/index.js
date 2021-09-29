document.addEventListener('DOMContentLoaded', () => {

  removeTimeSlot()
});


const removeTimeSlot = () => {
  const hours = document.getElementById('id_timeslot');
  const days = document.getElementById('id_day');
  const labels = document.getElementsByTagName('label');

  for (var i = 0; i < labels.length; i++) {
    if (labels[i].htmlFor === 'id_timeslot')
      var label = labels[i]
  }

  hours.style.display = 'none';
  label.style.display = 'none';

  days.addEventListener('change', () => {

    if (days.value === '') {
      label.style.display = 'none';
      hours.style.display = 'none';
    } else {
      label.style.display = 'block';
      hours.style.display = 'block';
    }
  });

  const hour_options = document.querySelectorAll('#id_timeslot');
  const day_options = document.querySelectorAll('#id_day');

  fetch(`/json`)
    .then(res => res.json())
    .then(data => {
      // console.log(data)
      const timeSlot = data.map(time => ({
        'timeslot': time.timeslot,
        'day': time.day,
      }))
      // console.log(timeSlot)
      // console.log(day)
      var counts = {};
      timeSlot.forEach((x) => {
        let string = x.timeslot.toString() + x.day.toString();
        counts[string] = (counts[string] || 0) + 1;
      });
      // console.log(counts)

      let hide = Object.keys(counts).filter(key => counts[key] >= 6)
      // console.log(hide);

      day_options[0].addEventListener('change', () => {

        let daySelected = day_options[0].options[day_options[0].selectedIndex].value;


        hour_options.forEach(element => {
          let options = Array.from(element)
          options.forEach(opt => {
            opt.hidden = false;
            hide.forEach(i => {
              if (opt.value === (i.charAt(0) + i.charAt(1)) && daySelected === i.charAt(2)) {
                opt.hidden = true;
                opt.selected = false;
              }
            })
          })
        });
      });

    })

}

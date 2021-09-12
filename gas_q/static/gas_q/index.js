document.addEventListener('DOMContentLoaded', () => {

  removeTimeSlot()
});


const removeTimeSlot = () => {

  const option = document.querySelectorAll('option');

  fetch(`/json`)
  .then(res => res.json())
  .then(data => {
    console.log(data)
    const timeSlot = data.map(time => time.timeslot)
    console.log(timeSlot)
    let map = timeSlot.reduce((prev, cur) => {
      prev[cur] = (prev[cur] || 0) + 1;
      return prev
    }, {})
    console.log(map);
    // let hide = map[0]
    let hide = Object.keys(map).filter(key => map[key] >= 3) 
    console.log('hide is...' + hide);
    option.forEach(element => {
      hide.forEach(i => {
        if (element.value === i) {
          element.hidden = true;
          element.selected = false;
        }
      })
      
    });
  })

}

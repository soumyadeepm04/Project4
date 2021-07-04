document.addEventListener('DOMContentLoaded', () => {
    const checkbox = document.querySelector('#follow');
    checkbox.addEventListener('change', () => {
        if (checkbox.dataset.exists == 'True'){
            checkbox.checked == true
        }
        if (checkbox.checked){
            fetch(`http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/follow/${checkbox.dataset.id}`, {
                method: 'PUT'
            })
            .then(response => {
                console.log(response);
        })
        }
    })
})
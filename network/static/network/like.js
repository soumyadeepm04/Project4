document.addEventListener('DOMContentLoaded', () => {
    window.onload = check();
    document.querySelectorAll('.like').forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            if (checkbox.checked){
                fetch('http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/like', {
                    method: 'POST',
                    body:JSON.stringify({
                        post_id: checkbox.dataset.id
                    })
                })
            }
            else{
                fetch('http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/unlike', {
                    method: 'POST',
                    body:JSON.stringify({
                        post_id: checkbox.dataset.id
                    })
                })
            }
        })
    })
})

function check(){
    document.querySelectorAll('.like').forEach(element => {
        if (element.dataset.liked === 'yes'){
            element.checked = true;
        }
    })
}
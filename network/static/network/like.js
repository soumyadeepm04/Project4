document.addEventListener('DOMContentLoaded', () => {
    window.onload = check();
    document.querySelectorAll('.like').forEach(checkbox => {
        let likes = checkbox.dataset.likes;
        checkbox.addEventListener('change', () => {
            if (checkbox.checked){
                fetch('http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/like', {
                    method: 'POST',
                    body:JSON.stringify({
                        post_id: checkbox.dataset.id
                    })
                })
                likes++;
                document.getElementById(`${checkbox.dataset.id}`).innerHTML = `Likes: ${likes}`;
            }
            else{
                fetch('http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/unlike', {
                    method: 'POST',
                    body:JSON.stringify({
                        post_id: checkbox.dataset.id
                    })
                })
                likes--;
                document.getElementById(`${checkbox.dataset.id}`).innerHTML = `Likes: ${likes}`;
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
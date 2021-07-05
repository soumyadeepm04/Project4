document.addEventListener('DOMContentLoaded', () => {
    window.onload = OnPageLoad();
    document.querySelector('#submit').onclick = () => {
        fetch(`http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/edit_post/${document.querySelector('#change_content').dataset.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    content: document.querySelector('#change_content').value
                })
            })
        document.querySelector('#change_content').value = '';
    }
})

function OnPageLoad(){
    document.querySelector('#change_content').value = document.querySelector('#change_content').dataset.content
}
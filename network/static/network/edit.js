document.addEventListener('DOMContentLoaded', () => {
    var x = 0;
    var y = 0;
    document.addEventListener('click', event => {
        document.querySelectorAll('.edit').forEach(element => {
            if (event.target === element){
                y = element;
                x = document.getElementById(`${element.dataset.timestamp}`);
                x.style.display = 'block';
                x.children[0].value = element.dataset.content;
            }
        })
    })
    document.addEventListener('click', event => {
        if (event.target === x.children[1]){
            document.querySelectorAll('div').forEach(element => {
                if (element.getAttribute('data-required_to_edit') === `${y.dataset.content}`){
                    element.innerHTML = `${x.children[0].value}`
                    fetch(`http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/edit_post/${y.dataset.id}`, {
                        method: 'PUT',
                        body: JSON.stringify({
                            content: x.children[0].value
                        })
                    })
                }
            })
            x.style.display = 'none';
        }
    })
})
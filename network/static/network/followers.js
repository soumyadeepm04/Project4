document.addEventListener('DOMContentLoaded', () => {
    window.onload = OnPageLoad();
    const checkbox = document.querySelector('#follow');
    let followers = checkbox.dataset.followers 
    checkbox.addEventListener('change', () => {
        if (checkbox.checked){
            fetch(`http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/follow/${checkbox.dataset.id}`, {
                method: 'PUT'
            })
            followers++;
            document.getElementById('followers').innerHTML = `Followers: ${followers} Following: ${checkbox.dataset.following}`
        }
        else{
            fetch(`http://ec2-13-127-62-102.ap-south-1.compute.amazonaws.com:8000/unfollow/${checkbox.dataset.id}`, {
                method: 'PUT'
            })
            followers--;
            document.getElementById('followers').innerHTML = `Followers: ${followers} Following: ${checkbox.dataset.following}`
        }
    })
})

function OnPageLoad(){
    if (document.querySelector('#follow').dataset.exists === 'True'){
        document.querySelector('#follow').checked = true;
    }
}
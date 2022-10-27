'use strict';

const followForm = document.querySelector('#follow-form');
const followBtn = document.querySelector('#followBtn');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

followForm.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log(e.target);
    axios({
        method: 'post',
        url: `/accounts/${e.target.dataset.userID}/follow/`,
        headers: { 'X-CSRFToken': csrftoken },
    })
        .then(response => {
            if (response.data.isFollow === true) {
                followBtn.innerText = '언팔로우'
            } else {
                followBtn.innerText = '팔로우'
            }
        })
});
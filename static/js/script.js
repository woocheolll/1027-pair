'use strict';

const form = document.querySelector('#follow-form')
form.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    axios({
        method: 'POST',
        url: `/accounts/${userId}/follow/`,
        headers: { 'X-CSRFToken': csrftoken, }
    })
        .then((response) => {
            const isFollow = response.data.isFollow
            const followBtn = document.querySelector('#follow-form > input[type=submit]')
            if (isFollow === true) {
                followBtn.value = 'unfollow'
            } else {
                followBtn.value = 'follow'
            }
            const followersCountTag = document.querySelector('#followers-count')
            const followingsCountTag = document.querySelector('#followings-count')
            const followersCount = response.data.followers_count
            const followingsCount = response.data.followings_count
            followersCountTag.innerText = followersCount
            followingsCountTag.innerText = followingsCount
        })
});

const commentForm = document.querySelector('#comment-form')
const csrftoken = document
    .querySelector('[name=csrfmiddlewaretoken]')
    .value
commentForm
    .addEventListener('submit', function (event) {
        event.preventDefault();
        axios({
            method: 'post',
            url: `/reviews/${event.target.dataset.reviewId}/comments/`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: new FormData(commentForm)
        }).then(response => {
            const comments = document.querySelector('#comments')
            const span = document.createElement('span')
            span.innerText = `${response.data.userName}님 | ${response.data.content}`
            const hr = document.createElement('hr')
            comments.append(span)
            comments.append(hr)
            commentForm.reset()
        })
    });



const selectForm = document.querySelector('#select-form');
const ctgSel = document.querySelector('#category-sel');

selectForm.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
        method: 'post',
        url: `/reviews/category/`,
        data: { 'value': event.value }
    })
        .then(response => {
            console.log('성공');

        })

})
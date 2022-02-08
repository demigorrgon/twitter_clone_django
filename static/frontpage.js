var handleTweetFormError = (message, display) => {
    var errorDivElement = document.getElementById("tweet-create-form-error");
    if (display === true) {
        errorDivElement.setAttribute("class", "d-block alert alert-danger");
        errorDivElement.innerText = message;
    } else {
        errorDivElement.setAttribute("class", "d-none alert alert-danger");
    }
}

var handleTweetCreateFormSubmit = (event) => {
    event.preventDefault();
    const formToSend = event.target
    const formToSendData = new FormData(formToSend)
    const url = formToSend.getAttribute('action')
    const method = formToSend.getAttribute('method')
    const responseType = "json"
    const xhr = new XMLHttpRequest()
    xhr.open(method, url);
    xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest')
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhr.onload = () => {
        if (xhr.status === 201) {
            handleTweetFormError("", false)
            const newTweetJson = JSON.parse(xhr.response);
            const newTweetElement = formattedTweetElement(newTweetJson);
            const previousHtml = tweetsContainerElem.innerHTML
            tweetsContainerElem.innerHTML = newTweetElement + previousHtml;
            formToSend.reset();

        } else if (xhr.status === 400) {
            const errorJson = JSON.parse(xhr.response);
            const contentError = errorJson.content;

            if (contentError) {
                let contentErrorMessage = contentError[0];
                if (contentErrorMessage) {
                    handleTweetFormError(contentErrorMessage, true)
                }
            }
        }
        else if (xhr.status === 403) {
            alert("Please login");
            window.location.href = "/account/login/";
        }
    }
    xhr.onerror = () => {
        alert('Yo chill')
    }
    xhr.send(formToSendData);
}

const tweetCreateForm = document.getElementById('tweet-create-form');
tweetCreateForm.addEventListener('submit', handleTweetCreateFormSubmit);

const tweetsContainerElem = document.getElementById("tweets")

var loadTweets = (tweetsElement, nextPage) => {
    // TODO: load tweets from next page
    const xhr = new XMLHttpRequest();
    const method = 'GET';

    if (nextPage !== undefined) {
        const url = nextPage;
        const responseType = 'json';
        xhr.responseType = responseType;
        xhr.open(method, url);
        xhr.onload = () => {
            const serverResponse = xhr.response;
            // console.log(serverResponse)
            var listedItems = serverResponse.results;
            // console.log(serverResponse, listedItems)
            var finalString = ""
            for (var i = 0; i < listedItems.length; i++) {
                var tweetObject = listedItems[i]
                var currentItem = formattedTweetElement(tweetObject)
                finalString += currentItem

            }
            finalString += nextPageButton()
            tweetsElement.innerHTML = finalString
        }
    }

    const url = `/api/tweets/feed/`;
    const responseType = 'json';
    xhr.responseType = responseType;
    xhr.open(method, url);
    xhr.onload = () => {
        const serverResponse = xhr.response;
        var listedItems = serverResponse.results;
        var finalString = ""
        for (var i = 0; i < listedItems.length; i++) {
            var tweetObject = listedItems[i]
            var currentItem = formattedTweetElement(tweetObject)
            finalString += currentItem

        }
        finalString += nextPageButton()
        tweetsElement.innerHTML = finalString
    }
    xhr.send();

}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var handleTweetAction = (tweet_id, currentAmount, action) => {
    const url = "/api/tweets/action/"
    const method = "POST"
    const data = JSON.stringify({
        id: tweet_id,
        action: action,
    });
    const xhr = new XMLHttpRequest();
    const csrftoken = getCookie('csrftoken');
    xhr.open(method, url);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest');
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.onload = () => {
        // console.log(xhr.status, xhr.response)
        loadTweets(tweetsContainerElem);
    }
    xhr.send(data);
    return
}

var handleFollowAction = (profileUser, action) => {
    const url = "/api/profiles/" + profileUser + "/follow/"
    const method = "POST"
    // console.log(profileUser)
    const data = JSON.stringify({
        username: profileUser,
        action: action,
    });
    const xhr = new XMLHttpRequest();
    const csrftoken = getCookie('csrftoken');
    xhr.open(method, url);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest');
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.onload = () => {
        console.log(xhr.status, xhr.response)
        window.location.href = '/';
    }

    xhr.send(data);
    return
}

var onClickEventFormatter = (tweetObject) => {
    username = tweetObject.username;
    return username
}

// var getNextPage = () => {
//     $.ajax({
//         url: '/api/tweets/feed/', success: function (result) {
//             console.log(result)
//         }
//     })
//     // loadTweets(tweetsContainerElem);
// }

var likeButton = (tweetObject) => {
    return "<button class='btn btn-primary' onclick='handleTweetAction(" + tweetObject.id + "," + tweetObject.likes + "," + '"like"' + ")'>" + tweetObject.likes + " Likes</button>";
}

var dislikeButton = (tweetObject) => {
    return "<button class='btn btn-outline-primary' onclick='handleTweetAction(" + tweetObject.id + "," + tweetObject.likes + "," + '"unlike"' + ")'>" + "dislike</button>";
}

var retweetButton = (tweetObject) => {
    return "<button class='btn btn-outline-success' onclick='handleTweetAction(" + tweetObject.id + "," + tweetObject.likes + "," + '"retweet"' + ")'>" + "retweet</button>";
}

var followButton = (tweetObject) => {
    return "<button class='btn btn-outline-primary' id='followBtn' onclick='handleFollowAction(\"" + tweetObject.username + "\"" + ", " + '"follow"' + ") '>" + "Follow </button>";
}
var nextPageButton = () => {
    return "<div class ='btn-group'>" + "<button class='btn btn-outline-primary' id='nextpageBtn'" + `onclick='loadTweets(tweetsContainerElem, getNextPage())'>Next Page</button></div>`
}

var formattedTweetElement = (tweetObject) => {
    var formattedTweet = "<div class='col-12 border mb-4 tweet' id='tweet-" + tweetObject.id + "'>" + "@" + tweetObject.username + "<br>" + "<div class='btn-group'>" + followButton(tweetObject) + "</div>" + "<br>tweeted: <br>" + tweetObject.content
        + "</p>" + "<div class='btn-group'>"
        + likeButton(tweetObject)
        + dislikeButton(tweetObject)
        + retweetButton(tweetObject)
        + "</div></div>";
    return formattedTweet
}

loadTweets(tweetsContainerElem);


// console.log(getNextPage())
var socket = io.connect('http://localhost:3000/');
    socket.on('connect', function(data){
    setStatus('connected');
    socket.emit('subscribe', {channel:'realtime'});
});

socket.on('reconnecting', function(data){
   setStatus('reconnecting');
});

socket.on('message', function (data) {
    data = $.parseJSON(data);
    console.log('received a message: ', data);
    createNewTweet(data);
});

function createNewTweet(data){
    var tweet_container = $('<div class="col-lg-3 col-md-4 col-sm-12 tweet_container"></div>');

    var tweet_media_container = $('<div class="tweet_media_container"></div>');
    var tweet_media = $('<img class="tweet_media img-responsive" src="' + data.media_url + '">');

    var tweet_footer = $('<div class="tweet_footer"></div>');

    var tweet_avatar = $('<div class="tweet_avatar"><img class=""image-responsive src="' + data.user_data['avatar_url'] + '"></div>');

    var tweet_text_container = $('<div class="tweet_text_container"></div>');
    var tweet_screen_name = $('<p class="tweet_screen_name">' + data.user_data['screen_name'] + '</p>');
    var tweet_user = $('<p class="tweet_user">' + data.user_data['name'] + '</p>');
    var tweet_text = $('<p class+"tweet_text">' + data.text + '</p>');

    tweet_text_container.append(tweet_screen_name).append(tweet_user).append(tweet_text);

    tweet_footer.append(tweet_avatar).append(tweet_text_container);

    tweet_media_container.append(tweet_media);

    tweet_container.append(tweet_media).append(tweet_footer);

    $('#content').prepend(tweet_container);
}

function setStatus(msg) {
    console.log('Connection Status : ' + msg);
}
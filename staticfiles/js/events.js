/**
 * Created by orehush on 3/15/16.
 */

var sneakers_url = '/sneakers/';

$(document).ready(function() {
    $.get(sneakers_url, function (response) {
        $('#sneakers').html(response);
    })
});

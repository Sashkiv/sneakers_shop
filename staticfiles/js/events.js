/**
 * Created by orehush on 3/15/16.
 */

var sneakers_url = '/sneakers/';
var sneakers_list_url = sneakers_url + 'list/';
var sneakers_params = '';

$(document).ready(function() {
    get_sneakers();
    get_list_sneakers();
});

function get_sneakers(params) {
    var url_request =  sneakers_url + '?' + sneakers_params;
    if ((params != '') && (params != undefined))
        url_request += params;
    $.get(url_request, function (response) {
        $('#sneakers').html(response);
    })
}

function get_list_sneakers() {
    $.get(sneakers_list_url, function (response) {
        $('#sneakers-index').html(response);
    })
}

function go_to_page(page) {
    var p = '&page=' + page;
    get_sneakers(p);
}

function refresh_sneakers() {
    var get_params = $('#sneakers-filter-form').serialize();
    sneakers_params = (get_params === '') ? sneakers_params : get_params;
    get_sneakers();
}

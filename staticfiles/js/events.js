/**
 * Created by orehush on 3/15/16.
 */

var sneakers_url = '/sneakers/';
var sneakers_list_url = sneakers_url + 'list/';
var sneakers_params = '';

$(document).ready(function() {
    if ($('#sneakers').html() !== undefined)
        get_sneakers();
    if ($('#sneakers-index').html() !== undefined)
        get_list_sneakers();
    $('.carousel').carousel({
      interval: 6000
    })
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
        var sneakers_index = $('#sneakers-index');
        var sneakers = $(response).filter('.sneakers');
        for (var i = 0; i < sneakers.length - 2; i+=3) {
            var div_item = '<div class="item">'
                + sneakers[i].outerHTML
                + sneakers[i+1].outerHTML
                + sneakers[i+2].outerHTML
                + '</div>';

            sneakers_index.append(div_item);
        }
        $('#sneakers-index > .item').first().addClass('active');
    });
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

/**
 * Created by orehush on 3/15/16.
 */

var sneakers_url = '/sneakers/';
var promo_url = '/sneakers/promo_list/';
var sneakers_list_url = sneakers_url + 'list/';
var sneakers_params = '';
var sneakers_images = [];
var current_image_index = 0;

$(document).ready(function() {
    if ($("#promo-slider").html() !== undefined)
        get_promo_list();
    if ($('#sneakers').html() !== undefined)
        get_sneakers();
    if ($('#sneakers-index').html() !== undefined)
        get_list_sneakers();
    if ($('#sneakers-detail').html() !== undefined)
    {
        events_for_image_detail();
        sneakers_images = $('.detail-img-small');
    }

    $('.carousel').carousel({
      interval: 6000
    });
});

function reset_form() {
    sneakers_params = '';
    get_sneakers();
}

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

function get_promo_list() {
    $.get(promo_url, function (response) {
        $('#promo-slider').html(response);
        $('#promo-slider > .item').first().addClass('active');
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

function events_for_image_detail() {
    var images = $('.detail-img-small');
    images.first().addClass('active');
    $(images).on('click', function () {
        $('#detail-img').find('img').attr('src', this.src);
        images.removeClass('active');
        $(this).addClass('active');
        for (var i = 0; i < sneakers_images.length; i++)
            if (sneakers_images[i] == this)
            {
                current_image_index = i;
                break
            }
    });

}

function set_current_image(index) {
    if (index < sneakers_images.length && index >= 0)
        sneakers_images[index].click();
}

function next_image() {
    if (current_image_index < sneakers_images.length - 1)
        current_image_index++;
    set_current_image(current_image_index);
}

function prev_image() {
    if (current_image_index > 0)
        current_image_index--;
    set_current_image(current_image_index);
}

function order() {
    var url = $('#order-sneakers').attr('action'); // the script where you handle the form input.
    $.ajax({
        type: "POST",
        url: url,
        data: $("#order-sneakers").serialize(),
        success: function(data)
        {
            $("#order-sneakers").hide();
            $("#success").show();
        },
        error:  function(xhr, str) {
            $("#order-sneakers").hide();
            $("#error").show();
        }
    });
}

function show_form() {
    $("#order-sneakers").show();
    $("#error").hide();
}

function close_popup() {
    $("#dialog").dialog('close');
}

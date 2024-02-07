(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);
    
    
    // Initiate the wowjs
    new WOW().init();
    
    
   // Back to top button
   $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });


    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    $(".myform-btn").on("click", () => {
        $("#myform").toggleClass("form-hide form-show")
    })

    $(".geoForm-btn").on("click", () => {
        $("#geoForm").toggleClass("form-hide form-show")
    })

    $(".demandeMainOeuvre-btn").on("click", () => {
        $("#demandeMainOeuvreForm").toggleClass("form-hide form-show")
    })

    $(".inscrireService-btn").on("click", () => {
        $("#inscrireServiceForm").toggleClass("form-hide form-show")
    })

    $(".demanderService-btn").on("click", () => {
        $("#demanderServiceForm").toggleClass("form-hide form-show")
    })

    $(".commis-btn").on("click", () => {
        $("#commisForm").toggleClass("form-hide form-show")
    })

    $(".top-search-btn").on("click", () => {
        $("#SearchBar").toggleClass("form-hide form-show")
    })

    $(".login-btn").on("click", () => {
        $("#login").toggleClass("form-hide form-show")
    })


    $(".item-button").on("click", () => {
        $(".sub-secteurs").toggleClass("sub-hide sub-show")
    })

     // Profile menu responsive
    $('.profile-menu-btn').click(()=>{
        $('.menu').toggleClass('hide-menu show-menu');
    })

     // Admin menu responsive
    $('#admin-menu-bars').click(()=>{
        $('.dashboard .sidebar').toggleClass('hide show');
        $('.dashboard .main-admin').toggleClass('full aside');
    })

    $('.hero-banner').slick({
        autoplay: true,
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
    })

})(jQuery);


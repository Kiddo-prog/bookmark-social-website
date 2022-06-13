(function () {
  var jquery_version = "3.6.0";
  var site_url = "127.0.0.1:8000";
  var static_url = site_url + "/static/";
  var min_height = 100;
  var min_width = 100;
  const bookmarklet = (msg) => {
    // create container for images
    var css = jQuery("<link>");
    css.attr({
      rel: "stylesheet",
      type: "text/css",
      href:
        static_url +
        "css/bookmarklet.css?r=" +
        Math.floor(Math.random() * 99999999999999999999),
    });
    jQuery("head").append(css);

    box_html =
      '<div id="bookmarklet"><a href="./" id="close">&times;</a><h1>Select an image to bookmark</h1><div class="images"></div></div>';
    jQuery("body").append(box_html);
    jQuery("#bookmarklet #close").on(function () {
      jQuery("#bookmarklet").remove();
    });
  };

  // Display each image in website
  jQuery.each(jQuery('img[src$="jpg"]'), function (index, image) {
    if (
      jQuery(image).width() >= min_width &&
      jQuery(image).height() >= min_height
    ) {
      image_url = jQuery(image).attr("src");
      jQuery("#bookmarklet .images").append(
        '<a href={% url "images:create" %}><img src="' + image_url + '" /></a>'
      );
    }
  });

  jQuery("#bookmarklet .images a").on(function (e) {
    e.preventDefault();
    selected_image = jQuery(this).children("img").attr("src");
    jQuery("#bookmarklet").hide();
    window.open(
      site_url +
        "images/create/?url=" +
        encodeURIComponent(selected_image) +
        "&title=" +
        encodeURIComponent(jQuery("title").text()),
      "_blank"
    );
  });

  if (typeof window.jQuery != "undefined") {
    bookmarklet();
  } else {
    var conflict = typeof window.$ != "undefined";
    var script = document.createElement("script");
    script.src =
      "//ajax.googleapis.com/ajax/libs/jquery/" +
      jquery_version +
      "/jquery.min.js";
    document.head.appendChild(script);
    var attempt = 15;
    (function () {
      if (typeof window.jQuery == "undefined") {
        if (--attempt > 0) {
          window.setTimeout(arguments.callee, 250);
        } else {
          alert("An error occured while loading jquery");
        }
      } else {
        bookmarklet();
      }
    })();
  }
})();

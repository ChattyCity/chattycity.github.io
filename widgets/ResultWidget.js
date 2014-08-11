(function ($) {

AjaxSolr.ResultWidget = AjaxSolr.AbstractWidget.extend({
  start: 0,

  beforeRequest: function () {
    $(this.target).html($('<img>').attr('src', 'images/ajax-loader.gif'));
  },

  facetLinks: function (facet_field, facet_values) {
    var links = [];
    if (facet_values) {
      for (var i = 0, l = facet_values.length; i < l; i++) {
        if (facet_values[i] !== undefined) {
          links.push(
            $('<a href="#"></a>')
            .text(facet_values[i])
            .click(this.facetHandler(facet_field, facet_values[i]))
          );
        }
        else {
          links.push('no items found in current selection');
        }
      }
    }
    return links;
  },

  facetHandler: function (facet_field, facet_value) {
    var self = this;
    return function () {
      self.manager.store.remove('fq');
      self.manager.store.addByValue('fq', facet_field + ':' + AjaxSolr.Parameter.escapeValue(facet_value));
      self.doRequest();
      return false;
    };
  },

  afterRequest: function () {
    $(this.target).empty();
    for (var i = 0, l = this.manager.response.response.docs.length; i < l; i++) {
      var doc = this.manager.response.response.docs[i];
      $(this.target).append(this.template(doc));

      var items = [];
      items = items.concat(this.facetLinks('topics', doc.hashtags));

      var $links = $('#links_' + doc.id);
      $links.empty();
      for (var j = 0, m = items.length; j < m; j++) {
        $links.append($('<li></li>').append(items[j]));
      }
    }
  },

  template: function (doc) {
    var snippet = '';
    
    if (doc.tweet.length > 300) {
      snippet += doc.tweet.substring(0, 300);
      snippet += '<span style="display:none;">' + doc.tweet.substring(300);
      snippet += '</span> <a href="#" class="more">more</a>';
    }
    else {
      snippet += 'Date:&nbsp;' + moment(doc.tstamp).format('MMMM Do YYYY, h:mm:ss a') + 
      '<br>City:&nbsp;' + doc.src_city + ' &#8594; ' + doc.dest_city + 
      '<br>Sentiment:&nbsp;' + doc.sentiment;
    }

	var autolinker = new Autolinker();
	var linkedTweet = autolinker.link(doc.tweet);

//	var test = '<div title="' + snippet + '" class="tooltip"><span title=""><h2>' + doc.tweet + '</h2></span></div>'
	//var linkedTest = autolinker.link(test);
	//var output = test;

	//var output = '<a href="#" title="' + snippet + '" class="tooltip"><span><h2>' + linkedTweet + '</h2></span></a>'
	
    var output = '<span class="trigger-element" data-tipped-options="position: \'left\', size: \'large\'" data-content="'+snippet+'"><h2>' + linkedTweet + '</h2></span>';
  //output += '<p id="links_' + doc.id + '" class="links"></p>';
   // output += '<p>' + snippet + '</p></div>';
  $(document).ready(function() {
    Tipped.create('.trigger-element', function() {
      return {
        content: $(this).data('content')
      };
    }, {
      skin: 'light'
    });
  });
  
    return output;
  },



  init: function () {
    $(document).on('click', 'a.more', function () {
      var $this = $(this),
          span = $this.parent().find('span');

      if (span.is(':visible')) {
        span.hide();
        $this.text('more');
      }
      else {
        span.show();
        $this.text('less');
      }

      return false;
    });
  }
});

})(jQuery);
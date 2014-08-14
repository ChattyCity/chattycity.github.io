var Manager;

(function ($) {

  $(function () {
    Manager = new AjaxSolr.Manager({
      solrUrl: 'http://54.164.33.84:8983/solr/collection1/'
    });
    Manager.addWidget(new AjaxSolr.ResultWidget({
      id: 'result',
      target: '#docs'
    }));
    
    Manager.addWidget(new AjaxSolr.PagerWidget({
      id: 'pager',
      target: '#pager',
      prevLabel: '&lt;',
      nextLabel: '&gt;',
      innerWindow: 1,
      renderHeader: function (perPage, offset, total) {
        $('#pager-header').html($('<span></span>').text('displaying ' + Math.min(total, offset + 1) + ' to ' + Math.min(total, offset + perPage) + ' of ' + total));
      }
    }));
    var fields = [ 'tweet', 'hashtags', 'src_city', 'dest_city' ];
    for (var i = 0, l = fields.length; i < l; i++) {
      Manager.addWidget(new AjaxSolr.TagcloudWidget({
        id: fields[i],
        target: '#' + fields[i],
        field: fields[i]
      }));
    }
    Manager.addWidget(new AjaxSolr.CurrentSearchWidget({
      id: 'currentsearch',
      target: '#selection'
    }));
    Manager.addWidget(new AjaxSolr.AutocompleteWidget({
      id: 'text',
      target: '#search',
      fields: [ 'tweet', 'hashtags', 'src_city', 'dest_city' ]
    }));
    Manager.addWidget(new AjaxSolr.CalendarWidget({
      id: 'calendar',
      target: '#calendar',
      field: 'tstamp'
    }));
    Manager.addWidget(new AjaxSolr.SentimentGroupWidget({
  id: 'sentiment',
  target: '#sentiment',
  field: 'sentiment',
  fields: ['sentiment']
}));
    Manager.init();
    Manager.store.addByValue('q', '*:*');
    var params = {
      facet: true,
      'facet.field': [ 'tweet', 'hashtags', 'src_city', 'dest_city', 'sentiment' ],
      'facet.limit': 35,
      'facet.mincount': 5,
      'f.topics.facet.limit': 50,
      'f.sentiment.facet.limit': 10,
	  'f.sentiment.facet.range.start': -1,
	  'f.sentiment.facet.range.end': 1,
	  'f.sentiment.facet.range.gap': 0.1,
      'facet.date': 'tstamp',
      'facet.date.start': '2014-07-06T00:00:00.000Z/DAY',
      'facet.date.end': '2014-07-31T00:00:00.000Z/DAY',
      'facet.date.gap': '+1DAY',
      'json.nl': 'map'
    };
    for (var name in params) {
      Manager.store.addByValue(name, params[name]);
    }
    Manager.doRequest();
  });

})(jQuery);

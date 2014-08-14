(function ($) {
AjaxSolr.SentimentGroupWidget = AjaxSolr.AbstractFacetWidget.extend({
  afterRequest: function () {
    if (this.manager.response.facet_counts.facet_fields[this.field] == undefined) {
      $(this.target).html(AjaxSolr.theme('no_items_found'));
      return;
    }

    var maxCount = 0;
    var objectedItems = [];
    var start = this.manager.response.facet_counts.facet_ranges[this.field].start;
    var gap = this.manager.response.facet_counts.facet_ranges[this.field].gap;
    var loopCounter = 0;
    for (var count in this.manager.response.facet_counts.facet_ranges[this.field].counts) {
      rangeStart = start + gap * loopCounter;
      rangeEnd = rangeStart + gap;            
      label = rangeStart + ' TO ' + rangeEnd;
		loopCounter++;
      facet = this.manager.response.facet_counts.facet_fields[this.field];
      objectedItems.push({ label: label, count: this.manager.response.facet_counts.facet_ranges[this.field].counts[count] });
    }

    objectedItems.sort(function (a, b) {
      return parseFloat(a.label) > parseFloat(b.label) ? -1 : 1;
    });

    $(this.target).empty();

    for (var i = 0, l = objectedItems.length; i < l; i++) {
      var label = '[' + objectedItems[i].label + ']';
      $(this.target).append(AjaxSolr.theme('sentimentgroup', label, objectedItems[i].count, this.clickHandler(label)));
    }
  },

  fq: function (label, exclude) {
    var fq_value = label;
    return (exclude ? '-' : '') + this.field + ':' + fq_value;
  }
});

})(jQuery);

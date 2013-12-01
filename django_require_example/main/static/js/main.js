requirejs.config({
  paths: {
    jquery: 'vendor/jquery-1.10.2'
  }
});

require(['jquery'], function ($) {
  $(function () { alert('hello!'); });
});
'use strict';


// Declare app level module which depends on filters, and services
angular.module('mininote', [
  'ngRoute',
  'mininote.filters',
  'mininote.services',
  'mininote.directives',
  'mininote.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/notes', {templateUrl: 'partials/notes.html', controller: 'NotesCtrl'});
  $routeProvider.otherwise({redirectTo: '/notes'});
}]);

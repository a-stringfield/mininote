'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
var services = angular.module('mininote.services', ["ngResource"]);

services.value("version", "0.1");

services.factory("NotesFactory", ["$resource",
                                  function($resource){
                                      return $resource("/notes", {}, {
                                          query: {method: 'GET', params: {}, isArray:true},
                                          create: {method: 'POST'}
                                      });
                                  }]);

services.factory("NoteFactory", ["$resource",
                                  function($resource){
                                      return $resource("/notes/:id", {}, {
                                          show: {method: 'GET', params: {id: "@id"}},
                                          update: {method: 'PUT', params: {id: "@id"}},
                                          delete: {method: 'DELETE', params: {id: "@id"}}
                                      });
                                  }]);

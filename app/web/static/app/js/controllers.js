'use strict';

/* Controllers */

angular.module('mininote.controllers', [])
  .controller('NotesCtrl', ['$scope', '$http', 'NotesFactory', 'NoteFactory', function($scope, $http, NotesFactory, NoteFactory) {
      $scope.about = {};
      $http({method:'GET', url:'/about'}).success(function (data,status,headers,config) {
          $scope.about = data;
      });
      $scope.notes = NotesFactory.query();
      $scope.note = {};
      $scope.addNewNote = function() {
          NotesFactory.create($scope.note);
          $scope.notes = NotesFactory.query();
          $scope.note = {};
      };
      $scope.updateNote = function(noteId) {
          NoteFactory.delete({id: noteId});
          $scope.notes = NotesFactory.query();
      };
  }]);

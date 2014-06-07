'use strict';

/* jasmine specs for controllers go here */

describe('controllers', function(){
  beforeEach(module('mininote.controllers'));

  it('should ....', inject(function($controller) {
    //spec body
    var notesCtrl = $controller('NotesCtrl', { $scope: {} });
    expect(notesCtrl).toBeDefined();
  }));
});

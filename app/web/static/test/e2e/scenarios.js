'use strict';

/* https://github.com/angular/protractor/blob/master/docs/getting-started.md */

describe('mininote', function() {

  browser.get('index.html');

  it('should automatically redirect to /notes when location hash/fragment is empty', function() {
    expect(browser.getLocationAbsUrl()).toMatch("/notes");
  });


  describe('notes', function() {

    beforeEach(function() {
      browser.get('index.html#/notes');
    });

    it('should render notes when user navigates to /notes', function() {
      expect(element.all(by.css('[ng-view] h5')).first().getText()).
        toMatch(/You don't have any notes./);
    });

  });

});

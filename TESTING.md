# Testing

Return back to the [README.md](README.md) file.

All features of Poetic Society have been tested through:
- Code validation of HTML, CSS, Python
- Browser compatability in Chrome, Firefox and Opera
- Responsiveness on mobile, tablet and desktop
- Lighthouse
- Defensive programming
-  User stories

## Code Validation

All files in Poetic Society have been validated through HTML, CSS and Python validators.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https://poetic-society-f2599d0af047.herokuapp.com/) | ![screenshot](documentation/html-home.png) | Pass: No Errors |
| View Poem | [W3C](https://validator.w3.org/nu/?doc=https://poetic-society-f2599d0af047.herokuapp.com/view_poem/2) | ![screenshot](documentation/html-viewpoem.png) | Pass: No Errors |
| Register | [W3C](https://validator.w3.org/nu/?doc=https://poetic-society-f2599d0af047.herokuapp.com/accounts/signup/) | ![screenshot](documentation/html-register.png) | See under bugss 
| Login | [W3C](https://validator.w3.org/nu/?doc=https://poetic-society-f2599d0af047.herokuapp.com/accounts/login/) | ![screenshot](documentation/html-login.png) | Pass: No Errors |
| Contact |  [W3C](https://validator.w3.org/nu/?doc=https://poetic-society-f2599d0af047.herokuapp.com/contact) | ![screenshot](documentation/html-contact.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpoetic-society-f2599d0af047.herokuapp.com) | ![screenshot](documentation/css-validation.png) | Bootstrap |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/manage.py) | ![screenshot](documentation/python-mainmanage.png) | Pass: No Errors |
| main-settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/main/settings.py/) | ![screenshot](documentation/python-mainsettings.png) | Pass: No Errors |
| main-urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/main/urls.py) | ![screenshot](documentation/python-mainurls.png) | Pass: No Errors |
| contact-admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/admin.py) | ![screenshot](documentation/python-contactadmin.png) | Pass: No Errors |
|contact-forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/forms.py) | ![screenshot](documentation/python-contactforms.png) | Pass: No Errors |
|contact-models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/models.py) | ![screenshot](documentation/python-contactmodels.png) | Pass: No Errors |
|contact-urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/urls.py) | ![screenshot](documentation/python-contacturls.png) | Pass: No Errors |
|contact-views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/views.py) | ![screenshot](documentation/python-contactviews.png) | Pass: No Errors |
|poems-admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/admin.py) | ![screenshot](documentation/python-poemsadmin.png) | Pass: No Errors |
|poems-forms.py | [PEP8 CI]( https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/forms.py) | ![screenshot](documentation/python-poemsforms.png) | Pass: No Errors |
|poems-models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/models.py) | ![screenshot](documentation/python-poemsmodels.png) | Pass: No Errors |
|poems-urls.py | [PEP8 CI]( https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/urls.py) | ![screenshot](documentation/python-poemsurls.png) | Pass: No Errors |
|poems-views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/views.py) | ![screenshot](documentation/python-poemsviews.png) | Pass: No Errors |


## Browser Compatibility

I have tested the browser compatability in the three browsers below.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Opera](https://www.opera.com/download)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | View Poem | Registrate | Login | Add Poem | Logout | Contact | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-home.png) | ![screenshot](documentation/chrome-viewpoem.png) | ![screenshot](documentation/chrome-register.png) | ![screenshot](documentation/chrome-login.png) | ![screenshot](documentation/chrome-addpoem.png) |  ![screenshot](documentation/chrome-logout.png) |  ![screenshot](documentation/chrome-contact.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-home.png) | ![screenshot](documentation/firefox-viewpoem.png) | ![screenshot](documentation/firefox-register.png) | ![screenshot](documentation/firefox-login.png) | ![screenshot](documentation/firefox-addpoem.png) |  ![screenshot](documentation/firefox-logout.png) |  ![screenshot](documentation/firefox-contact.png) | Works as expected |
| Opera | ![screenshot](documentation/opera-home.png) | ![screenshot](documentation/opera-viewpoem.png) | ![screenshot](documentation/opera-registrate.png) | ![screenshot](documentation/opera-login.png) | ![screenshot](documentation/opera-addpoem.png) |  ![screenshot](documentation/opera-logout.png) |  ![screenshot](documentation/opera-contact.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | View Poem | Register | Login | Add Poem | Logout | Contact | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/mobile-home.png) | ![screenshot](documentation/mobile-viewpoem.png) | ![screenshot](documentation/mobile-register.png) | ![screenshot](documentation/mobile-login.png) |  ![screenshot](documentation/mobile-addpoem.png) |  ![screenshot](documentation/mobile-logout.png) | ![screenshot](documentation/mobile-contact.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/tablet-home.png) | ![screenshot](documentation/tablet-viewpoem.png) | ![screenshot](documentation/tablet-register.png) | ![screenshot](documentation/tablet-login.png) |  ![screenshot](documentation/tablet-addpoem.png) |  ![screenshot](documentation/tablet-logout.png) | ![screenshot](documentation/tablet-contact.png) | Works as expected |
| Desktop | ![screenshot](documentation/chrome-home.png) | ![screenshot](documentation/chrome-viewpoem.png) | ![screenshot](documentation/chrome-register.png) | ![screenshot](documentation/chrome-login.png) | ![screenshot](documentation/chrome-addpoem.png) |  ![screenshot](documentation/chrome-logout.png) |  ![screenshot](documentation/chrome-contact.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-mobile-home.png) | ![screenshot](documentation/lighthouse-desktop-home.png) | Some minor warnings |
| View Poem | ![screenshot](documentation/lighthouse-mobile-viewpoem.png) | ![screenshot](documentation/lighthouse-desktop-viewpoem.png) | Some minor warnings |
| Register | ![screenshot](documentation/lighthouse-mobile-register.png) | ![screenshot](documentation/lighthouse-desktop-register.png) | Some minor warnings |
| Login | ![screenshot](documentation/lighthouse-mobile-login.png) | ![screenshot](documentation/lighthouse-desktop-login.png) | Some minor warnings |
| Add Poem | ![screenshot](documentation/lighthouse-mobile-addpoem.png) | ![screenshot](documentation/lighthouse-desktop-addpoem.png) | Some minor warnings |
| Logout | ![screenshot](documentation/lighthouse-mobile-logout.png) | ![screenshot](documentation/lighthouse-desktop-logout.png) | Some minor warnings |

## Defensive Programming

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
MS3 (Flask) | MS4/PP4/PP5 (Django):
- Standard users should not be able to access pages intended for superusers

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| View Poem | | | | | |
| | Feature is expected to open poem when clicking on a chosen one | Tested the feature by doing clicking on poem | The feature behaved as expected, and it did open the clicked poem | Test concluded and passed | ![screenshot](documentation/home.png)![screenshot](documentation/viewpoem-success.png) |
| Register | | | | | |
| | Feature is expected to do open a registration form when the user clicks on register in the nav-bar  | Tested the feature by clicking on register in the nav-bar | The feature behaved as expected, and it did open the form | Test concluded and passed | ![screenshot](documentation/register.png) |
| | Feature is expected to registrate a new member and log in when the user fills in their chosen username, password and email | Tested the feature by filling in information | The feature behaved as expected, and successfully logged in as user | Test concluded and passed | ![screenshot](documentation/register-success.png) |
| Login | | | | | |
| | Feature is expected to do open a login form when the user clicks on login in the nav-bar  | Tested the feature by clicking on login in the nav-bar | The feature behaved as expected, and it did open a form | Test concluded and passed | ![screenshot](documentation/login.png) |
| | Feature is expected to login when the user fills in username, password and clicks on signin | Tested the feature by doing filling in the information and clicking sign in | The feature behaved as expected, and it successfully logged in user | Test concluded and passed | ![screenshot](documentation/login-success.png) |
| Add Poem | | | | | |
| | Feature is expected to do open a form to add a poem when the registered user clicks on add poem in the nav-bar  | Tested the feature by clicking on contact in the nav-bar | The feature behaved as expected, and it did open a form | Test concluded and passed | ![screenshot](documentation/addpoem.png) |
| | Feature is expected to add a poem to the site when user fills in a title, poem and clicks on add poem | Tested the feature by doing filling in information and clicking add poem | The feature behaved as expected, and it did add the poem | Test concluded and passed | ![screenshot](documentation/addpoem-success.png) |
| Edit Poem | | | | | |
| | Feature is expected to do open a form to edit poem when the registered user clicks on edit poem on one of their poems | Tested the feature by clicking on edit poem on logged in users added poem | The feature behaved as expected, and it did open the form | Test concluded and passed | ![screenshot](documentation/editpoem.png) |
| | Feature is expected to show the edited poem to the site when user changes the title or poem and clicks on edit poem | Tested the feature by doing filling in information and clicking edit poem | The feature behaved as expected, and it did add the poem | Test concluded and passed | ![screenshot](documentation/editpoem-success.png) |
| | Feature is expected to deny editing poem and redirect to view poem when user is logged out | Tested the feature by logging out then pasting edit_poem over view_poem in browser | The feature behaved as expected, and it did denied acccess | Test concluded and passed | ![screenshot](documentation/editpoem-denied.png) |
| Delete Poem | | | | | |
| | Feature is expected to do open a popup which says "Are you sure you want to delete this poem?" with the options "Yes" and "No" when the registered user clicks on delete poem on one of their poems | Tested the feature by clicking on "Delete Poem" on logged in users added poem | The feature behaved as expected, and it did open the form | Test concluded and passed | ![screenshot](documentation/deletepoem.png) |
| | Feature is expected to not delete the poem when the user clicks "No" and go back to viewing the poem | Tested the feature by doing clicking on no | The feature behaved as expected, and it did not delete the poem and went back to viewing the poem when user chose "No" | Test concluded and passed | ![screenshot](documentation/deletepoem-no.png) |
| | Feature is expected to deny deleting poem and redirect to view poem when user is logged out | Tested the feature by logging out then pasting delete_poem over view_poem in browser | The feature behaved as expected, and it did denied acccess | Test concluded and passed | ![screenshot](documentation/editpoem-denied.png) |
| | Feature is expected to delete the poem when the user clicks "Yes" | Tested the feature by doing clicking on "Yes" | The feature behaved as expected, and it did logout when user chose "Yes" | Test concluded and passed | ![screenshot](documentation/deletepoem-success.png) |
| Logout | | | | | |
| | Feature is expected to do open a logout page when the user clicks on logout in the nav-bar  | Tested the feature by clicking on logout in the nav-bar | The feature behaved as expected, and it did open the page for the logout procedure | Test concluded and passed | ![screenshot](documentation/logout.png) |
| | Feature is expected to logout and show the message "You Have Signed Out." when the user clicks "Sign Out" | Tested the feature by doing clicking on "Sign Out" | The feature behaved as expected, and it did logout and show the message when user clicked "Sign Out" | Test concluded and passed | ![screenshot](documentation/logout-success.png) |
| Contact | | | | | |
| | Feature is expected to do open a contact form when the user clicks on contact in the nav-bar  | Tested the feature by clicking on contact in the nav-bar | The feature behaved as expected, and it did open a form | Test concluded and passed | ![screenshot](documentation/contact.png) |
| | Feature is expected to say "Thank for the message!" when the user has filled in the boxes of name, email, message  | Tested the feature by clicking on contact in the nav-bar | The feature behaved as expected, and it did say "Thank for the message!" | Test concluded and passed | ![screenshot](documentation/contact-success.png) |

OR

| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature0.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to view poems, so that I can enjoy poetry. | ![screenshot](documentation/home.png) ![screenshot](documentation/viewpoem-success.png) |
| As a new site user, I would like to registrate as user, so that I can share poems on the site. | ![screenshot](documentation/register.png) ![screenshot](documentation/register-success.png) |
| As a returning user, I would like to view poems, so that I can enjoy poetry. | ![screenshot](documentation/home.png) ![screenshot](documentation/viewpoem-success.png) |
| As a returning site user, I would like to login, so that I can share poems. | ![screenshot](documentation/login.png)![screenshot](documentation/login-success.png) |
| As a returning site user, I would like to add poems, so that I can share my poems. | ![screenshot](documentation/addpoem.png)![screenshot](documentation/addpoem-success.png) |
| As a returning site user, I would like to edit my poems, so that I can correct spellings or improve my text. | ![screenshot](documentation/editpoem.png)![screenshot](documentation/editpoem-success.png) |
| As a returning site user, I would like to delete poems, so that I can secure posting my poem. | ![screenshot](documentation/deletepoem.png)![screenshot](documentation/deletepoem-success.png) |
| As a returning site user, I would like to logout, so that I can feel calm and secure. | ![screenshot](documentation/logout.png)![screenshot](documentation/logout-success.png) |
| As a site administrator, I should be able to add poems, so that I can share poems. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to edit poems, so that I can correct spelling or improve text. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to delete poems, so that I can keep the site as I want. | ![screenshot](documentation/feature09.png) |


## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

#### Unit Test Issues

## Bugs

-  `'include is not defined'` when trying to runserver.

    ![screenshot](documentation/bug-2.png)

    - To fix this, I made the code shorter and easier for me to comprehend.

      ![screenshot](documentation/bug-2-fix.png)

-  `missing destination file operand` after message

    ![screenshot](documentation/bug-3.png)

    - To fix this, I added the name destination file.

-  `CSRF verification failed` 

    ![screenshot](documentation/bug-5.png)

    - To fix this, I added the gitpod link to trusted origins in settings.py

    ![screenshot](documentation/bug-05-fix.png)


### GitHub **Issues**

https://github.com/ilswh/poetic-society/issues

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/ilswh/poetic-society/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [`include is not defined` when trying to runserver.](https://github.com/ilswh/poetic-society/issues/11) | Closed |
| [`missing destination file operand` after message](https://github.com/ilswh/poetic-society/issues/12) | Closed |
| [`CSRF verification failed`](https://github.com/ilswh/poetic-society/issues/13) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/ilswh/poetic-society/issues).

| Bug | Status |
| --- | --- |
| [register.html valdidation failed](https://github.com/ilswh/poetic-society/issues/14) | Open |
| [style.css valdidation failed](https://github.com/ilswh/poetic-society/issues/15) | Open |

## Unfixed Bugs

- Django-allauth has a known bug with the signup form. It adds <p> tags within another block element, and causes HTML validation errors from W3C:.

    ![screenshot](documentation/bug-6.png)

    - I have not yet attempted to fix this.

- Parse error.

    ![screenshot](documentation/css-validation.png)

    - I have not yet attempted to fix this because it is bootstrap.

There are no remaining bugs that I am aware of.

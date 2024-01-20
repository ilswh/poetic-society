# Testing

Return back to the [README.md](README.md) file.

I have tested Poetic Society through
- Code validation of HTML, CSS, Python
- Browser compatability in Chrome, Safari/ Firefox and Opera
- Responsiveness on mobile, tablet and desktop
- Lighthouse
- Defensive programming
-  User stories

... within all features which are the homepage, view poem, registrate, login & logout and add poem.

## Code Validation

All files in Poetic Society have been validated through HTML, CSS and Python validators.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/) | ![screenshot](documentation/html-validation-home.png) | Pass: No Errors |
| View Poem | [W3C](https://validator.w3.org/) | ![screenshot](documentation/html-validation-viewpoem.png) | Pass: No Errors |
| Registrate | [W3C](https://validator.w3.org/) | ![screenshot](documentation/html-validation-registrate.png) | Pass: No Errors 
| Login | [W3C](https://validator.w3.org/) | ![screenshot](documentation/html-validation-login.png) | Pass: No Errors |
| Add Poem | [W3C](https://validator.w3.org/) | ![screenshot](documentation/html-validation-addpoem.png) | Pass: No Errors |
| Logout |  [W3C](https://validator.w3.org/) | ![screenshot](documentation/html-validation-logout.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Filswh.github.io%2Fpoetic-society) | ![screenshot](documentation/css-validation-style.png) | Pass: No Errors |

### Python

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑
The CI Python Linter can be used two different ways.
- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click on.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).
    - Check the example table below for a live demo.
It's recommended to validate each file using the API URL.
This will give you a custom URL which you can use on your testing documentation.
It makes it easier to return back to a file to validate it again in the future.
Use the steps above to generate your own custom URLs for each Python file.
**IMPORTANT**: `E501 line too long` errors
You must strive to fix any Python lines that are too long ( >80 characters ).
In rare cases where you cannot break the lines [without breaking the functionality],
then by adding `# noqa` to the end of those lines will ignore linting validation.
`# noqa` = **NO Quality Assurance**
**NOTE**: You must include 2 *spaces* before the `#`, and 1 *space* after the `#`.
Do not use `# noqa` all over your project just to clear down validation errors!
This can still cause a project to fail, for failing to fix actual PEP8 validation errors.
Sometimes strings or variables get too long, or long `if` conditional statements.
These are acceptable instances to use the `# noqa`.
When trying to fix "line too long" errors, try to avoid using `/` to split lines.
A better approach would be to use any type of opening bracket, and hit Enter just after that.
Any opening bracket type will work: `(`, `[`, `{`.
By using an opening bracket, Python knows where to appropriately indent the next line of code,
without having to "guess" yourself and attempt to tab to the correct indentation level.
Sample Python code validation documentation below (tables are extremely helpful!).
**Note**: This gives examples of PP3 (Python-only), and Flask/Django files, so eliminate the ones not applicable to your own project.
🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/manage.py) | ![screenshot](documentation/py-validation-manage.png) | Pass: No Errors |
| main-settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/main/settings.py/) | ![screenshot](documentation/py-validation-mainsettings.png) | Pass: No Errors |
| main-urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/main/urls.py) | ![screenshot](documentation/py-validation-mainurls.png) | Pass: No Errors |
| contact-admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/admin.py) | ![screenshot](documentation/py-validation-contactadmin.png) | Pass: No Errors |
|contact-forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/forms.py) | ![screenshot](documentation/py-validation-contactforms.png) | Pass: No Errors |
|contact-models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/models.py) | ![screenshot](documentation/py-validation-contactmodels.png) | Pass: No Errors |
|contact-urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/urls.py) | ![screenshot](documentation/py-validation-contacturls.png) | Pass: No Errors |
|contact-views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/contact/views.py) | ![screenshot](documentation/py-validation-contactviews.png) | Pass: No Errors |
|poems-admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/admin.py) | ![screenshot](documentation/py-validation-poemsadmin.png) | Pass: No Errors |
|poems-forms.py | [PEP8 CI]( https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/forms.py) | ![screenshot](documentation/py-validation-poemsforms.png) | Pass: No Errors |
|poems-models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/models.py) | ![screenshot](documentation/py-validation-poemsmodels.png) | Pass: No Errors |
|poems-urls.py | [PEP8 CI]( https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/urls.py) | ![screenshot](documentation/py-validation-poemsurls.png) | Pass: No Errors |
|poems-views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/poetic-society/main/poems/views.py) | ![screenshot](documentation/py-validation-poemsviews.png) | Pass: No Errors |

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑
**IMPORTANT**: Django settings.py
The Django settings.py file comes with 4 lines that are quite long, and will throw the `E501 line too long` error.
This is default behavior, but can be fixed by adding `# noqa` to the end of those lines.
Example:
```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```
🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Browser Compatibility

I have tested the browser compatability in the three browsers below.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Opera](https://www.opera.com/download)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | View Poem | Registrate | Login | Add Poem | Logout | Contact | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-viewpoem.png) | ![screenshot](documentation/browser-chrome-registrate.png) | ![screenshot](documentation/browser-chrome-login.png) | ![screenshot](documentation/browser-chrome-addpoem.png) |  ![screenshot](documentation/browser-chrome-logout.png) |  ![screenshot](documentation/browser-chrome-contact.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-viewpoem.png) | ![screenshot](documentation/browser-firefox-registrate.png) | ![screenshot](documentation/browser-firefox-login.png) | ![screenshot](documentation/browser-firefox-addpoem.png) |  ![screenshot](documentation/browser-firefox-logout.png) |  ![screenshot](documentation/browser-firefox-contact.png) | Works as expected |
| Opera | ![screenshot](documentation/browser-opera-home.png) | ![screenshot](documentation/browser-opera-viewpoem.png) | ![screenshot](documentation/browser-opera-registrate.png) | ![screenshot](documentation/browser-opera-login.png) | ![screenshot](documentation/browser-opera-addpoem.png) |  ![screenshot](documentation/browser-opera-logout.png) |  ![screenshot](documentation/browser-opera-contact.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | View Poem | Registrate | Login | Add Poem | Logout | Contact | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-viewpoem.png) | ![screenshot](documentation/responsive-mobile-registrate.png) | ![screenshot](documentation/responsive-mobile-login.png) |  ![screenshot](documentation/responsive-mobile-addpoem.png) |  ![screenshot](documentation/responsive-mobile-addpoem.png) |  ![screenshot](documentation/responsive-mobile-logout.png)  ![screenshot](documentation/responsive-mobile-contact.png) || Works as expected |

| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-viewpoem.png) | ![screenshot](documentation/responsive-tablet-registrate.png) | ![screenshot](documentation/responsive-tablet-login.png) |  ![screenshot](documentation/responsive-tablet-addpoem.png) |  ![screenshot](documentation/responsive-tablet-addpoem.png) |  ![screenshot](documentation/responsive-tablet-logout.png)  ![screenshot](documentation/responsive-tablet-contact.png) || Works as expected |

| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-viewpoem.png) | ![screenshot](documentation/responsive-desktop-registrate.png) | ![screenshot](documentation/responsive-desktop-login.png) |  ![screenshot](documentation/responsive-desktop-addpoem.png) |  ![screenshot](documentation/responsive-desktop-addpoem.png) |  ![screenshot](documentation/responsive-desktop-logout.png)  ![screenshot](documentation/responsive-desktop-contact.png) || Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |
| View Poem | ![screenshot](documentation/lighthouse-viewpoem--mobile.png) | ![screenshot](documentation/lighthouse-viewpoem--desktop.png) | Some minor warnings |
| Registrate | ![screenshot](documentation/lighthouse-registrate-mobile.png) | ![screenshot](documentation/lighthouse-registrate-desktop.png) | Slow response time due to large images |
| Login | ![screenshot](documentation/lighthouse-login-mobile.png) | ![screenshot](documentation/lighthouse-login-desktop.png) | Slow response time due to large images |
| Add Poem | ![screenshot](documentation/lighthouse-addpoem-mobile.png) | ![screenshot](documentation/lighthouse-addpoem.desktop.png) | Slow response time due to large images |
| Logout | ![screenshot](documentation/lighthouse-logout-mobile.png) | ![screenshot](documentation/lighthouse-logout-desktop.png) | Slow response time due to large images |

## Defensive Programming

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑
Defensive programming (defensive design) is extremely important!
When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):
Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses
PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only
MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers
You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).
You should include any manual tests performed, and the expected results/outcome.
Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.
Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.
🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature01.png) |
| View Poem | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature01.2.png) |
| Registrate | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature02.png) |
| Login | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| Add Poem | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature05.png) |
| Logout | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature04.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature06.png) |

OR

| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature0.png) |

## User Story Testing

Testing user stories is actually quite simple, once you've already got the stories defined on your README.
Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |


#### Unit Test Issues

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).
This can be used for both "fixed" and "unresolved" issues.

## Bugs

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

https://github.com/ilswh/poetic-society/issues
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.
You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).
Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/ilswh/poetic-society/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/ilswh/poetic-society/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/ilswh/poetic-society/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/ilswh/poetic-society/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/ilswh/poetic-society/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/ilswh/poetic-society/issues/5) | Open |

## Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.
If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.


- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

There are no remaining bugs that I am aware of.

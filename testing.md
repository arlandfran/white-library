# Testing

To ensure that the development environment is consistent across different machines, the .vscode directory was commited to the repository to ensure that:

1. [Autopep8](https://pypi.org/project/autopep8/) is the provided python formatter
2. [Pylint](https://pylint.org/) is the default linter

This assumes that you are using Visual Studio Code as your code editor.

## Code Validation

### HTML

HTML was validated using the [W3C Markup Validator](https://validator.w3.org/).

### CSS

CSS styles were validated with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

### JS

Javascript was validated along the way with [ESLint](https://eslint.org/) by installing it via NPM and enabled it in VS Code.

### Python

Python code was linted along the way using [Pylint](https://pylint.org/) and enabling it in VS Code. Python code was also formatted using [Autopep8](https://pypi.org/project/autopep8/) through VS Code.

## User Story Testing

- As a user, I want to see all the available products for sale

Users can navigate to the products page and see all the products on sale

- As a user I want to filter products by category and price

Users can sort products by category and priceon the products page

- As a user I want to contact the site owner

Users can navigate to the Contact Us page and fill out the form to send feedback

- As a user I want to search for a specific product or term

Users can query products via the search bar and get a match by title or description

- As a user I want to view additional product information

Users can click on a product and be taken to a product details page for more information

- As a user I want to view the items in my cart

Users can view/add/remove items from their bag

- As a user I want to revisit my cart even after leaving or logging out

User's bags are cached and available for the next time the user vists the site

- As a user I want to purchase products securely

Users are able to make purchases on the store securely using Stripe

- As a user I want to verify my account

On sign up, users are sent verification emails and able to purchase after verifying

- As a user I want to create an account

Users can create an account and access their profile to view account information

- As a registered user I want to log out of my account

Users can log out of their account to prevent unauthorized access

- As a registered user I want to view my order history/account information/addresses

Users can access their profile which displays all their account information and edit certain information such personal details or addresses. Order summaries are read only.

- As a registered user I want to save products

Users can save products to a saved later list for later viewing

- As a user registered I want to change my password

Users can change their password from their profile

- As a registered user I want to reset my password via email

- Users can follow the forgot password process during log in and works good

- As an admin add/edit/delete products

Admins have crud capabilities through the profile menu

## Responsive Testing

Website responsiveness was tested on [Google's Mobile Friendly Test](https://search.google.com/test/mobile-friendly) - Passed and [Responsinator](https://www.responsinator.com/) - Mobile and tablet devices test.

## Accessibility Testing

Accessibility was tested using [WAVE](https://wave.webaim.org/). Microsoft's [Accessibility Insights for Web extension](https://accessibilityinsights.io/en/) was used to cross check other accessbility issues.

## Defensive Design

- If user is logged in, then the login and register pages redirect to the home page.

- If the user navigates to a page that does not exists then a 404 page is shown.

- Forms are properly validated e.g. Admins cannot create products with price < 0.

- Users are asked to confirm their delete before clicking deleting any products.

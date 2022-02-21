# White Library

An e-commerce store that specialises in limited edition books and/or collectibles.

**Deployed Link**: TBD

**Project Goals:**

- Provide a platform for customers to purchase mainly limited edition books from various authors/series and also purchase collectibles
- Demonstrate web development competencies by building an e-commerce store using Django and PostgreSQL

## UX

### User Stories

| As a/an           | I want to                                                  | So that I can                                                                         |
| ----------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| User              | See all the available products for sale                    | Browse and discover products I may like                                               |
| User              | Filter products by category and price                      | Easily discover/find products that I like or are in my budget                         |
| User              | Contact the site owner                                     | Ask questions, send feedback or report issues regarding the site                      |
| User              | Search for a specific product or term                      | Find product(s) easily and quickly                                                    |
| User              | View additional product information                        | Read the book synopsis, view additional images and see more details about the product |
| User              | View the items in my cart                                  | Add/remove items and view the total                                                   |
| User              | Revisit my cart even after leaving the site or logging out | Continue my shopping where I left off                                                 |
| User              | Purchase products securely                                 | Ensure that my account and payment methods details are safe                           |
| User              | Verify my account                                          | Confirm the creation of my account                                                    |
| Unregistered User | Create an account                                          | View past orders and edit my account information                                      |
| Unregistered User | Checkout as a guest                                        | Purchase from the store without creating an account                                   |
| Registered User   | Log in                                                     | View my order history, account information etc.                                       |
| Registered User   | Log out                                                    | Prevent unauthorized access on a shared device                                        |
| Registered User   | View my order history                                      | See my previous purchases and the status of any current orders                        |
| Registered User   | View/edit my account information                           | Update any details if needed                                                          |
| Registered User   | View/edit my payment methods                               | Update any payment methods if needed                                                  |
| Registered User   | View/edit my shipping/billing addresses                    | Update any addresses if needed                                                        |
| Registered User   | Save products                                              | View/buy them at a later date                                                         |
| Registered User   | Change my password                                         | Update my passwords if needed                                                         |
| Registered User   | Reset my password via email                                | Access my account in case I've forgotten my password                                  |
| Admin             | Add product(s)                                             | Add new products to the store                                                         |
| Admin             | Edit product(s)                                            | Update product details                                                                |
| Admin             | Delete product(s)                                          | Remove products from the store                                                        |

### Design

**Wireframes:** [View wireframes here](https://www.figma.com/file/bqkbaMzTWfMel4mjFswWrX/white-library?node-id=0%3A1)

**Typeface**: [Inter](https://rsms.me/inter/)

### Features

- Account registration/authentication
- Payment system
- Responsive design

## Architecture

### Models

> Code does not include any class methods, fields only.

**Category:**

```python
class Category(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
```

**Product:**

```python
class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    saved = models.BooleanField(default=False)
    author = models.CharField(max_length=254)
    release_date = models.CharField(max_length=254)
    signed_copy = models.CharField(max_length=254, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    book_format = models.CharField(max_length=254, null=True, blank=True)
```

**Order:**

```python
class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(
        blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')
```

**Order Line Item:**

```python
class OrderLineItem(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
```

**User Profile:**

```python
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label="Country", null=False, blank=False)
```

## Technologies Used

**Languages:** HTML, CSS, JavaScript, Python

**Front-end:**

- [Tailwind CSS](https://tailwindcss.com) - Utility CSS Framework

- [Tailwind Elements](https://tailwind-elements.com/) - Tailwind plugin that recreates Bootstrap components with Tailwind CSS

**Back-end:**

- [Django](https://www.djangoproject.com/) - High level Python web framework

**Packages:**

- [django-allauth](https://www.intenct.nl/projects/django-allauth/) - Reusable Django app for local and social authentication.

- [django-tailwind](https://github.com/timonweb/django-tailwind) - Integrates Tailwind CSS into Django projects.

- [django-bootstrap-icons](https://github.com/christianwgd/django-bootstrap-icons): - Embed Bootstrap SVG icons in Django templates.

- [django-countries](https://github.com/SmileyChris/django-countries/): - Django app that provides country choices for use with forms and a country field for models.

- [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks): - Customize HTML Form Fields using template filters.

**Tooling:**

- [Figma](https://www.figma.com/) - High-fidelity Wireframing

- [Visual Studio Code](https://code.visualstudio.com/) - Code Editor

- [Git](https://git-scm.com/) - Version Control System

- [Github](https://github.com/) - Code Hosting Platform

- [Heroku](https://www.heroku.com/) - Platform-as-a-Service Cloud Provider

- [Pylint](https://pylint.org/) - Code linter for Python.

- [django-pylint](https://github.com/PyCQA/pylint-django) - Pylint plugin for improving code analysis when analysing code using Django.

- [autopep8](https://github.com/hhatto/autopep8) - Code formatter for Python.

- [ESLint](https://eslint.org/) - Code linter for Javascript.

- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - VSCode extension for linting Markdown.

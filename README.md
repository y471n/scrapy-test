![Scrapinghub logo](scrapinghub.png)

# Trial Project: Product spider #

### Goal ###

The goal of this trial project is to create a spider with Scrapy to scrape product information from a retailer (uk.farnell.com). The specs are detailed below.

### Product spider ###

Create a Python 3.5+ spider to scrape all items in the Electrical, Engineering Software, and Wireless Modules & Adapters categories on http://uk.farnell.com/.
It should navigate down the product category tree (e.g.: Wireless Modules & Adapters / RF Modules / RF Power) to the lowest level and parse on a per-product basis.

If a product does not have information for a specific field, please omit the field.

Fields:

* url: (string) Url of the product being scraped
* brand: (string) Product Brand Name
* title (string) Product headline containing the brand and product name
* unit_price: (float) Unit price of the product
* overview: (string) Product Overview description, usually has advertising copy
* information: (string) Dict array of specification objects in {name: specname, value: specvalue}
* manufacturer: (string) Manufacturer
* manufacturer_part: (string) Manufacturer part number
* tariff_number (string): Tariff code/number
* origin_country (string): Origin country
* files: (string list) String array of "Technical Docs" titles (usually PDF or URL titles)
* file_urls: (string list) String array of "Technical Docs" URLs
* image_urls: (string list) String Array of additional image urls
* primary_image_url: (string) URL of the main product image
* trail: (string list) Ordered string array (highest level category first) of categories

### Deliverable ###

You have been given access to this private repository on bitbucket to deliver the code of this trial.

The spider should be written in Python 3.5+ and follow the PEP8 style guidelines.  Please commit shub's scrapinghub.yml file (with any sensitive information removed).  You should also run your completed spider in the cloud - you will receive an email with an invitation to a Scrapy Cloud project for this purpose (if you don't, please let us know).  Instructions for deploying with Python 3 can be found here: https://helpdesk.scrapinghub.com/support/solutions/articles/22000200387-deploying-python-3-spiders-to-scrapy-cloud


Please keep the followings points in mind when delivering your code:

1. Commit History. Don’t worry about delivering a clean commit history, do as many commits as you would do while working normally. Please do not squash everything into a single commit, we use the commit history to review the evolution of your work.
2. Code quality. The final version of your code will be considered finished and production-ready - please make sure the spider results are complete and look correct upon inspection. If that’s not the case please indicate it when you email us back for reviewing.
3. Spent time report. Please include a file “hours.txt” with a list of tasks you worked on and the durations you worked on them. You can be as detailed as you want, but a summary of high-level points is often enough (learning scrapy, spider design, implementation, testing, etc).

### Time limit ###

The time limit for this project is 20 working hours, you must deliver the project finished or not when you have spent 20 hours working on in.

### Deadlines ###

This project doesn’t have a deadline. Just submit the results as soon as you have them ready (but no sooner) including the spent time report. The sooner you submit, the sooner we will move to the next step.

### Confidentiality ###

Please don’t share code or specifications about this project with anyone outside Scrapinghub.

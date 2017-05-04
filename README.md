![Scrapinghub logo](scrapinghub.png)

# Trial Project: Product spider #

### Goal ###

The goal of this trial project is to create a spider with Scrapy to scrape product information from a retailer (uk.farnell.com). The specs are detailed below.

### Product spider ###

The spider should extract information about every product on: http://uk.farnell.com/.
It should navigate down the product category tree (e.g.: Semiconductors / Memory / DRAM) to the lowest level and parse on a per-product basis.

Some of these fields might not be present in every product in the page.

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
* files: (string list) String array of "Technical Docs" filenames (usually PDF or URL titles)
* file_urls: (string list) String array of "Technical Docs" URLs
* image_urls: (string list) String Array of additional image urls
* primary_image_url: (string) URL of the main product image
* trail: (string list) Ordered string array (highest level category first) of categories

### Deliverable ###

You have been given access to this private repository on bitbucket to deliver the code of this trial.

You will also need to deploy and run your spider in our Scrapy Cloud platform. You can create a Scrapy Cloud free account here: https://dash.scrapinghub.com

Once you are ready for us to review your project please let us know by sending us an email to jobs@scrapinghub.com, be sure to include the link to the Scrapy Cloud project.


Please keep the followings points in mind when delivering your code:

1. Commit History. Don’t worry about delivering a clean commit history, do as many commits as you would do while working normally. Please do not squash everything into a single commit, we use the commit history to review the evolution of your work.
2. Code quality. The final version of your code will be considered finished and production-ready (ideally tested). If that’s not the case please indicate it when you email us back for reviewing.
3. Spent time report. Please include a file “hours.txt” with the report of the hours you spent working on the project. You can be as detailed as you want, but a summary of high-level points is often enough (learning scrapy, spider design, implementation, testing, etc)

### Time limit ###

The time limit for this project is 20 working hours, you must deliver the project finished or not when you have spent 20 hours working on in.

### Deadlines ###

This project doesn’t have a deadline. Just submit the results as soon as you have them ready (but no sooner) including the spent time report. The sooner you submit, the sooner we will move to the next step.

### Confidentiality ###

Please don’t share code or specifications about this project with anyone outside Scrapinghub.

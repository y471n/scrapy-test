![Scrapinghub logo](scrapinghub.png)

# Trial Project: Product spider #

### Goal ###

The goal of this trial project is to create a spider with Scrapy to scrape artistic work information from a museum website. The specs are detailed below.

**Note:** The museum website was created for this trial and both it and the spider have no commercial value.

### Product spider ###

Create a Python 3.5+ spider to scrape all works in the In Sunsh and Summertime categories on http://pstrial-2018-05-21.toscrape.com/ .
It should navigate down the work browse tree (e.g.: Summertime / Wrapper From / Barn Owl) to the lowest level and parse on a per-work basis.

If a work does not have information for a specific field, please omit the field.

Fields:

* url: (string) Url of the work being scraped
* artist: (list of strings) List of artists for the work
* title: (string) Title of the work
* image: (string) URL of the image
* height: (float) Physical height in cm, only if available in cm
* width: (float) Physical width in cm, only if available in cm
* description: (string) Description of the work
* path: (string list) The names of categories visited to reach the item via the browse tree. Ex: ["Summertime", "Wrapper From", "Ao Shu"]

### Getting started

Scrapy is an application framework for crawling web sites and extracting structured data. 
It is a primary library used for data extraction at ScrapingHub. So that's a main reason why trial is focused on Scrapy.

For this assignment you'll need to modify `artworks/spiders/trial.py`, `assumptions.txt`,
`feedback.txt` and `hours.txt` files.

Using [basic spider](https://doc.scrapy.org/en/latest/intro/tutorial.html#our-first-spider) should be enough to complete the task.

However we have a comprehensive [tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html) which provides deeper insight into Scrapy.

Additional bonus points may be awarded to those who use [Items](https://doc.scrapy.org/en/latest/topics/items.html#module-scrapy.item) and [Pipelines](https://doc.scrapy.org/en/latest/topics/item-pipeline.html#item-pipeline) in the trial code. 
`Items` are used to keep data structured. `Pipelines` allows to run post-processing on the collected data, i.e. drop empty fields, etc.

Since trial is limited on time it's not a mandatory requirement to use `Items` or `Pipelines`.

#### Running locally

1. Scrapy allows to [run](https://doc.scrapy.org/en/latest/intro/tutorial.html#how-to-run-our-spider) any spider locally.
> scrapy crawl trial 

2. More than that you can also [debug](https://doc.scrapy.org/en/latest/topics/commands.html#shell) with Scrapy. 
It can be really useful if you getting responses different to the ones in browser or like to check selectors 
created quickly.
> $ scrapy shell <url_to_explore>
>
> ....  # experiment with response 


#### Running at Scrapy Cloud

This trial requires crawl at Scrapy Cloud as deliverable.

ScrapingHub using own [tool](https://shub.readthedocs.io/en/stable/quickstart.html) to make Scrapy Cloud deployments.

Important steps to make deployment in right way:

1. [login](https://shub.readthedocs.io/en/stable/quickstart.html#basic-usage) to Scrapy Cloud.
    > shub login

    You'll need to provide your ScrapinghuAPI key on this step. Key can be found at https://app.scrapinghub.com/account/apikey
2. [set](https://shub.readthedocs.io/en/stable/configuration.html#where-to-configure-shub) project id so tool would know the target for deployment.
    
    `scrapinghub.yml` file needs to be updated with the correct project id.
    
    It is coming at the url you received with the invitation to the trial:
    `https://app.scrapinghub.com/p/<project_id>/`
3. Run `shub deploy` to load code to Scrapy Cloud (aka SC).
4. Run `shub schedule trial` to start spider on SC (it is also possible to run spider in UI by hitting `Run` button).
5. Check your project page `https://app.scrapinghub.com/p/<project_id>/` to see collected data.


### Deliverable ###

* The spider, committed and pushed to this repository

    The spider should be written in Python 3.5+ and follow the PEP8 style guidelines.  Please also commit shub's scrapinghub.yml file (with any sensitive information removed).

    Please keep the followings points in mind when delivering your code:

    1. Commit History. Don’t worry about delivering a clean commit history, do as many commits as you would do while working normally. Please do not squash everything into a single commit, we use the commit history to review the evolution of your work.
    2. Code quality. The final version of your code will be considered finished and production-ready - please make sure the spider results are complete and look correct upon inspection. You can check the [online documentation](https://doc.scrapy.org) to learn about Scrapy's features and best practices.

* A complete run of your finished spider in Scrapy Cloud

    You will receive an email with an invitation to a Scrapy Cloud project for this purpose (if you don't, please let us know).  Instructions for deploying with Python 3 can be found here: https://helpdesk.scrapinghub.com/support/solutions/articles/22000200387-deploying-python-3-spiders-to-scrapy-cloud

* Spent time report

    Please include a file "hours.txt" with a list of tasks you worked on and the durations you worked on them. You can be as detailed as you want, but a summary of high-level points is often enough (learning scrapy, spider design, implementation, testing, etc). Keep in mind that this is not a time competition, a clean implementation is preferable over a quick one.

* Assumptions and decisions report

    Please document assumptions you made and reasons for decisions you made in a file called "assumptions.txt" in your repository.  We will refer to this if your code contains things we did not expect.

* Feedback
    
    We would appreciate any feedback as per this trial. Please put it to "feedback.txt"

### Time limit ###

We expect this project to take around 8-10 hours depending on your level of experience.  We don't want you to over-invest yourself in this project, so if you're still working after spending 16 hours please stop and submit what you've completed.

### Deadlines ###

This project doesn’t have a deadline. Just submit the results as soon as you have them ready (but no sooner) including the spent time report. The sooner you submit, the sooner we will move to the next step.

### Confidentiality ###

Please don’t share code or specifications about this project with anyone outside Scrapinghub.

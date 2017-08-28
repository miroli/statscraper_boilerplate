This repository contains boilerplate code for developing a scraper that conforms to the [statscraper](https://github.com/jplusplus/statscraper) API.

## Quick start

1. Clone this repository.
2. Rename the package.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Implement the methods defined in `SampleScraper.py`.
5. Share your scraper with the world (see section on publishing packages).

## Sharing your scraper

The recommended way to make your scraper available to other users is by publishing it as a package on PyPi. To do that, you need to [register an account](https://pypi.python.org/pypi?%3Aaction=register_form).

A full walkthrough of the publishing process can [be found here](http://peterdowns.com/posts/first-time-with-pypi.html). We have already set up the required files. Just configure your settings in `setup.py`.
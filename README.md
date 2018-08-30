# Python Intercept Kindle #
## Description ##
Fetch the latest articles from [The Intercept](https://theintercept.com)'s RSS
feed, convert, and send them to an Amazon Kindle device.

version 1.0

## Prerequisites ##
* Make sure to have [Calibre](https://calibre-ebook.com/) installed
* Insert your Kindle address (*recipient_address*) and the accepted sender address
(*sender_address*) into the `config.ini`-file.

## To Dos ##
* Limit the articles, which will be fetched, converted, and send to the Kindle device.
Only the articles from the current day should be fetched, not all, which are available
by the RSS feed.
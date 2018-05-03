# Google Image Link Scraper
Scrapes google image links, for any given search result.

You need to enable the "custom search api" in Google's Developer Console. (https://console.cloud.google.com/) once you have enabled the "custom search api", put your account key in "key" variable.

Once that is done you're going to have to head over to: https://cse.google.com/ and create your own Custom Search Engine. Once you create your CSE, click "modify". On the modify page, make sure you enable Image Searching. Then, on the same page, click "search engine id" and copy and paste that into the "cx" variable. Save your CSE and run main.py.


By John Sandoval, 2018.

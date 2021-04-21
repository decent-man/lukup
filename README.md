# lukup
A quick webscraper tool to lookup info from your favourite websites.

For now it can only do pure text. No image,javascript,video,etc. :(

<!--It uses JSON files as configurations so it can already scrape from websites given the correct json.-->

The program is very basic at the moment. So the resulting output may look messed up for certain websites.

## Usage

1. Select the search text you want to lookup.

2. Copy it to clipboard first.

3. Invoke lukup.

4. Lukup will show a list of websites it has profiles for.

   If the website you are looking for doesn't exist, choose **+ Add Website**.
    - Search for `ASPERO0`,`GETARO1`,etc on your website and paste the link of the resulting page that opens up.
    - Lukup will process the link and ask you for a proper search term appropriate according to the website.
    - Lukup will open the page in **Element Selection Mode**. Select the web element which has the information you look for.
    - There are two ways from here:
        1. By XPath:
            - In **Element Selection Mode**, the selected element will be highlighted in the inspector.
            - Right click the attribute and copy its xpath.
            - Paste the Xpath in lukup's setup window.
            - Lukup will do its thing and you can test the profile by using **Test**.
            - If it is incorrect or showing gibberish, you can either try again OR use the manual method.
        2. By Manual(Recommended):
            - In **Element Selection Mode**, the selected element will be highlighted in the inspector.
            - Enter the correct tag and attribute information into the appropriate fields.
            - Lukup will do its thing and you can test the profile by using **Test**.
            - If the test window displays contains the correct information then all is good, click **Save** and it should add it into the list.
            - If it is incorrect or showing gibberish, you can try again.
    - Provided all went well the selected element's profile will be added to the list.
5. Select the website in which you want to lookup information for.
6. Be Enlightened.

## Installation

**<STILL_IN_DEVELOPMENT>**


# Element Data

This section involves capturing accurate html tag information for lukup to scrape correctly.

1. In the opened webpage, select and click on the element that contains the information you want to fetch.

2. Upon clicking the element's tag will be highlighted.

3. Beyond this there are two ways you can proceed:
    1. **The XPATH method**:
        This method is the "easier" option, but as all things easy it comes with a higher chance of inaccuracy.
        - Right click on the `id` attribute of the tag and select Copy XPATH from within the menu/submenu.
        - Paste this information in the Xpath field.
        - Press the **Test** button.
        - Lukup will generate appropriate profiles for the website and launch the testing sample window.
        - If the information in the sample window is as expected then Save the configuration and exit the setup.
    2. **The Manual Method**(Recommended):
        This is the preferred method of grabbing element data. This method has the highest accuracy.
        Once the required tag is highlighted in the inspector:
        - Input the **tag** name into the **Tag** field. Usually these would be `div`,`span`,etc at the beginning right after `<`.
        - Choose any **attribute name** in the **tag** and input this into the **Attribute Name** field. Ideally the best choice is the `id`, but in some websites there maybe more than one elements with the same id - this will cause problems. You can however enter any attribute like `class`,`itemtype`,etc just make sure it is unique.
        - Enter the **attribute's value** in the **Attribute Value** field. This would be the value of the attribute you chose written after `=` within quotation marks.
        - E.g For a tag like `<div id="mw-content-text" class="main-results">`
            - `div` will go in the **Tag** field.
            - `id` OR `class` will go in **Attribute Name** field.
            - `mw-content-text` OR `main-results`(depending on above choice) will go in **Attribute Value** field. 
        - Press the **Test** button.
        - Lukup will generate appropriate profiles for the website and launch the testing sample window.
        - If the information in the sample window is as expected then Save the configuration and exit the setup.

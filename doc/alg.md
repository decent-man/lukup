## Algorithm:-

1. Master
  - Get Search term from user.
  - Print a menu selection to ask for website to search for.
  <!--- Load the skel and dataclass from file(s) for the website chosen.-->
  - Load the config.json for the website chosen.
  - Get the text from the element.
  - Print output.

2. Window
  - Take output of Master.
  - Draw a borderless window with 
    - a big text box 95% the size of the window.
    - a url button to navigate to the url, if needed.
  - Use the text output from Master.
  - Esc/qq to close.

3. Site-Setup(v2 -- needs Selenium)
  - Open the target website with Inspector.
  - Have the user select the parent element which corresponds to the text he is interested in.
  - Save all underlying object model from the selected element into a file. -- Called as skeleton.
  - Analyze the the whole object model below and build a dataclass to represent all text(maybe images).
  - Save this and all built model into files under the website's directory to be accesed by the master program.


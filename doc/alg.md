## Algorithm:-

1. Master
  - Get Search term from user.
  - Print a menu selection to ask for website to search for.
  <!--- Load the skel and dataclass from file(s) for the website chosen.-->
  - Load the config.json for the website chosen.
  - Get the stuff.
  - Print formatted output.

2. Site-Setup(v2 -- needs Selenium)
  - Open the target website with Inspector.
  - Have the user select the parent element which corresponds to the text he is interested in.
  - Save all underlying object model from the selected element into a file. -- Called as skeleton.
  - Analyze the the whole object model below and build a dataclass to represent all text(maybe images).
  - Save this and all built model into files under the website's directory to be accesed by the master program.


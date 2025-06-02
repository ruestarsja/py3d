Possible Logo or Banner???!!!

# py3d
## A 3D graphics renderer in Python and pygame

The main goal of this project is for me to play around and experiment with writing a 3d graphics renderer without use of tutorials. It's not yet meant to be code that's worth distributing as software; rather, it's a learning opportunity for me. Here's my goals:

* The program should be able to read in data about 3D objects, correctly place them in the virtual 3D space, and -- most importantly -- *display* those objects on the screen based on the location of the virtual camera representing the user.

    * If that's confusing, take a 3D game like Minecraft as an example: for a given block (object), the computer has to determine where it is, where the player (virtual camera) is, and then how that block should appear to the player on their screen. If the player is further away, the block should appear smaller; if they're not looking directly at it, it should be off to the side of the screen, etc.

* The user should also be able to move the virtual camera, much like moving a player in a 3D game.

* I will *not* follow any video or article tutorials for major functionalities of the project.

* I will always attempt to figure out how to implement a feature entirely without help first. If I am struggling significantly, I will turn to *research*, not tutorials.

* I *may* use tutorials on minor technical issues, such as how to perform a simple task in Python, but only after attempting to research it using the official documentation or other similar means.

* After successfully implementing all major features, I may begin to use more external help to find better or more efficient ways of approaching them, and rewrite parts of the program.

* In the future, as a university independent project, I will take a semester to rewrite the program in a lower-level programming language such as C or Java, and in doing so will move away from the pygame module and learn to draw to the screen directly.

In other words, my rules in building this project can be simplified to the following: try everything myself first, and when in need of help, focus on *research*, not tutorials. Learn *about* the thing I'm trying to do, rather than just being told *how* to do it.

## Installation Instructions

While this project isn't designed for public use, you're still welcome to install it if you want to play around with it.

**Note:** This isn't built to be easily installed by non-technical users. It's still doable, but you might find yourself a bit lost.
**Note:** I've only tested this project on my own device. There's no guarantee that it will work on other devices the same as it does on mine. If you have any issues, please feel free to submit a bug report (see the Issues tab on GitHub)!

### To Install:

1. **Download.** From [the main page of the repository](https://github.com/ruestarsja/py3d), click the green "Code" button. In the dropdown that appears, click "Download ZIP" at the bottom. If prompted, select a folder on your computer where you will remember it.

2. **Unzip.** Locate the ZIP file you have just downloaded. On most devices, you should be able to double-click the ZIP file to unzip it to a folder. If this succeeds, you should see a new folder appear in the same folder as the ZIP; the new folder should be titled "py3d-main". If it didn't work, refer to [this article on unzipping files](https://www.greengeeks.com/tutorials/unzip-files-computer-devices/). Once you have successfully unzipped the file, you can safely delete the ZIP file (*not* the new folder).

3. **Make sure you have Python installed.**

    a. **For Windows:** [Windows users can download the Python installer here](https://www.python.org/downloads/windows/). Under the "Stable Releases" header, look at the download links under the first listed version, and select the 64-bit, 32-bit, or ARM64 version depending on your device. To determine what version you need, press the Windows key + R, type "cmd", and hit enter to open a command prompt. Then type the following command:
    ```
        wmic OS get OSArchitecture
    ```
    and press enter. This should print out the correct version. You can safely close the command line, then select the respective version. Once the installer has downloaded, double-click on the newly downloaded file and follow the instructions to download Python. Make sure to select "Add python to PATH" when given the option.

    b. **For MacOS:** [Mac users can download the Python installer here](https://www.python.org/downloads/macos/). Under the "Stable Releases" header, select "Download macOS 64-bit universal2 installer" under the first listed version. Once the installer has downloaded, double-click on the newly downloaded file and follow the instructions to download Python.

    c. **For Linux:** Many Linux distributions come with Python preinstalled. Press Ctrl + Alt + T to open the terminal, then run the following command:
    ```
        python3 --version
    ```
    If this displays a version number, you already have Python installed. If it instead throws an error, you need to install Python. [Refer to this article to download Python for Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/). You may now safely close the terminal.

4. **Make sure you have pygame installed.**

    a. **For Windows:** Open the command line again (Windows key + R, type "cmd", and hit enter). Type the following command:
    ```
        py -m pip install -U pygame --user
    ```
    and hit enter. You may now safely close the command line.

    b. **For MacOS:** Click the search bar on the top bar of your screen (Spotlight Search) or open Launchpad. Type "terminal", then hit return to open the terminal. Type the following command:
    ```
        python3 -m pip install -U pygame --user
    ```
    and hit return. You may now safely close the terminal.

    c. **For Linux:** Open the terminal again (Ctrl + Alt + T). Run the following command:
    ```
        python3 -m pip install -U pygame --user
    ```
    You may now safely close the terminal.

5. **Run the program.** Navigate back to the newly created "py3d-main" folder. In it, you should see a file called py3d.py. Double click this file and, if prompted, select to run it with Python. If you see the code rather than a running program, don't fret! Close the code (without changing it). Right click on the py3d.py file, select "Open with..." (or similar), and then click Python. If this option does not appear, you'll need to run the file from the terminal/command line.

    a. **For Windows:** Right-click on the py3d.py file, and select "Copy as path". If you don't see it, first select "Show more options". Once you have copied the path, open the command line one more time (Windows key + R, type "cmd", then hit enter). Type `py` followed by a space, and then right-click and select "Paste". Hit enter, and the program should start.

    b. **For MacOS:** Right-click on the py3d.py file, and select "Copy 'py3d.py' as Pathname". Open the terminal one more time (Spotlight Search or Launchpad, type "terminal", then hit return). Type `python3` followed by a space, and then select from the top bar "Edit", then "Paste". Hit return, and the program should start.

    c. **For Linux:** If you're familiar with the terminal, just run `python3 <path/to/file/py3d.py>`. If you're not, right-click on the py3d.py file, and look for an option called "Copy as path" or similar. (I can't find a good resource for all distros, so if you're having trouble, look up "copy as path" followed by the name of your distro.) Once you have copied the path, open the terminal one more time (Ctrl + Alt + T). Type `python3` followed by a space, and then hit Ctrl + Shift + V to paste. (If this doesn't work, again, look up "paste in terminal" followed by the name of your distro.) Hit enter, and the program should start.

If you have any issues with installing and running the program, feel free to reach out to me via email [ruestarsja@gmail.com](mailto:ruestarsja@gmail.com) and I will do my best to help!

## How to Tweak the Project

If you're interested in editing the project in any way, there are a few ways to go about it, depending on what you want to do.

1. **I want to modify the code for myself, without using Git or GitHub.** Easy! Just download the files as instructed above (in "Installation Instructions"). All of the Python files are there, uncompressed, so you can edit them to your heart's content!

2. **I want to use Git or GitHub to work on my own copy of this project.** I'll assume you are familiar with how to use Git if this is your goal. If not, you should go watch some YouTube tutorials, get Git set up, and come back. Click the green "Code" button and select one of the URLs to copy. You can then use this URL to clone the repo via the terminal.

3. **I want to contribute directly to the project, rather than having my own copy.** As this is a learning opportunity for me, I'm not interested in having any contributors right now. Any pull requests submitted will be rejected. If you're interested in working on the project, I would recommend making your own copy to play around with using one of the methods above.

## Known Issues

This is still very early in development, and there are a lot of issues. The major ones are detailed below, and will be addressed in the future. Please don't submit an issue for them on GitHub, as I already know about them.

* Objects above or below the camera are displayed incorrectly, without foreshortening.

* Objects behind the camera are also rendered in front of the camera.

* The camera is not stopped when looking straight up or down, and instead can freely be flipped upside down.

* When freeing and regrabbing the mouse, the difference in position is used to move the camera, rather than leaving the camera as is.

## Like this project?

Consider a small donation to help support the development of this and other projects!
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y51FWJON)
<div id="top"></div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Iash5225/Project">
  </a>

<h3 align="center">CITS 3403 Project</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/Iash5225/Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Iash5225/Project">View Demo</a>
    ·
    <a href="https://github.com/Iash5225/Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/Iash5225/Project/issues">Request Feature</a>
  </p>
</div>

<!-- CONTRIBUTORS -->
<div align="center">
  <h4>Authors:</h4>
  <p>David Wang (23064036)</p>
  <p>Jean-Pierre le Breton (21118434)</p>
  <p>Iash Bashir (23059859)</p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The project brief is linked [here](https://teaching.csse.uwa.edu.au/units/CITS3403/) however the goal was tio build a general daily game similar to Wordle

The primary principles that were the key focus of our game are as follows :

 + **Engaging**, so that it looks good and a user wants to play it every day.
 + **Challenging**, so the user feels a sense of achievement
 + **Intuitive**, so that it is easy for a user to access

As wordle as is a highly popular game, we decided to to capitalise on the aspect of inputing words. Upon research we found that a blend of Tetris and Wordle could be possible. As the game is played, randomly generated letters will drop from the top and will begin to stack up at the bottom of the grid. It is up to the user to clear as much letters as they can by trying to fomulate a word to be submitted,by using either their keyboard or by clicking on the letters on the screen. The game will finish when the pile reaches to the top.


<p align="right">(<a href="#top">back to top</a>)</p>


## Launching

To launch on local host you must first clone the repository into a directory that suits with the following command:

```
git clone https://github.com/Iash5225/Project
```

Next create a virtual environment

```
python3 -m venv auth
```

Then activate the virtual environment

```
source auth/bin/activate
```

Next install the necessary requirements with the following:

```
pip install -r requirements.txt
```

Navigate to the cloned repository and then run the server with the following, additionally you can specify the host ip and port number with the --host and --port flags:

```
flask run
```

If you have not specified different host IP or port number the server will be reachable on localhost:5000.

## Unit tests and Validation

Our tests cover basic cases that are self explanatory in the function names and in the comments provided. To run our tests the venv must be active and the flask server must be running, our default unit tests uses Chrome webdriver.

Our validation was done on the W3C website found [here](https://validator.w3.org/) we put in the local host url and it passed both tests for HTML and CSS!

To make sure all dependencies are upto date for the chrome webdriver and chrome

```
sudo apt update
```

Download and install Chrome:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb
```

To install numpy for the selenium

```
pip install numpy
```

To run unit tests

```
coverage run -m test
```

To run selenium tests
```
coverage run -m systemtests
```

To check the coverage report of tests
```
coverage report -m
```


### Built With

* [Flask](https://flask.palletsprojects.com/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Iash5225/Project](https://github.com/Iash5225/Project)

<p align="right">(<a href="#top">back to top</a>)</p>


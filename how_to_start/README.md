# How to start



## Get Polymer

Create a new folder for your project. `cd` into it and install bower
```
$ npm install -g bower
``` 
Create a bower.json file which handles your package dependencies
```
$ bower init
``` 
Now install Polymer
```
$ bower install --save Polymer
``` 
You can install other elements you might need (check out the element catalog)
```
$ bower install --save PolymerElements/paper-button
``` 
If you discover problems installing, due to conncetion failures to github, try:
```
$ git config --global url."https://".insteadOf git://
```

## Connect to crossbar.io router

We created an element which connects to a crossbar router. You can download it with bower

```
bower install --save https://github.com/RecordEvolution/cb-connect.git
```
Now start a web server
```
$ python -m SimpleHTTPServer
```
[Here](localhost:8000/bower_components/cb-connect/) you can get a documentation of the cb-connect element.

## Start developing

Start by creating an index.html where you need to import the Polymer library. Then add the cb-connect element. Finaly write your own custom element, which can receive questions and submit answers. 
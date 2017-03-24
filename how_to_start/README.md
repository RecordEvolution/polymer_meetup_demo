# How to start

## Task
Build a quiz client, which connects to our quiz channel and receives questions. Display the questions and build an interface to submit your answers. If you correctly send them back to the channel (you find some explanation below), they should be displayed at our answer overview application. 

## Get Polymer

Create a new folder for your project. `cd` into it and install bower, if you haven't already done that.
```
$ sudo npm install -g bower
``` 
Create a bower.json file which handles your package dependencies
```
$ bower init
``` 
Now install Polymer and some utility elements
```
$ bower install --save Polymer
$ bower install --save PolymerElements/paper-elements
$ bower install --save PolymerElements/iron-elements
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
At [localhost:8000/bower_components/cb-connect/](localhost:8000/bower_components/cb-connect/) you can get a documentation of the cb-connect element.
If you add this element to your project you need to set the websocket uri (wsuri property) and the realm.
```html
<cb-connect wsuri="ws://192.168.0.121:8099/ws" realm="polymer_meetup" on-crossbar-connected="getSessionObject"></cb-connect>
```

This configuration should let you connect to our quiz channel.
As pointed out in the `cb-connect` API reference, the element fires an event when connected and returns a session object. If you manage to collect this object you can publish and subscribe to certain topics.
To receive quiz questions you need to subscribe to the topic: `re.meetup.question`

```javascript
// SUBSCRIBE to a topic to receive events
function onQuestion(args) {
   console.log("Got question:", args[0]);
}
session.subscribe('re.meetup.question', onQuestion);
```

You will then receive a question object, which contains the question and an id. Then you can send your answer by publishing an answer object to the topic `re.meetup.answer`, which should have the following structure `{user: 'someone', answer: 'answer to the question', id='1234'}`. The id should match the id collected from the question object and you should choose a unique user name.

```javascript
// PUBLISH an event
var answerObject = {user: 'someone', answer: 'answer to the question', id='1234'};
session.publish('re.meetup.answer', [answerObject]);
```
#### Further reading:
+ [crossbar.io](http://crossbar.io)
+ [autobahnJS](http://autobahn.ws/js/)

## Start developing

Start by creating an index.html where you need to import the Polymer library. Then [build your own custom element](https://www.polymer-project.org/1.0/start/first-element/step-2) where you include the `cb-connection` element. Your application should display the questions we send and should be able to submit your answers. [webcomponents.org](https://www.webcomponents.org/) provides a lot of useful elements you can use, e.g. `paper-input` or `paper-button`. 


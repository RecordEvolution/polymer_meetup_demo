#!bash
bower install
npm install
polymer build
ln -s bower_components quiz-client/bower_components
ln -s fonts quiz-client/fonts
ln -s images quiz-client/images
ln -s src quiz-client/src
cd quiz-client
polymer build
#!bash
bower install
npm install
polymer build
ln -s $PWD/bower_components $PWD/quiz-client/bower_components
ln -s $PWD/fonts $PWD/quiz-client/fonts
ln -s $PWD/images $PWD/quiz-client/images
ln -s $PWD/src $PWD/quiz-client/src

cd quiz-client
polymer build
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError


class AppSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        ## SUBSCRIBE to a topic and receive events
        ##
        # def onhello(msg):
        #     print("event for 'onhello' received: {}".format(msg))

        # sub = yield self.subscribe(onhello, 'com.example.onhello')
        # print("subscribed to topic 'onhello'")

        ## REGISTER a procedure for remote calling
        ##
        # def add2(x, y):
        #     print("add2() called with {} and {}".format(x, y))
        #     return x + y

        # reg = yield self.register(add2, 'com.example.add2')
        # print("procedure add2() registered")

        ## PUBLISH and CALL every second .. forever
        ##
        counter = 0
        questions = [
                        {'id': '4kjhs34j43', 'question': 'Which package manager is used to install Polymer elements?'},
                        {'id': '9qx3n85mpl', 'question': '1 + 1 = ?'},
                        {'id': 'j2h4jhn2b4', 'question': 'Which day of week is today?'},
                        {'id': '0v3afl12o5', 'question': 'When was Record Evolution founded?'},
                        {'id': '1p43n242jx', 'question': 'Which Polymer Element can be used to collect user input?'},
                        {'id': '10eumc4m4m', 'question': 'Which polymer template can be used to repeat html content?'},
                        {'id': '498hff3h3k', 'question': 'Is this the last question?'}                   
                        ]
        while True:

            ## PUBLISH an event
            ##
            # yield self.publish('re.meetup.question', counter)
            print("published to 'oncounter' with counter {}".format(counter))
            counter += 1

            # if counter < 16:
            #     yield self.publish('re.meetup.question', questions[0])
            # elif counter < 32:
            #     yield self.publish('re.meetup.question', questions[1])
            # elif counter < 64:
            #     yield self.publish('re.meetup.question', questions[2])
            # elif counter < 96:
            #     yield self.publish('re.meetup.question', questions[3])
            # elif counter < 128:
            #     yield self.publish('re.meetup.question', questions[4])
            # elif counter < 160:
            #     yield self.publish('re.meetup.question', questions[5])                
            # else:
            #     yield self.publish('re.meetup.question', questions[6])


            if counter < 600:
                yield self.publish('re.meetup.question', questions[0])
            elif counter < 1200:
                yield self.publish('re.meetup.question', questions[1])
            elif counter < 1800:
                yield self.publish('re.meetup.question', questions[2])
            elif counter < 2400:
                yield self.publish('re.meetup.question', questions[3])
            elif counter < 3000:
                yield self.publish('re.meetup.question', questions[4])
            elif counter < 3600:
                yield self.publish('re.meetup.question', questions[5])                
            else:
                yield self.publish('re.meetup.question', questions[6])


            ## CALL a remote procedure
            ##
            # try:
            #     res = yield self.call('com.example.mul2', counter, 3)
            #     print("mul2() called with result: {}".format(res))
            # except ApplicationError as e:
                ## ignore errors due to the frontend not yet having
                ## registered the procedure we would like to call
                # if e.error != 'wamp.error.no_such_procedure':
                #     raise e

            yield sleep(1)

if __name__ == '__main__':
   from autobahn.twisted.wamp import ApplicationRunner
   runner = ApplicationRunner(url =u"ws://127.0.0.1:8099/ws", realm=u"polymer_meetup")
   runner.run(AppSession)
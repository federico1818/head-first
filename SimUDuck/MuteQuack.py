from QuackBehavior import QuackBehavior


class MuteQuack(QuackBehavior):

    def quack(self):
        print('<< Silence >>')

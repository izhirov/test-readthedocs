
class Foo:
    """Foo class in foo module"""

    def __init__(self, config):
        self.config = config

    def bar(self, x: int) -> int:
        """Bar method.

        Arguments:
            x {int} -- Input

        Returns
            x {int} -- Output
        """

        return x


class Bar(Foo):
    """"Bar class in foo module

    Arguments:
        config {dict} -- Config dict
    """

    def __int__(self, config):
        self.config = config

    def foo(self, x: int) -> int:
        """Foo method.

        Arguments:
            x {int} -- Input

        Returns
            x {int} -- Output
        """

        return x

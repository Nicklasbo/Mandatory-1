class CA:
    """Elementary Cellular Automaton - by nick1423 Nicklas Embo

    Represents a range 1, 3-cell neighbourhood elementary cellular automaton."""

    def __init__(self, rule, init_state='0'*20+'1'+'0'*20):
        """Initialize the CA with the given rule and initial state."""
        self.rule = bin(rule)[2:].zfill(8)
        self.state = init_state

    def state(self):
        """Returns the current state."""
        return self.state

    def next(self):
        """Progress one step and then return the current state."""
        newstate = ""
        for i in range(len(self.state)):
            left = "0" if i == "0" else self.state[i - 1]
            right = "0" if i == len(self.state) - 1 else self.state[i + 1]
            index = int(left + self.state[i] + right, base=2)
            newstate += self.rule[len(self.rule) - 1 - index]
        self.state = newstate
        return self.state

    def run(self, num=18):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        def prettyPrint(state):
            print(state.replace("0", " ").replace("1", "*"))
        prettyPrint(self.state)
        for _ in range(num-1):
            self.next()
            prettyPrint(self.state)


ca = CA(169)

ca.run()

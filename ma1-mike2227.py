class CA:
    """Elementary Cellular Automaton - by mike2227 Mike Hemmje Jahn

    Represents a range 1, 3-cell neighbourhood elementary cellular automaton."""

    def __init__(self, rule, init_state = '0' * 20 + '1' + '0' * 20):
        """Initialize the CA with the given rule and initial state."""

        self.init_state = init_state
        self.default = init_state
        self.first = True
        bin_number = format(rule, "08b")
        self.binary_pattern = {
            "111": "",
            "110": "",
            "101": "",
            "100": "",
            "011": "",
            "010": "",
            "001": "",
            "000": "",
        }

        for index, key in enumerate(self.binary_pattern):
            self.binary_pattern[key] = bin_number[index]

    def state(self):
        """Returns the current state."""
        return self.init_state

    def next(self):
        """Progress one step and then return the current state."""

        if self.first:
            self.first = False
            return self.init_state

        state = self.state()

        # split every third digit into an array of join them as a string and add to array
        # -2 because there will be 2 and 1 zero left in array ( [000,00,0] )
        triple_array = ["".join(state[i:i + 3]) for i in range(len(state) - 2)]

        # match with binary pattern and join it back to a string
        self.init_state = ''.join(self.binary_pattern[pat] for pat in triple_array)

        # patting with zero on both sides
        self.init_state = f"0{self.init_state}0"

        return self.state()

    def run(self, num = 18):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        for i in range(num):
            print(self.next().replace("0", " ").replace("1", "*"))


#CA(90).run()

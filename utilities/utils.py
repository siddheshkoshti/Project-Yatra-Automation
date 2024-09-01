class Utils:
    def assertlistItemtext(self, list, value):
        for stop in list:
            print("The trxt is :" + stop.text)
            assert stop.text == value
            print("assert pass")
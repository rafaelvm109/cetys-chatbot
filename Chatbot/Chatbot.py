from loguru import logger


# ---------------------
## This class handles all chatbot interactions
# Main Program Entry
class Chatbot:
    def __init__(self):
        self._name = "Cecilia"

    # ---------------------
    ## Greeting used by the Chatbot
    def Greet(self, Greeting):
        logger.debug(f'{self._name}: Greeting  f{Greeting}')

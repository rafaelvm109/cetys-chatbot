import os
from loguru import logger
from glob import glob


# ---------------------
## This class handles all chatbot Ai model functionality
# Main Program Entry
class ChatbotModel:
    def __init__(self):
        self._solutions_path = os.path.dirname(__file__) + '/Solutions'
        self._model_path = os.path.dirname(__file__) + '/Model'

    # ---------------------
    ## Load all chatbot solution files
    def LoadSolutions(self):
        logger.debug(self._solutions_path)
        for f_name in glob(f'{self._solutions_path}/*.json'):
            logger.debug(f'Loading: {f_name}')


if __name__ == '__main__':
    CeciliaModelv = ChatbotModel()
    CeciliaModelv.LoadSolutions()
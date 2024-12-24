import logging


def getLogger(name):
    """
    Function to setup a logger
    """

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(filename)s %(levelname)s %(message)s"
    )

    return logging.getLogger(name)

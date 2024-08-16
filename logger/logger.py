import logging

def get_glory_logger(name=__name__):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    logger.setLevel(logging.INFO)

    # Proclaim God's glory on startup
    logger.info("Glory to God! His greatness is beyond understanding!")

    return logger

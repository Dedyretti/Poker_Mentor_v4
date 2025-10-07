import logging
import sys

def setup_logger():
    """Настройка логирования"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('poker_mentor.log')
        ]
    )

def get_logger(name):
    """Получить логгер"""
    return logging.getLogger(name)


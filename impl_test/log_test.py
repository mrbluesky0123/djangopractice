import logging
from logging.handlers import TimedRotatingFileHandler

def get_standard_logger(pgm_name):
    logger = logging.getLogger(pgm_name)

    # 로그 레벨 설정
    logger.setLevel(logging.DEBUG)
    
    # 콘솔 출력 핸들러
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    # 파일 저장 핸들러
    # 1시간마다 로그파일 교체
    log_dir = '/home/mrbluesky/mrbluesky_env/use_service/log/'
    log_filename = pgm_name + '.log'
    file_handler = logging.handlers.TimedRotatingFileHandler(filename=log_dir+log_filename, when='h', interval=1)
    logger.addHandler(file_handler)

    # 로그 포멧 설정
    formatter = logging.Formatter('[%(asctime)s](%(levelname)s)%(name)s : %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    return logger

if __name__ == '__main__':
    log = get_standard_logger('test')
    log.debug('aaaaa')


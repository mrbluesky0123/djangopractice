import time
import datetime
from point_use.common import ocblogger

def service(service_name):

    def service_wrapper(func):

        def wrapper(*args, **kwargs):

            # 로그 오픈
            logger = ocblogger.get_standard_logger(service_name)

            # 시작 시간 출력
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            logger.info('{0} service started at {1}'.format(service_name, timestamp))

            # 시작 시간 기록
            t1 = time.time()

            # 서비스 실행
            result = func(*args, **kwargs)

            # 종료 시간 기록
            t2 = time.time()

            # 종료 시간 출력
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            logger.info('{0} service finished at {1}'.format(service_name, timestamp))

            # 소요 시간 출력
            logger.info('Elapsed time: {0}'.format(str(t2 - t1)))

            return result

        return wrapper

    return service_wrapper
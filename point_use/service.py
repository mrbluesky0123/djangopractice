from point_use.models import *
<<<<<<< HEAD
from point_use.common.ocbdecorators import *
from point_use.common import ocblogger
=======
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
from datetime import datetime
import json
import urllib

<<<<<<< HEAD
######################################################
# 2019.02.06 # 사용 서비스 구현
# 2019.02.08 # 승인번호 채번 외부 API 연동
# 2019.02.10 # 서비스 Decorator 구현
# 2019.02.11 # 로깅 추가
######################################################

SERVICE_NAME = 'POINT_USE'

@service(SERVICE_NAME)
def point_use(request):
    # request: dict
    # response: dict
    
    logger = ocblogger.get_standard_logger(SERVICE_NAME)
    
=======
''' 사용 서비스 구현 '''
''' 2019. 02. 08 '''
def point_use(request):
    # request: dict
    # response: dict
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    response = {
        'ans_cd': '',
        'ans_msg': '',
        'aprv_dy': '',
        'aprv_tm': '',
        'aprv_no': '',
        'rmn_pnt': '',
        'rep_aprv_no': '',
    }
<<<<<<< HEAD
    
    # 입력값(null) 검증
    logger.info('Input data: {0}'.format(request))
=======
    print('###########' + str(type(request)))
    # 입력값(null) 검증
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    for data in request:
        if data is None:
            response['ans_cd'] = '1111'
            response['ans_msg'] = 'Invalid input'
            return response
<<<<<<< HEAD
    
    # 카드 검증
    crd_sts = Card.objects.get_card_status(request['crd_no'])
    logger.info('[crd_no: {0}][crd_sts: {1}]'.format(request['crd_no'], crd_sts))
=======

    # 카드 검증
    crd_sts = Card.objects.get_card_status(request['crd_no'])
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    if crd_sts == None:
        response['ans_cd'] = '2011'
        response['ans_msg'] = 'No card registered'
        return response
    elif crd_sts != 'A':
        response['ans_cd'] = '1112'
        response['ans_msg'] = 'Invalid card'
        return response
    
    # 회원 ID get
    mbr_id = Card.objects.get_mbr_id_by_crd_no(request['crd_no'])
<<<<<<< HEAD
    logger.info('[crd_no: {0}][mbr_id: {1}]'.format(request['crd_no'], mbr_id))
    
    # 회원 검증
    mbr_sts = Member.objects.get_member_status(mbr_id)
    logger.info('[mbr_id: {0}][mbr_sts: {1}]'.format(mbr_id, mbr_sts))
=======

    # 회원 검증
    mbr_sts = Member.objects.get_member_status(mbr_id)
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    if mbr_sts == None:
        response['ans_cd'] = '2012'
        response['ans_msg'] = 'No member exists'
        return response
    elif mbr_sts != 'A':
        response['ans_cd'] = '1113'
        response['ans_msg'] = 'Invalid member'
        return response
    
    # 가맹점 검증
    mcht_sts = Merchant.objects.get_merchant_status(request['mcht_no'])
<<<<<<< HEAD
    logger.info('[mcht_no: {0}][mcht_sts: {1}]'.format(request['mcht_no'], mcht_sts))
=======
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    if mcht_sts == None:
        response['ans_cd'] = '2013'
        response['ans_msg'] = 'No merchant exists'
        return response
    elif mcht_sts != 'A':
        response['ans_cd'] = '1114'
        response['ans_msg'] = 'Invalid merchant'
        return response

    # 포인트 검증
    point = Point.objects.get_point(mbr_id)
<<<<<<< HEAD
    logger.info('[mbr_id: {0}][point: {1}]'.format(mbr_id, point))
=======
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    if point < int(request['deal_amt']):
        response['ans_cd'] = '1115'
        response['ans_msg'] = 'Point insufficient'
        return response

    # 포인트 사용(차감)
    remain_point = point - int(request['deal_amt'])

    # 포인트 업데이트
    if Point.objects.update_point(mbr_id, remain_point) < 0:
        response['ans_cd'] = '2014'
        response['ans_msg'] = 'Something wrong'
        return response

    # 승인정보 받아오기
<<<<<<< HEAD
    # 외부 API 연동 (2019.02.08)
    mcht_fg = Merchant.objects.get_merchant_flag(request['mcht_no'])
    aprv_info = _get_approve_info(request['mcht_no'], mcht_fg)
    logger.info('Approve info from external API: {}'.format(aprv_info))
=======
    mcht_fg = Merchant.objects.get_merchant_flag(request['mcht_no'])
    aprv_info = _get_approve_info(request['mcht_no'], mcht_fg)
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    
    # 예외처리

    # 응답값 반환
    response['ans_cd'] = '0000'
    response['ans_msg'] = 'OK'
    response['aprv_dy'] = aprv_info['aprv_dy']
    response['aprv_tm'] = aprv_info['aprv_tm']
    response['rep_aprv_no'] = aprv_info['rep_aprv_no']
    response['rmn_pnt'] = remain_point
<<<<<<< HEAD

    return response

# 외부 API 연동 함수 (2018.02.08)
=======
    return response

''' 외부 API 연동 '''
''' 2019. 02. 08 '''
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
def _get_approve_info(mcht_no, mcht_fg):
    req_url = 'http://198.13.47.188:9090/spring5mvc_war/aprv_no'
    header = {'Content-Type': 'application/json'}
    body = {
	    "svc_modu_id": "APPROVE",
	    "telgrm_fg": "ON",
	    "onoff_mcht_fg": mcht_fg,
	    "mbrsh_pgm_id": "A",
	    "mcht_no": mcht_no
    }
    # data = bytes(urllib.parse.urlencode(body).encode())
<<<<<<< HEAD
    try:
        request = urllib.request.Request(url=req_url, data=json.dumps(body).encode('utf-8'), headers=header)
        response = urllib.request.urlopen(request).read().decode('utf-8')
        result = json.loads(response)
    except:
        result = {'aprv_dy':'20190228', 'aprv_tm':'000000', 'rep_aprv_no':'F8231231'}
    # print(result) 
=======
    request = urllib.request.Request(url=req_url, data=json.dumps(body).encode('utf-8'), headers=header)
    response = urllib.request.urlopen(request).read().decode('utf-8')
    result = json.loads(response)
    print(result) 
>>>>>>> b527ad9a329c26bc0a538151f3f26c824346bbb3
    return result
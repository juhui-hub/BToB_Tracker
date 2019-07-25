import cv2
import numpy as np

video_path='btob.mp4'
cap=cv2.VideoCapture(video_path) #동영상 로드

output_size = (187, 333) #(w,h) 핸드폰에 꽉차게 보임:375,667

#영상 저장 이건 어려워서 그냥 복붙만 하면 됨
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('%s_output.mp4' % (video_path.split('.')[0]), fourcc, cap.get (cv2.CAP_PROP_FPS),output_size) 
#비디오 모듈 초기화 
# FPS=Frame per Second :1 초당 프레임의 개수
#cap.get(cv2.CAP_PROP_FPS): cap에 로드된 동영상의 FPS를 반환
#size는 output_size


if not cap.isOpened(): #동영상 제대로 로드되면 True 반환
    exit() #프로그램 종료

tracker=cv2.TrackerCSRT_create() #CSRT 오브젝트 트래커를 초기화

#첫번째 프레임 설정
ret,img=cap.read() 

cv2.namedWindow('Select Window') #이 프로그램이 이 window에서 ROI 설정 (대소문자 구분)
cv2.imshow('Select Window',img) #첫번째 프레임 보여줌

#ROI 설정
rect=cv2.selectROI('Select Window',img,fromCenter=False,showCrosshair=True)
#ROI 설정해서 rect로 반환
#ing 센터에서 시작하지말고 중심점으로 해
cv2.destroyWindow('Select Window') #ROI 선택하면 윈도우 닫아

#tracker 초기화
tracker.init(img, rect) #오브젝트 트래커가 img와 rect를 따라가게 설정

while True:
    ret, img = cap.read() 
    #동영상 1프레임씩 읽어서 img변수에 저장 
    #비디오 끝나면 ret이 false됨

    if not ret:
        exit() #ret이 false면 종료

    success, box = tracker.update(img) #img에서 rect로 설정한 이미지와 비슷한 물체의 위치를 찾아 반환

    left, top, w, h = [int(v) for v in box] #box를 한번 돌때마다 나오는 값v를 int로 변환하여 순서대로 넣음
    center_x = left + w / 2
    center_y = top + h /2


    result_top = int (center_y - output_size[1]/2)
    result_bottom = int (center_y + output_size[1]/2)

    result_left = int (center_x - output_size[0]/2)
    result_right = int (center_x + output_size[0]/2)



    if (result_top <= 0): 
        result_top = 0
        result_bottom = 333

    if (result_bottom >= 720):
        result_bottom = 720
        result_top = 387

    if (result_left <= 0):
        result_left = 0
        result_right = 187

    if (result_right >= 1280):
        result_right = 0
         result_left = 
    
    
    print(result_top, result_bottom, result_left, result_right)
    result_img = img[result_top : result_bottom, result_left : result_right]
    #직사각형으로 나타내기
    cv2.rectangle(img, pt1=(left,top), pt2=(left+w,top+h), color=(255,255,255), thickness=3) #이미지에 사각형 그림


    cv2.imshow('result_img', result_img) 
    cv2.imshow('img',img) #윈도우에 이미지 출력
    if cv2.waitKey(1) & 0xFF ==27 :
        #waitKey(n) : 키 입력을 n밀리세컨드간 기다림
        #안쓰면 background에서 돌다가 꺼짐
        #문자 q에 해당하는 아스키 코드를 int 로 반환 : )==ord('q')
        # esc 누르면 꺼짐
        break #q 누르면 바로 break

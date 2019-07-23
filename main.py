import cv2
import numpy as np

video_path='btob.mp4'
cap=cv2.VideoCapture(video_path) #동영상 로드

if not cap.isOpened(): #동영상 제대로 로드되면 True 반환
    exit() #프로그램 종료

#첫번째 프레임 설정
ret,img=cap.read() 

cv2.namedWindow('Select Window') #이 프로그램이 이 window에서 ROI 설정 (대소문자 구분)
cv2.imshow('Select Window',img) #첫번째 프레임 보여줌

#ROI 설정
rext=cv2.selectROI('Select Window',img,fromCenter=False,showCrosshair=True)
#ROI 설정해서 rect로 반환
#ing 센터에서 시작하지말고 중심점으로 해
cv2.destroyWindow('Select Window') #ROI 선택하면 윈도우 닫아
while True:
    ret,img=cap.read() 
    #동영상 1프레임씩 읽어서 img변수에 저장 
    #비디오 끝나면 ret이 false됨

    if not ret:
        exit() #ret이 false면 종료

    cv2.imshow('img',img) #윈도우에 이미지 출력
    if cv2.waitKey(1)==ord('q'): 
        #waitKey(n) : 키 입력을 n밀리세컨드간 기다림
        #안쓰면 background에서 돌다가 꺼짐
        #문자 q에 해당하는 아스키 코드를 int 로 반환
        break #q 누르면 바로 break

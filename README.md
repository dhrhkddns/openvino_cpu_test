# openvino_cpu_test
전력상의 배터리 지속시간이 짧아서 openvino cpu로 테스트할때 저가형 노트북 60프레임 되는지 테스트

-현재 웹캠의 60프레임도 살리는게 쉽지 않다.
그 이유는 고성능 gpu를 쓸때는 초당 100프레임도 처리하지만, 문제는 그걸 구동할 배터리가 외부 전력이 없으면 1시간정도가 최대이다.

그래서 GPU의 괴물같은 배터리 소모를 대체하기 위해 CPU를 사용하려는데

저가형 CPU에서 OPENVINO를 사용하면 30FPS도 가능하다 (640,480)기준으로.

그런데 여기서 일반적인 추론 형식은 FP32인데 FP16, INT8 옵션은 정확도가 살짝 떨어지지만 사실상 공 1개를 빠르게 검출해야하는 측면에서는 검출이 문제 없을 것 같다,

추론 속도 INT8 (피시방기준 cpu fps 60정도) > FP16 > FP32(fps 30) ( (기본값)

정확도는 반대이다.

그러므로 유동적으로 openvino를 int8 옵션으로 export해서 사용하면, 같은 openvino여도 웹캠의 60FPS를 이용할수 있다. (웹캠의 속도는 코덱과 CAP.D_SHOW를 이용)


#INT8 60프레임

![INT8_60프레임](https://github.com/user-attachments/assets/72c52cc2-04a6-454d-9f21-b8bfe7bfab6a)

#FP32 30프레임(기본값)

![FP32_30프레임](https://github.com/user-attachments/assets/086af5a2-5f46-4274-942e-b311560a93c4)

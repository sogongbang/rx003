.. _technical_report_007_autonomous_driving_basic_using_ros2:


ROS2를 사용한 자율주행 기초 및 구현
****************************************************************
(title) ROS를 이용하여 자율주행로봇 구현
(subtitle) 제11회 국제e-모빌리티엑스포참여

<요약>
==========================================
ROS는 로봇 소프트웨어 개발을 위한 오픈 소스 프레임워크로, 로봇 애플리케이션을 개발, 시뮬레이션, 테스트, 배포하는데 필요한 다양한 도구와 라이브러리를 제공하며, 
특히 모듈성, 재사용성, 유연성을 강조하며, 복잡한 로봇 시스템의 구성요소를 쉽게 통합할 수 있도록 설계되었다. 
따라서 우리팀에서는 터틀봇에 ROS2 의 배포판중 하나인 foxy를 기반으로 설치를 진행하였고, 해당 프레임워크 위에서 기본적인 토픽통신과 노드에 대한 이해를 바탕으로 
gazebo등 여러 패키지들을 가져와 원격조종과 매핑작업, 내비게이션 작업 및 파라미터 변화에 따른 performance의 변화양상을 확인 및 분석하는데 초점을 두었고, 이 과정에서 
터득한 노하우를 바탕으로 “제3회 국제대학생 EV자율주행 경진대회”에 참가하였고, 여기서 얻은 피드백을 정리하였다.


<Abstract>
==========================================
ROS is an open-source framework for robot software development, providing a variety of tools and libraries necessary for developing, simulating, testing, 
and deploying robot applications. It emphasizes modularity, reusability, and flexibility, and is designed to facilitate the easy integration of components 
in complex robotic systems. Therefore, our team proceeded with the installation of ROS2 Foxy, one of the distributions, on the TurtleBot. Based on this framework, 
we focused on understanding basic topic communication and nodes, and brought in various packages such as Gazebo for remote control, mapping, navigation tasks, 
and analyzing the changes in performance with parameter variations. Using the expertise gained through this process, we participated in the "3rd International University 
EV Autonomous Driving Competition," and have compiled the feedback received from this experience.


Ⅰ. 서 론
===============================================
이 문서는 제3회 국제대학생 EV 자율주행 경진대회에 참가하기위해, ROS2와 터틀봇3 버거를 사용한 자율주행을 구현하는 과정에서 조사한 정보의 기록이다.

문서의 구조는 유사한 과정을 기록한 논문인, "ROS를 활용한 서빙 이동로봇의 구현" :cite:`EUISEONKIM2019ROS` 참조하여 구성하였다.



Ⅱ.EV자율주행경진대회 (준비단계)
===============================================

<ROS 정의> 

Robot Operating System로,  로봇  소프트웨어 개발을 위한 오픈 소스 프레임워크이다. ROS는 로봇 애플리케이션 개발의 복잡성을 줄이기 위해 다양한 라이브러리와 도구를 제공한다. 
ROS는 로봇의 하드웨어 추상화, 장치 드라이버, 라이브러리, 시뮬레이션 도구, 시각화 도구, 메시지 전달, 패키지 관리 등을 지원한다.

-ROS의 주요 구성요소

1.	Master: 각기 다른 노드들이 서로 통신할 수 있도록 관리하는 중앙서버 역할

2.	Node: 각각의 독립적인 실행단위로, 특정 기능을 수행하는 프로그램

3.	Topic: 노드 간에 메시지를 주고받는 채널, publisher와 subscriber 모델을 따름

4.	Service: 요청과 응답패턴으로 동작하는 통신방식

5.	Action: 장시간 걸리는 작업을 수행할때 사용하는 비동기 통신방식

6.	Package: 노드, 메시지, 서비스 등을 포함하는 소프트웨어 모듈

<ROS 장점>

1.	모듈성: 로봇시스템을 여러개의  독립적인 모듈로 나누어 개발할 수 있어 개발과 유지보수가 용이하다

2.	재사용성: 다양한 로봇 프로젝트에서 이미 개발된 코드를 재사용할 수 있어 개발시간을 단축할 수 있다.

3.	유연성: 서로 다른 하드웨어와 소프트웨어 구성요소를 통합하는데 유연하게 대처할 수 있다.

4.	커뮤니티 지원: 광범위한 오픈소스 커뮤니티의 지원을 받아 많은 리소스와 도움을 얻을 수 있다.

5.	다양한 도구: 시뮬레이션 시각화, 디버깅 등의 다양한 도구가 제공되어 개발 효율성을 높일 수 있다.

6.	분산 처리: 여러 노드가 분산되어 작업을 처리할 수 있어 성능과 확장성이 뛰어나다

7.	표준화된 인터페이스: ROS는 로봇 시스템의 표준화된 인터페이스를 제공하여 다른 로봇 및 소프트웨어와의 호환성을 높인다.


<실제 ROS가 쓰이는 예시들>

1. 자율 주행 : ROS는 자율 주행 차량의 센서 데이터 처리, 경로 계획, 차량 제어 등을 위해 사용된다.

2. 드론 : 드론의 비행 제어, 경로 계획, 영상 처리 등에 ROS를 사용하여 효율적인 개발이 가능하다.

3. 산업용 로봇 : 제조 공장에서 사용되는 로봇 팔 등의 제어를 위해 ROS가 사용된다. 





2.2 ROS 설치
-----------------------
 ROS를 설치하기 위해 우분투 환경이 설정되어야 한다. 먼저 사용하려는 ROS 버전과 그에 맞는 우분투 버전을 파악하고 사용하려는 PC에 우분투를 설치한다. 
 그 다음 ROS 설치를 위한 명령어들을 터미널에 차례로 입력하면 설치가 완료된다.
 터틀봇에도 PC에 설치된 버전과 통일하여 설치하면 되는데, 공식 홈페이지에 올라와 있는 통합 파일을 이용하면 더 편리하게 설치할 수 있다.






2.3 터틀봇 패키지 설치
-----------------------
사용해야 할 패키지 :
Teleop : 키보드를 통해 터틀봇을 수동으로 조작한다
Slam : 라이다를 통해 주변 환경을 mapping 한다.
Navigtion : mapping된 파일과 navigation 알고리즘을 통해 출발지에서 목적지까지 주행한다.
Bringup : 로봇의 하드웨어와 소프트웨어를 초기화하고 시작하는 역할이다. (다양한 노드 실행, 센서 데이터 수집, 명령 전달 등)






Ⅲ.자율주행 구현을 위한 터틀봇 구현(연구단계)
===============================================
3.1 경기장 제작(시뮬레이터->실제구현)
-----------------------------------------------------
2024년 04월 01일 ~ 04월 05일 동안 제주 국제 컨벤션센터에서 개최되었던  2024 제3회 국제대학생 EV 자율주행 경진대회 1/10스케일 (Turtlebot3 Burger) 사전 교육을 실시했었습니다.
 


-Construct를 이용한 터틀봇 시뮬레이터 구현

.. _figure_006_01_temp:

.. figure:: /_static/image/ioconstruct.png
    :width: 90%
    :align: center
    :alt: ioconstruct

    ioconstruct

-트랙개발- Gazebo 시뮬레이터로 구현


.. _figure_006_02_temp:

.. figure:: /_static/image/gazebo_simulator.png
    :width: 90%
    :align: center
    :alt: Gazebo simulator

    Gazebo simulator

-시뮬레이터로는 실제 결과를 예상할 수 없을 것이라고 판단하여 실물크기의 경기장을 직접 제작하기로 함


.. _figure_006_03_temp:

.. figure:: /_static/image/track1.png
    :width: 90%
    :align: center
    :alt: track1

    track1



.. _figure_006_04_temp:

.. figure:: /_static/image/track2.png
    :width: 90%
    :align: center
    :alt: track2

    track2

-경기장 예시 사진

.. _figure_006_05_temp:

.. figure:: /_static/image/blueprint1.png
    :width: 90%
    :align: center
    :alt: blueprint1

    blueprint1

-경기 하루 전날 실제 도면 제시

.. _figure_006_06_temp:

.. figure:: /_static/image/blueprint2.png
    :width: 90%
    :align: center
    :alt: blueprint2

    blueprint2

3.2 자율주행 구동(맵핑)
----------------------------
<제약>

참가팀 전부 Navigation을 사용하여, Rviz 상에서 출발지점과 도착지점을 설정하여 네비게이션하는 방식으로 경기에 참가

<미션>

동적/정적장애물 피해서 목적지까지 주행한다.

-mapping완료 후 navigation 실행 화면

.. _figure_006_07_temp:

.. figure:: /_static/image/navigation.png
    :width: 90%
    :align: center
    :alt: navigation

    navigation








<mapping 중 발생한 문제점>

로봇을 너무 빨리 움직였을 경우 map이 정확히 그려지지 않는 경우가 많았다. 벽을 정확히 그리지 않아서 틈이 생기거나, 벽으로 그려진 곳으로부터 멀어지면서 되려 벽이 사라지는 등 
로봇을 어떻게 조작하느냐에 따라 map의 정확도가 달라졌다. 
맵핑시 발생했던 문제점(틈까지 완벽하게 따지지 않아서 자율주행 시 지도를 엉뚱하게 그려 우회해서 가는 경우)



3.3  파라미터 분석(디버깅)
----------------------------
저장된 지도에 기반하여 Navigation을 할 때, 여러 가지 파라미터 값을 변경하여 변화를 줄 수 있다. 다음은 올바른 Navigation Tuning을 위해 주로 변경한 파라미터들이다.

1. inflation_radius : 장애물 근처에서 cost를 증가시키는 영역의 반경을 정의합니다. 이 영역 내의 셀은 장애물에 가까울수록 더 높은 cost를 가지게 됩니다. 
이는 로봇이 장애물을 안전하게 피하도록 합니다.

2. cost_scaling_factor : 장애물 근처에서 cost가 증가하는 속도를 결정합니다. 값이 높을수록 cost가 빠르게 증가하며, 이는 로봇이 장애물에 더 멀리 떨어져 있도록 합니다.

3. sim_time : 로컬 플래너가 시뮬레이션하는 시간의 길이를 정의합니다. 시뮬레이션 시간 동안 로봇의 가능한 경로를 탐색합니다. 더 긴 시간은 더 많은 경로를 고려하지만 계산 cost가 증가할 수 있습니다.

4. xy_goal_tolerance : 목표 지점에서 허용되는 최대 위치 오차를 정의합니다. 이 값 이내에 도달하면 로봇은 목표에 도달한 것으로 간주합니다.

5. robot_radius : 로봇의 반경을 정의합니다. 이는 로봇이 장애물과의 충돌을 피하기 위해 필요한 최소 거리 계산에 사용됩니다.





Ⅳ.결론 및 향후 과제
===============================================
실제 대회를 진행하면서 두 가지 큰 문제가 발생했다. 

1. 라이다 영점 문제
2. 네트워크 오류 문제

라이다 영점 문제는 기존에 테스트를 진행할 때는 한번도 발생하지 않은 문제였다. navigation을 실행했을 때 라이다 센서가 읽는 값들이 전체적으로 계속 회전하는 증상이 발생했다. 
실행 파일을 종료 후 다시 실행 하거나 터틀봇 및 PC를 재부팅하면 일시적으로 해결이 되었으나 종종 안되는 경우도 많았다. 

 네트워크 오류의 경우, PC와 터틀봇의 연결 환경에 따라 실행 파일이 정상적으로 동작하거나, 오류가 발생해 종료되는 등의 네트워크 환경의 영향을 크게 받은 것으로 추측된다. 
 연습 기간 동안 휴대폰의 핫스팟을 이용하여 연습했고 이 과정에서는 매우 가끔 발생하는 오류를 제외하고는 문제 없이 동작하였지만, 대회 장소에서는 이 오류의 빈도가 상당히 높아졌으며 
 마땅한 해결책이 없었기에 PC와 터틀봇을 계속 재부팅하는 과정을 통해 상황을 모면했다. 노트북 핫스팟을 경유하여 하는 방식도 사용했으나 증상은 크게 개선되지 않았다. 

라이다 영점 문제가 네트워크 문제와 연관성이 있는 지는 확실하지 않으며 더 알아보아야 할 문제이다. 또한 PC와 터틀봇의 연결을 위한 안정적인 네트워크 환경을 구축하기 위한 조건도 더 분석해볼 필요가 있다. 


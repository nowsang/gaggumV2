## README
# 가꿈 - 스마트홈 IoT 프로젝트

## 🌳 프로젝트 주소 : https://k8b101.p.ssafy.io

---

## 🌳 소개 영상 보기 : [Youtube URL](https://youtu.be/X2S5y5FsOjA)

---

## 🌳 프로젝트 진행 기간

---

2023.04.10 ~ 2023.05.19 (총 6주)

SSAFY 8기 자율 프로젝트

## 🌳 팀원 및 역할

---

![자율 프로젝트 팀원](https://github.com/Hyokiz/Algorithm/assets/109258146/0894ddd6-7ee5-47d0-9f41-ddda97c38065)

## 🌳 프로젝트 개요

---

최근 1인 가구에서 반려식물이 인기를 끌고 있습니다. 그러나 식물은 우리가 생각하는 것보다 매우 민감한 생명체입니다. 적절한 수분과 영양분을 공급받지 못하면 쉽게 질병에 걸리거나 죽을 수 있습니다. 하지만 바쁜 직장인들에게는 식물을 관리할 시간이 부족해서 식물을 키우는 데 실패하는 경우가 있습니다. 이러한 배경을 바탕으로 저희는 식물 자동 관리 서비스, 가꿈을 제작하게 되었습니다.

특화 프로젝트와 다르게 시뮬레이터에서 터틀봇을 조종하는 것이 아닌, 실제 환경에서 터틀봇을 조종하는 방식을 선택하였습니다. 따라서 Front, Back, ROS로 이루어졌던 전 프로젝트에서 Hardware부분이 추가되었습니다. Front-end는 특화 프로젝트에서는 React를 활용한 웹 앱 어플리케이션을 개발하였으나, 본 프로젝트에서는 Kotlin을 활용한 Android App을 개발하였습니다. ROS는 기존의 Python 코드에, C++코드를 추가하였습니다.



## 🌳 주요 기능

---

### 집안 내부 탐색을 통한 맵 정보 저장

### 물이 필요한 식물들의 급수 주기를 파악하여 필요한 양만큼 자동 급수

### 정해진 시간에 햇빛이 필요한 식물을 햇빛이 잘 드는 곳으로 이동

---

- 라이더 센서를 이용한 장애물 인식
- A* 알고리즘을 통한 최적 경로 계산(Path Tracking)
- YOLO모델을 사용해서 화분 객체 탐지
- 탐지된 화분 좌표 추정 알고리즘 개발


## 🌳 기술 스택

---

### Front

- Node v18.15.0
- React v18.2.0
- Kotlin v1.8.0
- Android Studio Flamingo
- Firebase 인증
- Kotlin Socket.io-client v1.0.1
- APIs
  - OpenWeather API v2.5
  - 오늘의 꽃 추천 API v2.0

### Back

- Node v18.15.0
- Socket.io v4.6.1
- Express.js v4.18.2

### ROS

- Python v3.8.10
- Python-Socket.io v5.8.0
- C++ 14
- ROS2-eloquent(release 2020.01.24)
- opencv-contrib-python 4.5.3.56
- opencv-python 4.5.3.56
- openssl 1.0.2u
- choco 0.10.15
- rti 5.3.1
- openslice 6.9.190403
```
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DOMAIN_ID=35
AMENT_PREFIX_PATH=/opt/ros/foxy
PYTHONPATH=/opt/ros/foxy/lib/python3.8/site-packages
LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/gazebo-11/plugins:/opt/ros/foxy/opt/yaml_cpp_vendor/lib:/opt/ros/foxy/opt/rviz_ogre_vendor/lib:/opt/ros/foxy/lib/x86_64-linux-gnu:/opt/ros/foxy/lib
ROS_LOCALHOST_ONLY=0
PATH=/opt/ros/foxy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
ROS_DISTRO=foxy
```

### ROS GPU Setting
- CUDA Toolkit 11.2.2(March 2021)
- cuDNN v8.1.0 (January 26th, 2021) for CUDA 11.0, 11.1 and 11.2

### ROS Pytorch
- torch 1.8.1 + cu111
- torchaudio 0.8.1
- torchvision 0.9.1 + cu111

### ROS YOLO
- numpy 1.21.1
- Pillow 9.4.0
- pandas 1.3.5
- setuptools 67.6.0
- seaborn 0.12.2

### Hardware

- Turtlebot3 Burger
- 라즈베리파이 4
- OpenCR
- micro-ros v2.0.5
- mighty zap 액추에이터 12Lf Series
- HC-SR04 초음파센서
- arduino 물펌프

### DB

- Amazon S3
- MySQL

### CI/CD

- Docker
- Jenkins
- NGINX

## 🌳 산출물

---

### 요구사항 명세서

[요구사항 명세서](https://j8b310.notion.site/d2753cc1f7f24088b8c5f95de22ea3ad)

### ERD

[ERD](https://j8b310.notion.site/ERD-728e8a011e6f484ebb16bda811a0d08f)

### API 명세서

[API 명세서](https://j8b310.notion.site/API-aeaeb98744db4d208244063fe19c2048)

### 와이어 프레임

[와이어 프레임](https://www.figma.com/file/bJj1vEB1RWQ0dVShCkFPyV/B310?type=design&node-id=0%3A1&t=HWiQ3QhB2ZPzUQ2A-1)

### 포팅 매뉴얼

[포팅 매뉴얼](https://j8b310.notion.site/496da9e887314449b8297402baf4b360)

## 🌳 프로젝트 파일 구조

---

### Front

```
📦front
 ┣ 📂.gradle
 ┣ 📂app
 ┃ ┣ 📂build
 ┃ ┣ 📂sampledata
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂main
 ┃ ┃ ┃ ┣ 📂java
 ┃ ┃ ┃ ┃ ┗ 📂com
 ┃ ┃ ┃ ┃ ┃ ┗ 📂gaggum
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜CameraActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜DiaryAdapter.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜DiaryFragment.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜FlowerClient.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ImagePreviewActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜JoinActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜KeyCertificationActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LocationProvider.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜MainActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜MainFragment.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜MapScanActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜MyPlantFragment.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜MyPlantRVAdapter.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜PlantDetailActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜RegisterFragment.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜RetrofitDto.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜RetrofitObject.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜RetrofitService.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜RVAdapter.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SigninActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜SplashActivity.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜UserRoom.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ViewPagerAdapter.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜ViewPagerDTO.kt
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WeatherClient.kt
 ┃ ┃ ┃ ┣ 📂res
 ┃ ┃ ┃ ┃ ┣ 📂anim
 ┃ ┃ ┃ ┃ ┃ ┣ 📜slide_in_up.xml
 ┃ ┃ ┃ ┃ ┃ ┗ 📜slide_out_down.xml
 ┃ ┃ ┃ ┃ ┣ 📂drawable
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arrow_down.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arrow_left.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arrow_right.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜arrow_up.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜diary_button.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ic_launcher_background.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜kakao_login_medium_wide.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜maskable_icon_x192_logo.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜modal_background.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_diary.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_home.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_my_plant.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜nav_register.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜photo1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜photo2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜photo3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜plans_blueprint.gif
 ┃ ┃ ┃ ┃ ┃ ┣ 📜radius_button.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜radius_flowermean.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜radius_flowername.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜radius_image.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜robot.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜start_background_tulip.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sun_0.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sun_1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜textview_rounded.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜view_round_bottom.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜view_round_top.xml
 ┃ ┃ ┃ ┃ ┃ ┗ 📜view_round_white.xml
 ┃ ┃ ┃ ┃ ┣ 📂drawable-v24
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ic_launcher_foreground.xml
 ┃ ┃ ┃ ┃ ┣ 📂font
 ┃ ┃ ┃ ┃ ┃ ┣ 📜bmjua_ttf.ttf
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fa_solid_900.ttf
 ┃ ┃ ┃ ┃ ┃ ┗ 📜font_awesome.xml
 ┃ ┃ ┃ ┃ ┣ 📂layout
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_camera.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_image_preview.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_join.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_key_certification.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_main.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_map_scan.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_plant_detail.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_signin.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜activity_splash.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dialog_bottom.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜diary_detail_modal.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜diary_item.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fragment_diary.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fragment_main.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fragment_my_plant.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fragment_register.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pv_item.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rv_item.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rv_item_my_plant.xml
 ┃ ┃ ┃ ┃ ┃ ┗ 📜year_month_picker_dialog.xml
 ┃ ┃ ┃ ┃ ┣ 📂menu
 ┃ ┃ ┃ ┃ ┃ ┗ 📜nav_menu.xml
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-anydpi-v26
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-anydpi-v33
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-hdpi
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-mdpi
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-xhdpi
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-xxhdpi
 ┃ ┃ ┃ ┃ ┣ 📂mipmap-xxxhdpi
 ┃ ┃ ┃ ┃ ┣ 📂navigation
 ┃ ┃ ┃ ┃ ┃ ┗ 📜nav_graph.xml
 ┃ ┃ ┃ ┃ ┣ 📂values
 ┃ ┃ ┃ ┃ ┃ ┣ 📜colors.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dimens.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜ic_launcher_background.xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜strings.xml
 ┃ ┃ ┃ ┃ ┃ ┗ 📜themes.xml
 ┃ ┃ ┃ ┃ ┣ 📂values-night
 ┃ ┃ ┃ ┃ ┃ ┗ 📜themes.xml
 ┃ ┃ ┃ ┃ ┗ 📂xml
 ┃ ┃ ┃ ┃ ┃ ┣ 📜backup_rules.xml
 ┃ ┃ ┃ ┃ ┃ ┗ 📜data_extraction_rules.xml
 ┃ ┃ ┃ ┣ 📜AndroidManifest.xml
 ┃ ┃ ┃ ┗ 📜ic_launcher-playstore.png
 ┃ ┃ ┗ 📂test
 ┃ ┃ ┃ ┗ 📂java
 ┃ ┃ ┃ ┃ ┗ 📂com
 ┃ ┃ ┃ ┃ ┃ ┗ 📂gaggum
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜ExampleUnitTest.kt
 ┃ ┣ 📜.gitignore
 ┃ ┣ 📜build.gradle
 ┃ ┣ 📜google-services.json
 ┃ ┗ 📜proguard-rules.pro
 ┣ 📂build
 ┃ ┗ 📂kotlin
 ┃ ┃ ┗ 📂sessions
 ┣ 📂gradle
 ┃ ┗ 📂wrapper
 ┃ ┃ ┣ 📜gradle-wrapper.jar
 ┃ ┃ ┗ 📜gradle-wrapper.properties
 ┣ 📜.gitignore
 ┣ 📜build.gradle
 ┣ 📜gradle.properties
 ┣ 📜gradlew
 ┣ 📜gradlew.bat
 ┣ 📜local.properties
 ┗ 📜settings.gradle
```

### Back

```
📦back
 ┣ 📂aws
 ┃ ┗ 📜s3.js
 ┣ 📂routes
 ┃ ┣ 📜diary.js
 ┃ ┣ 📜plant.js
 ┃ ┗ 📜turtle.js
 ┣ 📂servies
 ┃ ┣ 📜db.js
 ┃ ┣ 📜diary.js
 ┃ ┣ 📜plant.js
 ┃ ┗ 📜turtle.js
 ┣ 📂socket
 ┃ ┗ 📜socket.js
 ┣ 📜.dockerignore
 ┣ 📜.gitignore
 ┣ 📜app.js
 ┣ 📜dockerfile
 ┣ 📜helper.js
 ┣ 📜package-lock.json
 ┗ 📜package.json
```

### ROS2

```
📦src
 ┣ 📂gaggum
 ┃ ┣ 📂map
 ┃ ┃ ┗ 📜map.txt
 ┃ ┣ 📂nodes
 ┃ ┃ ┣ 📜gaggum_socket.cpp
 ┃ ┃ ┣ 📜time_13.cpp
 ┃ ┃ ┗ 📜time_15.cpp
 ┃ ┣ 📜CMakeLists.txt
 ┃ ┗ 📜package.xml
 ┣ 📂gaggum_msgs
 ┃ ┣ 📂msg
 ┃ ┃ ┣ 📜Detection.msg
 ┃ ┃ ┣ 📜MapScan.msg
 ┃ ┃ ┣ 📜SunPlantInfo.msg
 ┃ ┃ ┗ 📜WaterPlantInfo.msg
 ┃ ┣ 📜CMakeLists.txt
 ┃ ┗ 📜package.xml
 ┣ 📂gaggum_python
 ┃ ┣ 📂gaggum_python
 ┃ ┃ ┣ 📂model_weights
 ┃ ┃ ┃ ┣ 📜gaggum_weight_turtle_final.pt
 ┃ ┃ ┃ ┣ 📜gaggum_weight_turtle_final_1.pt
 ┃ ┃ ┃ ┣ 📜gaggum_weight_turtle_final_2.pt
 ┃ ┃ ┃ ┣ 📜gaggum_weight_turtle_final_3.pt
 ┃ ┃ ┃ ┗ 📜gaggum_weight_turtle_final_4.pt
 ┃ ┃ ┣ 📜a_star.py
 ┃ ┃ ┣ 📜a_star_local_path.py
 ┃ ┃ ┣ 📜image_capture.py
 ┃ ┃ ┣ 📜load_map.py
 ┃ ┃ ┣ 📜move_sun.py
 ┃ ┃ ┣ 📜navigation.py
 ┃ ┃ ┣ 📜odom.py
 ┃ ┃ ┣ 📜odom_reset.py
 ┃ ┃ ┣ 📜path_tracking.py
 ┃ ┃ ┣ 📜run_mapping.py
 ┃ ┃ ┣ 📜scan_read.py
 ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┣ 📜wall_tracking.py
 ┃ ┃ ┣ 📜water.py
 ┃ ┃ ┣ 📜yolov5.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂map
 ┃ ┃ ┗ 📜map.txt
 ┃ ┣ 📂resource
 ┃ ┃ ┗ 📜gaggum_python
 ┃ ┣ 📂test
 ┃ ┃ ┣ 📜test_copyright.py
 ┃ ┃ ┣ 📜test_flake8.py
 ┃ ┃ ┗ 📜test_pep257.py
 ┃ ┣ 📜package.xml
 ┃ ┣ 📜setup.cfg
 ┃ ┗ 📜setup.py
 ┣ 📂navigation2
 ┃ ┣ 📂.circleci
 ┃ ┃ ┗ 📜config.yml
 ┃ ┣ 📂.dockerhub
 ┃ ┃ ┣ 📂debug
 ┃ ┃ ┃ ┣ 📜Dockerfile
 ┃ ┃ ┃ ┗ 📜dummy.Dockerfile
 ┃ ┃ ┣ 📂devel
 ┃ ┃ ┃ ┗ 📜Dockerfile
 ┃ ┃ ┗ 📂release
 ┃ ┃ ┃ ┣ 📜Dockerfile
 ┃ ┃ ┃ ┗ 📜dummy.Dockerfile
 ┃ ┣ 📂.github
 ┃ ┃ ┣ 📜ISSUE_TEMPLATE.md
 ┃ ┃ ┗ 📜PULL_REQUEST_TEMPLATE.md
 ┃ ┣ 📂doc
 ┃ ┃ ┣ 📂architecture
 ┃ ┃ ┃ ┗ 📜Navigation-System.eap
 ┃ ┃ ┣ 📂design
 ┃ ┃ ┃ ┣ 📜NavigationSystemTasks.png
 ┃ ┃ ┃ ┗ 📜Navigation_2_Overview.pdf
 ┃ ┃ ┣ 📂parameters
 ┃ ┃ ┃ ┗ 📜param_list.md
 ┃ ┃ ┣ 📂process
 ┃ ┃ ┃ ┗ 📜PreReleaseChecklist.md
 ┃ ┃ ┣ 📂requirements
 ┃ ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┃ ┣ 📜Command-Pipeline-Support.png
 ┃ ┃ ┃ ┃ ┣ 📜Command-Pipeline.png
 ┃ ┃ ┃ ┃ ┣ 📜Command-Pipeline.vsdx
 ┃ ┃ ┃ ┃ ┣ 📜Context.png
 ┃ ┃ ┃ ┃ ┣ 📜Mapping-Use-Cases.png
 ┃ ┃ ┃ ┃ ┣ 📜Mission-Execution-Use-Cases.png
 ┃ ┃ ┃ ┃ ┣ 📜Mission-Planning-Use-Cases.png
 ┃ ┃ ┃ ┃ ┣ 📜Navigation-System.png
 ┃ ┃ ┃ ┃ ┗ 📜With-Support-Modules.png
 ┃ ┃ ┃ ┣ 📜requirements.md
 ┃ ┃ ┃ ┗ 📜_template_requirement.md
 ┃ ┃ ┣ 📂use_cases
 ┃ ┃ ┃ ┣ 📜collision_avoidance_use_case.md
 ┃ ┃ ┃ ┣ 📜indoor_localization_use_case.md
 ┃ ┃ ┃ ┣ 📜indoor_navigation_use_case.md
 ┃ ┃ ┃ ┣ 📜keep_out_zones_use_case.md
 ┃ ┃ ┃ ┣ 📜multi-story-building_use_case.md
 ┃ ┃ ┃ ┣ 📜outdoor_localization_use_case.md
 ┃ ┃ ┃ ┣ 📜outdoor_navigation_use_case.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜_template_use_case.md
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_amcl
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_amcl
 ┃ ┃ ┃ ┃ ┣ 📂map
 ┃ ┃ ┃ ┃ ┃ ┗ 📜map.hpp
 ┃ ┃ ┃ ┃ ┣ 📂motion_model
 ┃ ┃ ┃ ┃ ┃ ┗ 📜motion_model.hpp
 ┃ ┃ ┃ ┃ ┣ 📂pf
 ┃ ┃ ┃ ┃ ┃ ┣ 📜eig3.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pf.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pf_kdtree.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pf_pdf.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜pf_vector.hpp
 ┃ ┃ ┃ ┃ ┣ 📂sensors
 ┃ ┃ ┃ ┃ ┃ ┗ 📂laser
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜laser.hpp
 ┃ ┃ ┃ ┃ ┣ 📜amcl_node.hpp
 ┃ ┃ ┃ ┃ ┗ 📜angleutils.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┃ ┗ 📜portable_utils.h
 ┃ ┃ ┃ ┣ 📂map
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜map.c
 ┃ ┃ ┃ ┃ ┣ 📜map_cspace.cpp
 ┃ ┃ ┃ ┃ ┣ 📜map_draw.c
 ┃ ┃ ┃ ┃ ┣ 📜map_range.c
 ┃ ┃ ┃ ┃ ┗ 📜map_store.c
 ┃ ┃ ┃ ┣ 📂motion_model
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜differential_motion_model.cpp
 ┃ ┃ ┃ ┃ ┣ 📜motion_model.cpp
 ┃ ┃ ┃ ┃ ┗ 📜omni_motion_model.cpp
 ┃ ┃ ┃ ┣ 📂pf
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜eig3.c
 ┃ ┃ ┃ ┃ ┣ 📜pf.c
 ┃ ┃ ┃ ┃ ┣ 📜pf_draw.c
 ┃ ┃ ┃ ┃ ┣ 📜pf_kdtree.c
 ┃ ┃ ┃ ┃ ┣ 📜pf_pdf.c
 ┃ ┃ ┃ ┃ ┗ 📜pf_vector.c
 ┃ ┃ ┃ ┣ 📂sensors
 ┃ ┃ ┃ ┃ ┣ 📂laser
 ┃ ┃ ┃ ┃ ┃ ┣ 📜beam_model.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜laser.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜likelihood_field_model.cpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜likelihood_field_model_prob.cpp
 ┃ ┃ ┃ ┃ ┗ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜amcl_node.cpp
 ┃ ┃ ┃ ┗ 📜main.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_behavior_tree
 ┃ ┃ ┣ 📂doc
 ┃ ┃ ┃ ┣ 📜hierarchy.odg
 ┃ ┃ ┃ ┗ 📜hierarchy.svg
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_behavior_tree
 ┃ ┃ ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┃ ┃ ┣ 📂action
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜back_up_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜clear_costmap_service.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compute_path_to_pose_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜follow_path_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜navigate_to_pose_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜reinitialize_global_localization_service.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜spin_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜truncate_path_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wait_action.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📂condition
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜distance_traveled_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜goal_reached_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜goal_updated_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜initial_pose_received_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜is_battery_low_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜is_stuck_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜time_expired_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜transform_available_condition.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📂control
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pipeline_sequence.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜recovery_node.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜round_robin_node.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📂decorator
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜distance_controller.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜goal_updater_node.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜rate_controller.hpp
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜speed_controller.hpp
 ┃ ┃ ┃ ┃ ┣ 📜behavior_tree_engine.hpp
 ┃ ┃ ┃ ┃ ┣ 📜bt_action_node.hpp
 ┃ ┃ ┃ ┃ ┣ 📜bt_conversions.hpp
 ┃ ┃ ┃ ┃ ┗ 📜bt_service_node.hpp
 ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┣ 📂action
 ┃ ┃ ┃ ┃ ┣ 📜back_up_action.cpp
 ┃ ┃ ┃ ┃ ┣ 📜clear_costmap_service.cpp
 ┃ ┃ ┃ ┃ ┣ 📜compute_path_to_pose_action.cpp
 ┃ ┃ ┃ ┃ ┣ 📜follow_path_action.cpp
 ┃ ┃ ┃ ┃ ┣ 📜navigate_to_pose_action.cpp
 ┃ ┃ ┃ ┃ ┣ 📜reinitialize_global_localization_service.cpp
 ┃ ┃ ┃ ┃ ┣ 📜spin_action.cpp
 ┃ ┃ ┃ ┃ ┣ 📜truncate_path_action.cpp
 ┃ ┃ ┃ ┃ ┗ 📜wait_action.cpp
 ┃ ┃ ┃ ┣ 📂condition
 ┃ ┃ ┃ ┃ ┣ 📜distance_traveled_condition.cpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_reached_condition.cpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_updated_condition.cpp
 ┃ ┃ ┃ ┃ ┣ 📜initial_pose_received_condition.cpp
 ┃ ┃ ┃ ┃ ┣ 📜is_battery_low_condition.cpp
 ┃ ┃ ┃ ┃ ┣ 📜is_stuck_condition.cpp
 ┃ ┃ ┃ ┃ ┣ 📜time_expired_condition.cpp
 ┃ ┃ ┃ ┃ ┗ 📜transform_available_condition.cpp
 ┃ ┃ ┃ ┣ 📂control
 ┃ ┃ ┃ ┃ ┣ 📜pipeline_sequence.cpp
 ┃ ┃ ┃ ┃ ┣ 📜recovery_node.cpp
 ┃ ┃ ┃ ┃ ┗ 📜round_robin_node.cpp
 ┃ ┃ ┃ ┗ 📂decorator
 ┃ ┃ ┃ ┃ ┣ 📜distance_controller.cpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_updater_node.cpp
 ┃ ┃ ┃ ┃ ┣ 📜rate_controller.cpp
 ┃ ┃ ┃ ┃ ┗ 📜speed_controller.cpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┗ 📜behavior_tree_engine.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┃ ┣ 📂action
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_back_up_action.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_clear_costmap_service.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_compute_path_to_pose_action.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_follow_path_action.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_navigate_to_pose_action.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_reinitialize_global_localization_service.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_spin_action.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_truncate_path_action.cpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_wait_action.cpp
 ┃ ┃ ┃ ┃ ┣ 📂condition
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_distance_traveled.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_goal_reached.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_goal_updated.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_initial_pose_received.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_is_battery_low.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_is_stuck.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_time_expired.cpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_transform_available.cpp
 ┃ ┃ ┃ ┃ ┣ 📂control
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_pipeline_sequence.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_recovery_node.cpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_round_robin_node.cpp
 ┃ ┃ ┃ ┃ ┗ 📂decorator
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_distance_controller.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_goal_updater_node.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_rate_controller.cpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_speed_controller.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜test_action_server.hpp
 ┃ ┃ ┃ ┣ 📜test_behavior_tree_fixture.hpp
 ┃ ┃ ┃ ┣ 📜test_bt_conversions.cpp
 ┃ ┃ ┃ ┣ 📜test_dummy_tree_node.hpp
 ┃ ┃ ┃ ┣ 📜test_service.hpp
 ┃ ┃ ┃ ┗ 📜test_transform_handler.hpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜groot_instructions.md
 ┃ ┃ ┣ 📜nav2_tree_nodes.xml
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_bringup
 ┃ ┃ ┣ 📂bringup
 ┃ ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┃ ┣ 📜bringup_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜localization_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜multi_tb3_simulation_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜navigation_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜rviz_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜slam_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜spawn_tb3_launch.py
 ┃ ┃ ┃ ┃ ┗ 📜tb3_simulation_launch.py
 ┃ ┃ ┃ ┣ 📂maps
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_world.pgm
 ┃ ┃ ┃ ┃ ┗ 📜turtlebot3_world.yaml
 ┃ ┃ ┃ ┣ 📂params
 ┃ ┃ ┃ ┃ ┣ 📜nav2_multirobot_params_1.yaml
 ┃ ┃ ┃ ┃ ┣ 📜nav2_multirobot_params_2.yaml
 ┃ ┃ ┃ ┃ ┗ 📜nav2_params.yaml
 ┃ ┃ ┃ ┣ 📂rviz
 ┃ ┃ ┃ ┃ ┣ 📜nav2_default_view.rviz
 ┃ ┃ ┃ ┃ ┗ 📜nav2_namespaced_view.rviz
 ┃ ┃ ┃ ┣ 📂urdf
 ┃ ┃ ┃ ┃ ┗ 📜turtlebot3_waffle.urdf
 ┃ ┃ ┃ ┣ 📂worlds
 ┃ ┃ ┃ ┃ ┣ 📜waffle.model
 ┃ ┃ ┃ ┃ ┗ 📜world_only.model
 ┃ ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┃ ┗ 📜README.md
 ┃ ┃ ┗ 📂nav2_gazebo_spawner
 ┃ ┃ ┃ ┣ 📂nav2_gazebo_spawner
 ┃ ┃ ┃ ┃ ┣ 📜nav2_gazebo_spawner.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂resource
 ┃ ┃ ┃ ┃ ┗ 📜nav2_gazebo_spawner
 ┃ ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┃ ┣ 📜setup.cfg
 ┃ ┃ ┃ ┗ 📜setup.py
 ┃ ┣ 📂nav2_bt_navigator
 ┃ ┃ ┣ 📂behavior_trees
 ┃ ┃ ┃ ┣ 📜follow_point.xml
 ┃ ┃ ┃ ┣ 📜navigate_w_replanning_and_recovery.xml
 ┃ ┃ ┃ ┣ 📜navigate_w_replanning_and_round_robin_recovery.xml
 ┃ ┃ ┃ ┣ 📜navigate_w_replanning_distance.xml
 ┃ ┃ ┃ ┣ 📜navigate_w_replanning_speed.xml
 ┃ ┃ ┃ ┗ 📜navigate_w_replanning_time.xml
 ┃ ┃ ┣ 📂doc
 ┃ ┃ ┃ ┣ 📜AutoLocalization_w_recovery_parallel.png
 ┃ ┃ ┃ ┣ 📜auto_localization.png
 ┃ ┃ ┃ ┣ 📜follow_point.png
 ┃ ┃ ┃ ┣ 📜legend.png
 ┃ ┃ ┃ ┣ 📜navigate_w_replanning_distance.png
 ┃ ┃ ┃ ┣ 📜navigate_w_replanning_time.png
 ┃ ┃ ┃ ┣ 📜parallel_w_recovery.png
 ┃ ┃ ┃ ┣ 📜parallel_w_round_robin_recovery.png
 ┃ ┃ ┃ ┣ 📜proposed_recovery.png
 ┃ ┃ ┃ ┣ 📜recovery_node.png
 ┃ ┃ ┃ ┗ 📜recovery_w_goal_updated.png
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_bt_navigator
 ┃ ┃ ┃ ┃ ┣ 📜bt_navigator.hpp
 ┃ ┃ ┃ ┃ ┗ 📜ros_topic_logger.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜bt_navigator.cpp
 ┃ ┃ ┃ ┣ 📜main.cpp
 ┃ ┃ ┃ ┗ 📜ros_topic_logger.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_common
 ┃ ┃ ┣ 📂cmake
 ┃ ┃ ┃ ┗ 📜nav2_package.cmake
 ┃ ┃ ┣ 📂nav2_common
 ┃ ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┃ ┣ 📜has_node_params.py
 ┃ ┃ ┃ ┃ ┣ 📜replace_string.py
 ┃ ┃ ┃ ┃ ┣ 📜rewritten_yaml.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜nav2_common-extras.cmake
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂nav2_controller
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_controller
 ┃ ┃ ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┃ ┃ ┣ 📜simple_goal_checker.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜simple_progress_checker.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜stopped_goal_checker.hpp
 ┃ ┃ ┃ ┃ ┗ 📜nav2_controller.hpp
 ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜goal_checker.cpp
 ┃ ┃ ┃ ┃ ┗ 📜progress_checker.cpp
 ┃ ┃ ┃ ┣ 📜simple_goal_checker.cpp
 ┃ ┃ ┃ ┣ 📜simple_progress_checker.cpp
 ┃ ┃ ┃ ┗ 📜stopped_goal_checker.cpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜main.cpp
 ┃ ┃ ┃ ┗ 📜nav2_controller.cpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┣ 📜plugins.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_core
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_core
 ┃ ┃ ┃ ┃ ┣ 📜controller.hpp
 ┃ ┃ ┃ ┃ ┣ 📜exceptions.hpp
 ┃ ┃ ┃ ┃ ┣ 📜global_planner.hpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_checker.hpp
 ┃ ┃ ┃ ┃ ┣ 📜progress_checker.hpp
 ┃ ┃ ┃ ┃ ┗ 📜recovery.hpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_costmap_2d
 ┃ ┃ ┣ 📂cfg
 ┃ ┃ ┃ ┣ 📜Costmap2D.cfg
 ┃ ┃ ┃ ┣ 📜GenericPlugin.cfg
 ┃ ┃ ┃ ┣ 📜InflationPlugin.cfg
 ┃ ┃ ┃ ┣ 📜ObstaclePlugin.cfg
 ┃ ┃ ┃ ┗ 📜VoxelPlugin.cfg
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_costmap_2d
 ┃ ┃ ┃ ┃ ┣ 📜array_parser.hpp
 ┃ ┃ ┃ ┃ ┣ 📜clear_costmap_service.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_2d.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_2d_publisher.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_2d_ros.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_layer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_math.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_subscriber.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_topic_collision_checker.hpp
 ┃ ┃ ┃ ┃ ┣ 📜cost_values.hpp
 ┃ ┃ ┃ ┃ ┣ 📜exceptions.hpp
 ┃ ┃ ┃ ┃ ┣ 📜footprint.hpp
 ┃ ┃ ┃ ┃ ┣ 📜footprint_collision_checker.hpp
 ┃ ┃ ┃ ┃ ┣ 📜footprint_subscriber.hpp
 ┃ ┃ ┃ ┃ ┣ 📜inflation_layer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜layer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜layered_costmap.hpp
 ┃ ┃ ┃ ┃ ┣ 📜observation.hpp
 ┃ ┃ ┃ ┃ ┣ 📜observation_buffer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜obstacle_layer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜range_sensor_layer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜static_layer.hpp
 ┃ ┃ ┃ ┃ ┗ 📜voxel_layer.hpp
 ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┣ 📜example.launch
 ┃ ┃ ┃ ┗ 📜example_params.yaml
 ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┣ 📜inflation_layer.cpp
 ┃ ┃ ┃ ┣ 📜obstacle_layer.cpp
 ┃ ┃ ┃ ┣ 📜range_sensor_layer.cpp
 ┃ ┃ ┃ ┣ 📜static_layer.cpp
 ┃ ┃ ┃ ┗ 📜voxel_layer.cpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜array_parser.cpp
 ┃ ┃ ┃ ┣ 📜clear_costmap_service.cpp
 ┃ ┃ ┃ ┣ 📜costmap_2d.cpp
 ┃ ┃ ┃ ┣ 📜costmap_2d_cloud.cpp
 ┃ ┃ ┃ ┣ 📜costmap_2d_markers.cpp
 ┃ ┃ ┃ ┣ 📜costmap_2d_node.cpp
 ┃ ┃ ┃ ┣ 📜costmap_2d_publisher.cpp
 ┃ ┃ ┃ ┣ 📜costmap_2d_ros.cpp
 ┃ ┃ ┃ ┣ 📜costmap_layer.cpp
 ┃ ┃ ┃ ┣ 📜costmap_math.cpp
 ┃ ┃ ┃ ┣ 📜costmap_subscriber.cpp
 ┃ ┃ ┃ ┣ 📜costmap_topic_collision_checker.cpp
 ┃ ┃ ┃ ┣ 📜footprint.cpp
 ┃ ┃ ┃ ┣ 📜footprint_collision_checker.cpp
 ┃ ┃ ┃ ┣ 📜footprint_subscriber.cpp
 ┃ ┃ ┃ ┣ 📜layer.cpp
 ┃ ┃ ┃ ┣ 📜layered_costmap.cpp
 ┃ ┃ ┃ ┗ 📜observation_buffer.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📂integration
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜costmap_tester.cpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_tests_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜footprint_tests.cpp
 ┃ ┃ ┃ ┃ ┣ 📜inflation_tests.cpp
 ┃ ┃ ┃ ┃ ┣ 📜obstacle_tests.cpp
 ┃ ┃ ┃ ┃ ┣ 📜range_tests.cpp
 ┃ ┃ ┃ ┃ ┗ 📜test_costmap_topic_collision_checker.cpp
 ┃ ┃ ┃ ┣ 📂map
 ┃ ┃ ┃ ┃ ┣ 📜TenByTen.pgm
 ┃ ┃ ┃ ┃ ┗ 📜TenByTen.yaml
 ┃ ┃ ┃ ┣ 📂test_launch_files
 ┃ ┃ ┃ ┃ ┗ 📜costmap_map_server.launch.py
 ┃ ┃ ┃ ┣ 📂unit
 ┃ ┃ ┃ ┃ ┣ 📜array_parser_test.cpp
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┗ 📜footprint_collision_checker_test.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜costmap_params.yaml
 ┃ ┃ ┃ ┣ 📜module_tests.cpp
 ┃ ┃ ┃ ┣ 📜simple_driving_test.xml
 ┃ ┃ ┃ ┗ 📜testing_helper.hpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜costmap_plugins.xml
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_dwb_controller
 ┃ ┃ ┣ 📂costmap_queue
 ┃ ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┃ ┗ 📂costmap_queue
 ┃ ┃ ┃ ┃ ┃ ┣ 📜costmap_queue.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜limited_costmap_queue.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜map_based_queue.hpp
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜costmap_queue.cpp
 ┃ ┃ ┃ ┃ ┗ 📜limited_costmap_queue.cpp
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┣ 📜mbq_test.cpp
 ┃ ┃ ┃ ┃ ┗ 📜utest.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┣ 📂dwb_core
 ┃ ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┃ ┗ 📂dwb_core
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dwb_local_planner.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜exceptions.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜illegal_trajectory_tracker.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜publisher.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜trajectory_critic.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜trajectory_generator.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜trajectory_utils.hpp
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜dwb_local_planner.cpp
 ┃ ┃ ┃ ┃ ┣ 📜illegal_trajectory_tracker.cpp
 ┃ ┃ ┃ ┃ ┣ 📜publisher.cpp
 ┃ ┃ ┃ ┃ ┗ 📜trajectory_utils.cpp
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┗ 📜utils_test.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜local_planner_plugin.xml
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┣ 📂dwb_critics
 ┃ ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┃ ┗ 📂dwb_critics
 ┃ ┃ ┃ ┃ ┃ ┣ 📜alignment_util.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜base_obstacle.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜goal_align.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜goal_dist.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜line_iterator.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜map_grid.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜obstacle_footprint.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜oscillation.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜path_align.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜path_dist.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜prefer_forward.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rotate_to_goal.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜twirling.hpp
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜alignment_util.cpp
 ┃ ┃ ┃ ┃ ┣ 📜base_obstacle.cpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_align.cpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_dist.cpp
 ┃ ┃ ┃ ┃ ┣ 📜map_grid.cpp
 ┃ ┃ ┃ ┃ ┣ 📜obstacle_footprint.cpp
 ┃ ┃ ┃ ┃ ┣ 📜oscillation.cpp
 ┃ ┃ ┃ ┃ ┣ 📜path_align.cpp
 ┃ ┃ ┃ ┃ ┣ 📜path_dist.cpp
 ┃ ┃ ┃ ┃ ┣ 📜prefer_forward.cpp
 ┃ ┃ ┃ ┃ ┣ 📜rotate_to_goal.cpp
 ┃ ┃ ┃ ┃ ┗ 📜twirling.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜default_critics.xml
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┣ 📂dwb_msgs
 ┃ ┃ ┃ ┣ 📂msg
 ┃ ┃ ┃ ┃ ┣ 📜CriticScore.msg
 ┃ ┃ ┃ ┃ ┣ 📜LocalPlanEvaluation.msg
 ┃ ┃ ┃ ┃ ┣ 📜Trajectory2D.msg
 ┃ ┃ ┃ ┃ ┗ 📜TrajectoryScore.msg
 ┃ ┃ ┃ ┣ 📂srv
 ┃ ┃ ┃ ┃ ┣ 📜DebugLocalPlan.srv
 ┃ ┃ ┃ ┃ ┣ 📜GenerateTrajectory.srv
 ┃ ┃ ┃ ┃ ┣ 📜GenerateTwists.srv
 ┃ ┃ ┃ ┃ ┣ 📜GetCriticScore.srv
 ┃ ┃ ┃ ┃ ┗ 📜ScoreTrajectory.srv
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┣ 📂dwb_plugins
 ┃ ┃ ┃ ┣ 📂cfg
 ┃ ┃ ┃ ┃ ┗ 📜KinematicParams.cfg
 ┃ ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┃ ┗ 📂dwb_plugins
 ┃ ┃ ┃ ┃ ┃ ┣ 📜kinematic_parameters.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜limited_accel_generator.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜one_d_velocity_iterator.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜standard_traj_generator.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜velocity_iterator.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜xy_theta_iterator.hpp
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜kinematic_parameters.cpp
 ┃ ┃ ┃ ┃ ┣ 📜limited_accel_generator.cpp
 ┃ ┃ ┃ ┃ ┣ 📜standard_traj_generator.cpp
 ┃ ┃ ┃ ┃ ┗ 📜xy_theta_iterator.cpp
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜twist_gen.cpp
 ┃ ┃ ┃ ┃ ┗ 📜velocity_iterator_test.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┃ ┗ 📜plugins.xml
 ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┣ 📜DWB_Structure_Simplified.svg
 ┃ ┃ ┃ ┗ 📜LocalPlanner.svg
 ┃ ┃ ┣ 📂nav2_dwb_controller
 ┃ ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┣ 📂nav_2d_msgs
 ┃ ┃ ┃ ┣ 📂msg
 ┃ ┃ ┃ ┃ ┣ 📜Path2D.msg
 ┃ ┃ ┃ ┃ ┣ 📜Pose2D32.msg
 ┃ ┃ ┃ ┃ ┣ 📜Pose2DStamped.msg
 ┃ ┃ ┃ ┃ ┣ 📜Twist2D.msg
 ┃ ┃ ┃ ┃ ┣ 📜Twist2D32.msg
 ┃ ┃ ┃ ┃ ┗ 📜Twist2DStamped.msg
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┣ 📂nav_2d_utils
 ┃ ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┃ ┗ 📂nav_2d_utils
 ┃ ┃ ┃ ┃ ┃ ┣ 📜conversions.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜odom_subscriber.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parameters.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜path_ops.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜tf_help.hpp
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜conversions.cpp
 ┃ ┃ ┃ ┃ ┣ 📜path_ops.cpp
 ┃ ┃ ┃ ┃ ┗ 📜tf_help.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_lifecycle_manager
 ┃ ┃ ┣ 📂doc
 ┃ ┃ ┃ ┣ 📜diagram_lifecycle_manager.JPG
 ┃ ┃ ┃ ┗ 📜uml_lifecycle_manager.JPG
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_lifecycle_manager
 ┃ ┃ ┃ ┃ ┣ 📜lifecycle_manager.hpp
 ┃ ┃ ┃ ┃ ┗ 📜lifecycle_manager_client.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜lifecycle_manager.cpp
 ┃ ┃ ┃ ┣ 📜lifecycle_manager_client.cpp
 ┃ ┃ ┃ ┗ 📜main.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜launch_lifecycle_test.py
 ┃ ┃ ┃ ┗ 📜test_lifecycle_manager.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_map_server
 ┃ ┃ ┣ 📂cmake_modules
 ┃ ┃ ┃ ┗ 📜FindGRAPHICSMAGICKCPP.cmake
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_map_server
 ┃ ┃ ┃ ┃ ┣ 📜map_io.hpp
 ┃ ┃ ┃ ┃ ┣ 📜map_mode.hpp
 ┃ ┃ ┃ ┃ ┣ 📜map_saver.hpp
 ┃ ┃ ┃ ┃ ┗ 📜map_server.hpp
 ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┗ 📜map_saver_server.launch.py
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📂map_saver
 ┃ ┃ ┃ ┃ ┣ 📜main_cli.cpp
 ┃ ┃ ┃ ┃ ┣ 📜main_server.cpp
 ┃ ┃ ┃ ┃ ┗ 📜map_saver.cpp
 ┃ ┃ ┃ ┣ 📂map_server
 ┃ ┃ ┃ ┃ ┣ 📜main.cpp
 ┃ ┃ ┃ ┃ ┗ 📜map_server.cpp
 ┃ ┃ ┃ ┣ 📜map_io.cpp
 ┃ ┃ ┃ ┗ 📜map_mode.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📂component
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜test_map_saver_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜test_map_saver_node.cpp
 ┃ ┃ ┃ ┃ ┣ 📜test_map_saver_publisher.cpp
 ┃ ┃ ┃ ┃ ┣ 📜test_map_server_launch.py
 ┃ ┃ ┃ ┃ ┗ 📜test_map_server_node.cpp
 ┃ ┃ ┃ ┣ 📂map_saver_cli
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┗ 📜test_map_saver_cli.cpp
 ┃ ┃ ┃ ┣ 📂test_constants
 ┃ ┃ ┃ ┃ ┗ 📜test_constants.h
 ┃ ┃ ┃ ┣ 📂test_launch_files
 ┃ ┃ ┃ ┃ ┣ 📜map_saver_node.launch.py
 ┃ ┃ ┃ ┃ ┗ 📜map_server_node.launch.py
 ┃ ┃ ┃ ┣ 📂unit
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┗ 📜test_map_io.cpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜invalid_image.yaml
 ┃ ┃ ┃ ┣ 📜map_saver_params.yaml
 ┃ ┃ ┃ ┣ 📜map_server_params.yaml
 ┃ ┃ ┃ ┣ 📜testmap.bmp
 ┃ ┃ ┃ ┣ 📜testmap.pgm
 ┃ ┃ ┃ ┣ 📜testmap.png
 ┃ ┃ ┃ ┣ 📜testmap.yaml
 ┃ ┃ ┃ ┗ 📜test_constants.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_msgs
 ┃ ┃ ┣ 📂action
 ┃ ┃ ┃ ┣ 📜BackUp.action
 ┃ ┃ ┃ ┣ 📜ComputePathToPose.action
 ┃ ┃ ┃ ┣ 📜DummyRecovery.action
 ┃ ┃ ┃ ┣ 📜FollowPath.action
 ┃ ┃ ┃ ┣ 📜FollowWaypoints.action
 ┃ ┃ ┃ ┣ 📜NavigateToPose.action
 ┃ ┃ ┃ ┣ 📜Spin.action
 ┃ ┃ ┃ ┗ 📜Wait.action
 ┃ ┃ ┣ 📂msg
 ┃ ┃ ┃ ┣ 📜BehaviorTreeLog.msg
 ┃ ┃ ┃ ┣ 📜BehaviorTreeStatusChange.msg
 ┃ ┃ ┃ ┣ 📜Costmap.msg
 ┃ ┃ ┃ ┣ 📜CostmapMetaData.msg
 ┃ ┃ ┃ ┣ 📜Particle.msg
 ┃ ┃ ┃ ┣ 📜ParticleCloud.msg
 ┃ ┃ ┃ ┗ 📜VoxelGrid.msg
 ┃ ┃ ┣ 📂srv
 ┃ ┃ ┃ ┣ 📜ClearCostmapAroundRobot.srv
 ┃ ┃ ┃ ┣ 📜ClearCostmapExceptRegion.srv
 ┃ ┃ ┃ ┣ 📜ClearEntireCostmap.srv
 ┃ ┃ ┃ ┣ 📜GetCostmap.srv
 ┃ ┃ ┃ ┣ 📜LoadMap.srv
 ┃ ┃ ┃ ┣ 📜ManageLifecycleNodes.srv
 ┃ ┃ ┃ ┗ 📜SaveMap.srv
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_navfn_planner
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_navfn_planner
 ┃ ┃ ┃ ┃ ┣ 📜navfn.hpp
 ┃ ┃ ┃ ┃ ┗ 📜navfn_planner.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜navfn.cpp
 ┃ ┃ ┃ ┗ 📜navfn_planner.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜global_planner_plugin.xml
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_planner
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_planner
 ┃ ┃ ┃ ┃ ┗ 📜planner_server.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜main.cpp
 ┃ ┃ ┃ ┗ 📜planner_server.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_recoveries
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_recoveries
 ┃ ┃ ┃ ┃ ┣ 📜recovery.hpp
 ┃ ┃ ┃ ┃ ┗ 📜recovery_server.hpp
 ┃ ┃ ┣ 📂plugins
 ┃ ┃ ┃ ┣ 📜back_up.cpp
 ┃ ┃ ┃ ┣ 📜back_up.hpp
 ┃ ┃ ┃ ┣ 📜spin.cpp
 ┃ ┃ ┃ ┣ 📜spin.hpp
 ┃ ┃ ┃ ┣ 📜wait.cpp
 ┃ ┃ ┃ ┗ 📜wait.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜main.cpp
 ┃ ┃ ┃ ┗ 📜recovery_server.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜test_recoveries.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┗ 📜recovery_plugin.xml
 ┃ ┣ 📂nav2_regulated_pure_pursuit_controller
 ┃ ┃ ┣ 📂doc
 ┃ ┃ ┃ ┗ 📜lookahead_algorithm.png
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_regulated_pure_pursuit_controller
 ┃ ┃ ┃ ┃ ┗ 📜regulated_pure_pursuit_controller.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┗ 📜regulated_pure_pursuit_controller.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜test_regulated_pp.cpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜nav2_regulated_pure_pursuit_controller.xml
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_rviz_plugins
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_rviz_plugins
 ┃ ┃ ┃ ┃ ┣ 📜goal_common.hpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_pose_updater.hpp
 ┃ ┃ ┃ ┃ ┣ 📜goal_tool.hpp
 ┃ ┃ ┃ ┃ ┣ 📜nav2_panel.hpp
 ┃ ┃ ┃ ┃ ┗ 📜ros_action_qevent.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜goal_tool.cpp
 ┃ ┃ ┃ ┗ 📜nav2_panel.cpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜plugins_description.xml
 ┃ ┣ 📂nav2_system_tests
 ┃ ┃ ┣ 📂maps
 ┃ ┃ ┃ ┣ 📜empty_room.pgm
 ┃ ┃ ┃ ┣ 📜empty_room.png
 ┃ ┃ ┃ ┣ 📜empty_room.yaml
 ┃ ┃ ┃ ┣ 📜map.pgm
 ┃ ┃ ┃ ┣ 📜map.xcf
 ┃ ┃ ┃ ┣ 📜map_circular.pgm
 ┃ ┃ ┃ ┗ 📜map_circular.yaml
 ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┣ 📂dynamic_obstacle
 ┃ ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┃ ┣ 📜model.sdf
 ┃ ┃ ┃ ┃ ┗ 📜README.md
 ┃ ┃ ┃ ┣ 📂dynamic_world
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┗ 📜world.model
 ┃ ┃ ┃ ┣ 📂empty_room
 ┃ ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┃ ┣ 📜model.sdf
 ┃ ┃ ┃ ┃ ┗ 📜README.md
 ┃ ┃ ┃ ┣ 📂turtlebot3_burger
 ┃ ┃ ┃ ┃ ┣ 📂meshes
 ┃ ┃ ┃ ┃ ┃ ┣ 📜burger_base.dae
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lds.dae
 ┃ ┃ ┃ ┃ ┃ ┣ 📜left_tire.dae
 ┃ ┃ ┃ ┃ ┃ ┗ 📜right_tire.dae
 ┃ ┃ ┃ ┃ ┣ 📜model-1_4.sdf
 ┃ ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┃ ┣ 📂turtlebot3_waffle
 ┃ ┃ ┃ ┃ ┣ 📂meshes
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lds.dae
 ┃ ┃ ┃ ┃ ┃ ┣ 📜left_tire.dae
 ┃ ┃ ┃ ┃ ┃ ┣ 📜r200.dae
 ┃ ┃ ┃ ┃ ┃ ┣ 📜right_tire.dae
 ┃ ┃ ┃ ┃ ┃ ┗ 📜waffle_base.dae
 ┃ ┃ ┃ ┃ ┣ 📜model-1_4.sdf
 ┃ ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┃ ┣ 📂turtlebot3_waffle_depth_camera
 ┃ ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┃ ┗ 📂turtlebot3_world
 ┃ ┃ ┃ ┃ ┣ 📂meshes
 ┃ ┃ ┃ ┃ ┃ ┣ 📜hexagon.dae
 ┃ ┃ ┃ ┃ ┃ ┗ 📜wall.dae
 ┃ ┃ ┃ ┃ ┣ 📜model-1_4.sdf
 ┃ ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┣ 📂scripts
 ┃ ┃ ┃ ┗ 📜ctest_loop.bash
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📂dummy_controller
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜dummy_controller.cpp
 ┃ ┃ ┃ ┃ ┣ 📜dummy_controller.hpp
 ┃ ┃ ┃ ┃ ┗ 📜main.cpp
 ┃ ┃ ┃ ┣ 📂dummy_planner
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜dummy_planner.cpp
 ┃ ┃ ┃ ┃ ┣ 📜dummy_planner.hpp
 ┃ ┃ ┃ ┃ ┗ 📜main.cpp
 ┃ ┃ ┃ ┣ 📂localization
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┣ 📜test_localization_launch.py
 ┃ ┃ ┃ ┃ ┗ 📜test_localization_node.cpp
 ┃ ┃ ┃ ┣ 📂planning
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜example_result.png
 ┃ ┃ ┃ ┃ ┣ 📜planner_tester.cpp
 ┃ ┃ ┃ ┃ ┣ 📜planner_tester.hpp
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┣ 📜test_planner_costmaps_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜test_planner_costmaps_node.cpp
 ┃ ┃ ┃ ┃ ┣ 📜test_planner_plugins.cpp
 ┃ ┃ ┃ ┃ ┣ 📜test_planner_random_launch.py
 ┃ ┃ ┃ ┃ ┗ 📜test_planner_random_node.cpp
 ┃ ┃ ┃ ┣ 📂recoveries
 ┃ ┃ ┃ ┃ ┣ 📂backup
 ┃ ┃ ┃ ┃ ┃ ┣ 📜backup_recovery_tester.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜backup_recovery_tester.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_backup_recovery_launch.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_backup_recovery_node.cpp
 ┃ ┃ ┃ ┃ ┣ 📂spin
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜spin_recovery_tester.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜spin_recovery_tester.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_spin_recovery_launch.py
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_spin_recovery_node.cpp
 ┃ ┃ ┃ ┃ ┣ 📂wait
 ┃ ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_wait_recovery_launch.py
 ┃ ┃ ┃ ┃ ┃ ┣ 📜test_wait_recovery_node.cpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wait_recovery_tester.cpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜wait_recovery_tester.hpp
 ┃ ┃ ┃ ┃ ┗ 📜README.md
 ┃ ┃ ┃ ┣ 📂system
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┣ 📜tester_node.py
 ┃ ┃ ┃ ┃ ┣ 📜test_multi_robot_launch.py
 ┃ ┃ ┃ ┃ ┗ 📜test_system_launch.py
 ┃ ┃ ┃ ┣ 📂system_failure
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┣ 📜tester_node.py
 ┃ ┃ ┃ ┃ ┗ 📜test_system_failure_launch.py
 ┃ ┃ ┃ ┣ 📂updown
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┣ 📜start_nav2
 ┃ ┃ ┃ ┃ ┣ 📜test_updown.cpp
 ┃ ┃ ┃ ┃ ┣ 📜test_updown_launch.py
 ┃ ┃ ┃ ┃ ┣ 📜test_updown_reliability
 ┃ ┃ ┃ ┃ ┗ 📜updownresults.py
 ┃ ┃ ┃ ┗ 📂waypoint_follower
 ┃ ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┣ 📜tester.py
 ┃ ┃ ┃ ┃ ┗ 📜test_case_py.launch
 ┃ ┃ ┣ 📂urdf
 ┃ ┃ ┃ ┣ 📜common_properties.urdf
 ┃ ┃ ┃ ┣ 📜turtlebot3_burger.urdf
 ┃ ┃ ┃ ┗ 📜turtlebot3_waffle.urdf
 ┃ ┃ ┣ 📂worlds
 ┃ ┃ ┃ ┣ 📜turtlebot3_ros2_demo.world
 ┃ ┃ ┃ ┣ 📜turtlebot3_ros2_demo_obstacle.world
 ┃ ┃ ┃ ┗ 📜world_only.model
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_util
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_util
 ┃ ┃ ┃ ┃ ┣ 📜clear_entirely_costmap_service_client.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap.hpp
 ┃ ┃ ┃ ┃ ┣ 📜execution_timer.hpp
 ┃ ┃ ┃ ┃ ┣ 📜geometry_utils.hpp
 ┃ ┃ ┃ ┃ ┣ 📜lifecycle_node.hpp
 ┃ ┃ ┃ ┃ ┣ 📜lifecycle_service_client.hpp
 ┃ ┃ ┃ ┃ ┣ 📜lifecycle_utils.hpp
 ┃ ┃ ┃ ┃ ┣ 📜line_iterator.hpp
 ┃ ┃ ┃ ┃ ┣ 📜node_thread.hpp
 ┃ ┃ ┃ ┃ ┣ 📜node_utils.hpp
 ┃ ┃ ┃ ┃ ┣ 📜odometry_utils.hpp
 ┃ ┃ ┃ ┃ ┣ 📜robot_utils.hpp
 ┃ ┃ ┃ ┃ ┣ 📜service_client.hpp
 ┃ ┃ ┃ ┃ ┣ 📜simple_action_server.hpp
 ┃ ┃ ┃ ┃ ┗ 📜string_utils.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜costmap.cpp
 ┃ ┃ ┃ ┣ 📜dump_params.cpp
 ┃ ┃ ┃ ┣ 📜lifecycle_bringup_commandline.cpp
 ┃ ┃ ┃ ┣ 📜lifecycle_node.cpp
 ┃ ┃ ┃ ┣ 📜lifecycle_service_client.cpp
 ┃ ┃ ┃ ┣ 📜lifecycle_utils.cpp
 ┃ ┃ ┃ ┣ 📜node_thread.cpp
 ┃ ┃ ┃ ┣ 📜node_utils.cpp
 ┃ ┃ ┃ ┣ 📜odometry_utils.cpp
 ┃ ┃ ┃ ┣ 📜robot_utils.cpp
 ┃ ┃ ┃ ┗ 📜string_utils.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📂test_dump_params
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_default.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_error.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_help.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_md.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_md_verbose.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_multiple.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_yaml.txt
 ┃ ┃ ┃ ┃ ┣ 📜dump_params_yaml_verbose.txt
 ┃ ┃ ┃ ┃ ┣ 📜test_dump_params_default.test.py
 ┃ ┃ ┃ ┃ ┣ 📜test_dump_params_md.test.py
 ┃ ┃ ┃ ┃ ┣ 📜test_dump_params_multiple.test.py
 ┃ ┃ ┃ ┃ ┣ 📜test_dump_params_node.py
 ┃ ┃ ┃ ┃ ┗ 📜test_dump_params_yaml.test.py
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜test_actions.cpp
 ┃ ┃ ┃ ┣ 📜test_execution_timer.cpp
 ┃ ┃ ┃ ┣ 📜test_geometry_utils.cpp
 ┃ ┃ ┃ ┣ 📜test_lifecycle_cli_node.cpp
 ┃ ┃ ┃ ┣ 📜test_lifecycle_node.cpp
 ┃ ┃ ┃ ┣ 📜test_lifecycle_utils.cpp
 ┃ ┃ ┃ ┣ 📜test_node_utils.cpp
 ┃ ┃ ┃ ┣ 📜test_odometry_utils.cpp
 ┃ ┃ ┃ ┣ 📜test_robot_utils.cpp
 ┃ ┃ ┃ ┣ 📜test_service_client.cpp
 ┃ ┃ ┃ ┗ 📜test_string_utils.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_voxel_grid
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_voxel_grid
 ┃ ┃ ┃ ┃ ┗ 📜voxel_grid.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┗ 📜voxel_grid.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┗ 📜voxel_grid_tests.cpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂nav2_waypoint_follower
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂nav2_waypoint_follower
 ┃ ┃ ┃ ┃ ┗ 📜waypoint_follower.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜main.cpp
 ┃ ┃ ┃ ┗ 📜waypoint_follower.cpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂navigation2
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂smac_planner
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂smac_planner
 ┃ ┃ ┃ ┃ ┣ 📜a_star.hpp
 ┃ ┃ ┃ ┃ ┣ 📜collision_checker.hpp
 ┃ ┃ ┃ ┃ ┣ 📜constants.hpp
 ┃ ┃ ┃ ┃ ┣ 📜costmap_downsampler.hpp
 ┃ ┃ ┃ ┃ ┣ 📜node_2d.hpp
 ┃ ┃ ┃ ┃ ┣ 📜node_basic.hpp
 ┃ ┃ ┃ ┃ ┣ 📜node_se2.hpp
 ┃ ┃ ┃ ┃ ┣ 📜options.hpp
 ┃ ┃ ┃ ┃ ┣ 📜smac_planner.hpp
 ┃ ┃ ┃ ┃ ┣ 📜smac_planner_2d.hpp
 ┃ ┃ ┃ ┃ ┣ 📜smoother.hpp
 ┃ ┃ ┃ ┃ ┣ 📜smoother_cost_function.hpp
 ┃ ┃ ┃ ┃ ┗ 📜types.hpp
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📜a_star.cpp
 ┃ ┃ ┃ ┣ 📜costmap_downsampler.cpp
 ┃ ┃ ┃ ┣ 📜node_2d.cpp
 ┃ ┃ ┃ ┣ 📜node_se2.cpp
 ┃ ┃ ┃ ┣ 📜smac_planner.cpp
 ┃ ┃ ┃ ┗ 📜smac_planner_2d.cpp
 ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┣ 📂deprecated_upsampler
 ┃ ┃ ┃ ┃ ┣ 📜upsampler.hpp
 ┃ ┃ ┃ ┃ ┣ 📜upsampler_cost_function.hpp
 ┃ ┃ ┃ ┃ ┗ 📜upsampler_cost_function_nlls.hpp
 ┃ ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┃ ┣ 📜path.png
 ┃ ┃ ┃ ┣ 📜test_a_star.cpp
 ┃ ┃ ┃ ┣ 📜test_collision_checker.cpp
 ┃ ┃ ┃ ┣ 📜test_costmap_downsampler.cpp
 ┃ ┃ ┃ ┣ 📜test_node2d.cpp
 ┃ ┃ ┃ ┣ 📜test_nodebasic.cpp
 ┃ ┃ ┃ ┣ 📜test_nodese2.cpp
 ┃ ┃ ┃ ┣ 📜test_smac_2d.cpp
 ┃ ┃ ┃ ┣ 📜test_smac_se2.cpp
 ┃ ┃ ┃ ┗ 📜test_smoother.cpp
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┣ 📜smac_plugin.xml
 ┃ ┃ ┗ 📜smac_plugin_2d.xml
 ┃ ┣ 📂tools
 ┃ ┃ ┣ 📜bt2img.py
 ┃ ┃ ┣ 📜build_all.sh
 ┃ ┃ ┣ 📜code_coverage_report.bash
 ┃ ┃ ┣ 📜ctest_retry.bash
 ┃ ┃ ┣ 📜initial_ros_setup.sh
 ┃ ┃ ┣ 📜release.Dockerfile
 ┃ ┃ ┣ 📜ros2_dependencies.repos
 ┃ ┃ ┣ 📜run_sanitizers
 ┃ ┃ ┣ 📜run_test_suite.bash
 ┃ ┃ ┣ 📜skip_keys.txt
 ┃ ┃ ┣ 📜source.Dockerfile
 ┃ ┃ ┗ 📜update_bt_diagrams.bash
 ┃ ┣ 📜.dockerignore
 ┃ ┣ 📜.gitignore
 ┃ ┣ 📜codecov.yml
 ┃ ┣ 📜Dockerfile
 ┃ ┣ 📜Doxyfile
 ┃ ┣ 📜LICENSE
 ┃ ┗ 📜README.md
 ┣ 📂turtlebot3
 ┃ ┣ 📂.github
 ┃ ┃ ┗ 📂workflows
 ┃ ┃ ┃ ┣ 📜lint.yml
 ┃ ┃ ┃ ┗ 📜ros-ci.yml
 ┃ ┣ 📂turtlebot3
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂turtlebot3_bringup
 ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┣ 📜robot.launch.py
 ┃ ┃ ┃ ┣ 📜rviz2.launch.py
 ┃ ┃ ┃ ┗ 📜turtlebot3_state_publisher.launch.py
 ┃ ┃ ┣ 📂param
 ┃ ┃ ┃ ┣ 📜burger.yaml
 ┃ ┃ ┃ ┣ 📜waffle.yaml
 ┃ ┃ ┃ ┗ 📜waffle_pi.yaml
 ┃ ┃ ┣ 📂script
 ┃ ┃ ┃ ┣ 📜99-turtlebot3-cdc.rules
 ┃ ┃ ┃ ┗ 📜create_udev_rules
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂turtlebot3_cartographer
 ┃ ┃ ┣ 📂config
 ┃ ┃ ┃ ┗ 📜turtlebot3_lds_2d.lua
 ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┣ 📜cartographer.launch.py
 ┃ ┃ ┃ ┗ 📜occupancy_grid.launch.py
 ┃ ┃ ┣ 📂rviz
 ┃ ┃ ┃ ┗ 📜tb3_cartographer.rviz
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂turtlebot3_description
 ┃ ┃ ┣ 📂meshes
 ┃ ┃ ┃ ┣ 📂bases
 ┃ ┃ ┃ ┃ ┣ 📜burger_base.stl
 ┃ ┃ ┃ ┃ ┣ 📜waffle_base.stl
 ┃ ┃ ┃ ┃ ┗ 📜waffle_pi_base.stl
 ┃ ┃ ┃ ┗ 📂sensors
 ┃ ┃ ┃ ┃ ┣ 📜astra.dae
 ┃ ┃ ┃ ┃ ┣ 📜astra.jpg
 ┃ ┃ ┃ ┃ ┣ 📜lds.stl
 ┃ ┃ ┃ ┃ ┣ 📜r200.dae
 ┃ ┃ ┃ ┃ ┗ 📜r200.jpg
 ┃ ┃ ┣ 📂rviz
 ┃ ┃ ┃ ┗ 📜model.rviz
 ┃ ┃ ┣ 📂urdf
 ┃ ┃ ┃ ┣ 📜common_properties.urdf
 ┃ ┃ ┃ ┣ 📜turtlebot3_burger.urdf
 ┃ ┃ ┃ ┣ 📜turtlebot3_waffle.urdf
 ┃ ┃ ┃ ┗ 📜turtlebot3_waffle_pi.urdf
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂turtlebot3_example
 ┃ ┃ ┣ 📂resource
 ┃ ┃ ┃ ┗ 📜turtlebot3_example
 ┃ ┃ ┣ 📂turtlebot3_example
 ┃ ┃ ┃ ┣ 📂turtlebot3_obstacle_detection
 ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_obstacle_detection.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂turtlebot3_patrol_client
 ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_patrol_client.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂turtlebot3_patrol_server
 ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_path.py
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_patrol_server.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂turtlebot3_position_control
 ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_path.py
 ┃ ┃ ┃ ┃ ┣ 📜turtlebot3_position_control.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┣ 📜setup.cfg
 ┃ ┃ ┗ 📜setup.py
 ┃ ┣ 📂turtlebot3_navigation2
 ┃ ┃ ┣ 📂launch
 ┃ ┃ ┃ ┗ 📜navigation2.launch.py
 ┃ ┃ ┣ 📂map
 ┃ ┃ ┃ ┣ 📜turtlebot3_world.pgm
 ┃ ┃ ┃ ┗ 📜turtlebot3_world.yaml
 ┃ ┃ ┣ 📂param
 ┃ ┃ ┃ ┣ 📜burger.yaml
 ┃ ┃ ┃ ┣ 📜waffle.yaml
 ┃ ┃ ┃ ┗ 📜waffle_pi.yaml
 ┃ ┃ ┣ 📂rviz
 ┃ ┃ ┃ ┗ 📜tb3_navigation2.rviz
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂turtlebot3_node
 ┃ ┃ ┣ 📂include
 ┃ ┃ ┃ ┗ 📂turtlebot3_node
 ┃ ┃ ┃ ┃ ┣ 📂devices
 ┃ ┃ ┃ ┃ ┃ ┣ 📜devices.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜motor_power.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜reset.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜sound.hpp
 ┃ ┃ ┃ ┃ ┣ 📂sensors
 ┃ ┃ ┃ ┃ ┃ ┣ 📜battery_state.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜imu.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜joint_state.hpp
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sensors.hpp
 ┃ ┃ ┃ ┃ ┃ ┗ 📜sensor_state.hpp
 ┃ ┃ ┃ ┃ ┣ 📜control_table.hpp
 ┃ ┃ ┃ ┃ ┣ 📜diff_drive_controller.hpp
 ┃ ┃ ┃ ┃ ┣ 📜dynamixel_sdk_wrapper.hpp
 ┃ ┃ ┃ ┃ ┣ 📜odometry.hpp
 ┃ ┃ ┃ ┃ ┗ 📜turtlebot3.hpp
 ┃ ┃ ┣ 📂param
 ┃ ┃ ┃ ┣ 📜burger.yaml
 ┃ ┃ ┃ ┣ 📜waffle.yaml
 ┃ ┃ ┃ ┗ 📜waffle_pi.yaml
 ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┣ 📂devices
 ┃ ┃ ┃ ┃ ┣ 📜motor_power.cpp
 ┃ ┃ ┃ ┃ ┣ 📜reset.cpp
 ┃ ┃ ┃ ┃ ┗ 📜sound.cpp
 ┃ ┃ ┃ ┣ 📂sensors
 ┃ ┃ ┃ ┃ ┣ 📜battery_state.cpp
 ┃ ┃ ┃ ┃ ┣ 📜imu.cpp
 ┃ ┃ ┃ ┃ ┣ 📜joint_state.cpp
 ┃ ┃ ┃ ┃ ┗ 📜sensor_state.cpp
 ┃ ┃ ┃ ┣ 📜diff_drive_controller.cpp
 ┃ ┃ ┃ ┣ 📜dynamixel_sdk_wrapper.cpp
 ┃ ┃ ┃ ┣ 📜node_main.cpp
 ┃ ┃ ┃ ┣ 📜odometry.cpp
 ┃ ┃ ┃ ┗ 📜turtlebot3.cpp
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜CMakeLists.txt
 ┃ ┃ ┗ 📜package.xml
 ┃ ┣ 📂turtlebot3_teleop
 ┃ ┃ ┣ 📂resource
 ┃ ┃ ┃ ┗ 📜turtlebot3_teleop
 ┃ ┃ ┣ 📂turtlebot3_teleop
 ┃ ┃ ┃ ┣ 📂script
 ┃ ┃ ┃ ┃ ┣ 📜teleop_keyboard.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜CHANGELOG.rst
 ┃ ┃ ┣ 📜package.xml
 ┃ ┃ ┣ 📜setup.cfg
 ┃ ┃ ┗ 📜setup.py
 ┃ ┣ 📜.gitignore
 ┃ ┣ 📜CONTRIBUTING.md
 ┃ ┣ 📜ISSUE_TEMPLATE.md
 ┃ ┣ 📜LICENSE
 ┃ ┣ 📜README.md
 ┃ ┣ 📜turtlebot3.repos
 ┃ ┗ 📜turtlebot3_ci.repos
 ┗ 📂yolov5
 ┃ ┣ 📂.github
 ┃ ┃ ┣ 📂ISSUE_TEMPLATE
 ┃ ┃ ┃ ┣ 📜bug-report.yml
 ┃ ┃ ┃ ┣ 📜config.yml
 ┃ ┃ ┃ ┣ 📜feature-request.yml
 ┃ ┃ ┃ ┗ 📜question.yml
 ┃ ┃ ┣ 📂workflows
 ┃ ┃ ┃ ┣ 📜ci-testing.yml
 ┃ ┃ ┃ ┣ 📜codeql-analysis.yml
 ┃ ┃ ┃ ┣ 📜docker.yml
 ┃ ┃ ┃ ┣ 📜greetings.yml
 ┃ ┃ ┃ ┣ 📜links.yml
 ┃ ┃ ┃ ┣ 📜stale.yml
 ┃ ┃ ┃ ┗ 📜translate-readme.yml
 ┃ ┃ ┣ 📜dependabot.yml
 ┃ ┃ ┗ 📜PULL_REQUEST_TEMPLATE.md
 ┃ ┣ 📂classify
 ┃ ┃ ┣ 📜predict.py
 ┃ ┃ ┣ 📜train.py
 ┃ ┃ ┣ 📜tutorial.ipynb
 ┃ ┃ ┗ 📜val.py
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📂hyps
 ┃ ┃ ┃ ┣ 📜hyp.no-augmentation.yaml
 ┃ ┃ ┃ ┣ 📜hyp.Objects365.yaml
 ┃ ┃ ┃ ┣ 📜hyp.scratch-high.yaml
 ┃ ┃ ┃ ┣ 📜hyp.scratch-low.yaml
 ┃ ┃ ┃ ┣ 📜hyp.scratch-med.yaml
 ┃ ┃ ┃ ┗ 📜hyp.VOC.yaml
 ┃ ┃ ┣ 📂images
 ┃ ┃ ┃ ┣ 📜bus.jpg
 ┃ ┃ ┃ ┗ 📜zidane.jpg
 ┃ ┃ ┣ 📂scripts
 ┃ ┃ ┃ ┣ 📜download_weights.sh
 ┃ ┃ ┃ ┣ 📜get_coco.sh
 ┃ ┃ ┃ ┣ 📜get_coco128.sh
 ┃ ┃ ┃ ┗ 📜get_imagenet.sh
 ┃ ┃ ┣ 📜Argoverse.yaml
 ┃ ┃ ┣ 📜coco.yaml
 ┃ ┃ ┣ 📜coco128-seg.yaml
 ┃ ┃ ┣ 📜coco128.yaml
 ┃ ┃ ┣ 📜GlobalWheat2020.yaml
 ┃ ┃ ┣ 📜ImageNet.yaml
 ┃ ┃ ┣ 📜Objects365.yaml
 ┃ ┃ ┣ 📜SKU-110K.yaml
 ┃ ┃ ┣ 📜VisDrone.yaml
 ┃ ┃ ┣ 📜VOC.yaml
 ┃ ┃ ┗ 📜xView.yaml
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📂hub
 ┃ ┃ ┃ ┣ 📜anchors.yaml
 ┃ ┃ ┃ ┣ 📜yolov3-spp.yaml
 ┃ ┃ ┃ ┣ 📜yolov3-tiny.yaml
 ┃ ┃ ┃ ┣ 📜yolov3.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-bifpn.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-fpn.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-p2.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-p34.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-p6.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-p7.yaml
 ┃ ┃ ┃ ┣ 📜yolov5-panet.yaml
 ┃ ┃ ┃ ┣ 📜yolov5l6.yaml
 ┃ ┃ ┃ ┣ 📜yolov5m6.yaml
 ┃ ┃ ┃ ┣ 📜yolov5n6.yaml
 ┃ ┃ ┃ ┣ 📜yolov5s-ghost.yaml
 ┃ ┃ ┃ ┣ 📜yolov5s-LeakyReLU.yaml
 ┃ ┃ ┃ ┣ 📜yolov5s-transformer.yaml
 ┃ ┃ ┃ ┣ 📜yolov5s6.yaml
 ┃ ┃ ┃ ┗ 📜yolov5x6.yaml
 ┃ ┃ ┣ 📂segment
 ┃ ┃ ┃ ┣ 📜yolov5l-seg.yaml
 ┃ ┃ ┃ ┣ 📜yolov5m-seg.yaml
 ┃ ┃ ┃ ┣ 📜yolov5n-seg.yaml
 ┃ ┃ ┃ ┣ 📜yolov5s-seg.yaml
 ┃ ┃ ┃ ┗ 📜yolov5x-seg.yaml
 ┃ ┃ ┣ 📜common.py
 ┃ ┃ ┣ 📜experimental.py
 ┃ ┃ ┣ 📜tf.py
 ┃ ┃ ┣ 📜yolo.py
 ┃ ┃ ┣ 📜yolov5l.yaml
 ┃ ┃ ┣ 📜yolov5m.yaml
 ┃ ┃ ┣ 📜yolov5n.yaml
 ┃ ┃ ┣ 📜yolov5s.yaml
 ┃ ┃ ┣ 📜yolov5x.yaml
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂segment
 ┃ ┃ ┣ 📜predict.py
 ┃ ┃ ┣ 📜train.py
 ┃ ┃ ┣ 📜tutorial.ipynb
 ┃ ┃ ┗ 📜val.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 📂aws
 ┃ ┃ ┃ ┣ 📜mime.sh
 ┃ ┃ ┃ ┣ 📜resume.py
 ┃ ┃ ┃ ┣ 📜userdata.sh
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂docker
 ┃ ┃ ┃ ┣ 📜Dockerfile
 ┃ ┃ ┃ ┣ 📜Dockerfile-arm64
 ┃ ┃ ┃ ┗ 📜Dockerfile-cpu
 ┃ ┃ ┣ 📂flask_rest_api
 ┃ ┃ ┃ ┣ 📜example_request.py
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜restapi.py
 ┃ ┃ ┣ 📂google_app_engine
 ┃ ┃ ┃ ┣ 📜additional_requirements.txt
 ┃ ┃ ┃ ┣ 📜app.yaml
 ┃ ┃ ┃ ┗ 📜Dockerfile
 ┃ ┃ ┣ 📂loggers
 ┃ ┃ ┃ ┣ 📂clearml
 ┃ ┃ ┃ ┃ ┣ 📜clearml_utils.py
 ┃ ┃ ┃ ┃ ┣ 📜hpo.py
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂comet
 ┃ ┃ ┃ ┃ ┣ 📜comet_utils.py
 ┃ ┃ ┃ ┃ ┣ 📜hpo.py
 ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂wandb
 ┃ ┃ ┃ ┃ ┣ 📜wandb_utils.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂segment
 ┃ ┃ ┃ ┣ 📜augmentations.py
 ┃ ┃ ┃ ┣ 📜dataloaders.py
 ┃ ┃ ┃ ┣ 📜general.py
 ┃ ┃ ┃ ┣ 📜loss.py
 ┃ ┃ ┃ ┣ 📜metrics.py
 ┃ ┃ ┃ ┣ 📜plots.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜activations.py
 ┃ ┃ ┣ 📜augmentations.py
 ┃ ┃ ┣ 📜autoanchor.py
 ┃ ┃ ┣ 📜autobatch.py
 ┃ ┃ ┣ 📜callbacks.py
 ┃ ┃ ┣ 📜dataloaders.py
 ┃ ┃ ┣ 📜downloads.py
 ┃ ┃ ┣ 📜general.py
 ┃ ┃ ┣ 📜loss.py
 ┃ ┃ ┣ 📜metrics.py
 ┃ ┃ ┣ 📜plots.py
 ┃ ┃ ┣ 📜torch_utils.py
 ┃ ┃ ┣ 📜triton.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜.dockerignore
 ┃ ┣ 📜.gitattributes
 ┃ ┣ 📜.gitignore
 ┃ ┣ 📜.pre-commit-config.yaml
 ┃ ┣ 📜benchmarks.py
 ┃ ┣ 📜CITATION.cff
 ┃ ┣ 📜CONTRIBUTING.md
 ┃ ┣ 📜detect.py
 ┃ ┣ 📜export.py
 ┃ ┣ 📜hubconf.py
 ┃ ┣ 📜LICENSE
 ┃ ┣ 📜README.md
 ┃ ┣ 📜README.zh-CN.md
 ┃ ┣ 📜requirements.txt
 ┃ ┣ 📜setup.cfg
 ┃ ┣ 📜train.py
 ┃ ┣ 📜tutorial.ipynb
 ┃ ┗ 📜val.py
```

## 🌳 시연영상
---

### 집스캔

![집스캔](https://github.com/Hyokiz/Algorithm/assets/109258146/aafd3fc1-1332-41d5-869c-4eb8da8c02ae)

### 집스캔 알람

![집스캔_알람_고화질](https://github.com/Hyokiz/Algorithm/assets/109258146/62749994-39ab-4c49-8686-f7e6e07c3f23)

### 화분 들기

![화분_들기_고화질](https://github.com/Hyokiz/Algorithm/assets/109258146/9f7535d9-4b75-42e6-96fb-02773c6e54cf)

### 물 주기

![물주기](https://github.com/Hyokiz/Algorithm/assets/109258146/eb05d2de-30b7-45fb-8bae-27951cbf27c2)

### 화분 이동

![화분_이동](https://github.com/Hyokiz/Algorithm/assets/109258146/9b3a9167-8326-444c-a55d-8f2195df9ed9)

### 화분 놓기

![화분_놓기](https://github.com/Hyokiz/Algorithm/assets/109258146/1f0ea0fd-adbe-4379-9e97-393ed25a5aad)

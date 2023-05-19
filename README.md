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
 ┣ 📂turtlebot3
 ┗ 📂yolov5
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

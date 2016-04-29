# Android 리소스 자동화
 1. 아이폰은 고려하지 않음

## 작업 환경
1. 파이썬 설치
2. setuptools, pip, gdata 설치
3. AndroidStudio Python Community Edition Plugin 설치


## 구글시트 만들기
1. 참조 시트 원본 : https://docs.google.com/spreadsheets/d/1w-bYDRkDxCKR5eHwWM1FmqZFslkLam7Lp_aoidcDc4U/edit#gid=0

2. 시트 만들기
 - 참조 시트와 같이 F4~H4(한국어, 영어, Android Key)

3. 구글 스크립트 생성
 - 구글시트 -> 도구 -> 스크립트 편집기 복사 붙여넣기(app/script/googleScript.txt)

4. 리소스 만들기
 -  구글시트 -> 도구 -> Android Resource sheet 클릭 (아래와 같이 시트 복사본이 생성됨)
 - 시트 복사본 : https://docs.google.com/spreadsheets/d/1w-bYDRkDxCKR5eHwWM1FmqZFslkLam7Lp_aoidcDc4U/edit#gid=0
 - 복사된 시트는 웹에 공개 필요
 - 웹에 공개 - 인터넷의 모든 사용자가 찾아서 볼 수 있습니다.

5. app/build.gradle (GoogleDocId 추가)
 - 시트 복사본 1XnOlCR6IBIxyHBD6l6uT0zkGACrQtim6nynJvbkbOX0
 - ext.GoogleDocId = '1XnOlCR6IBIxyHBD6l6uT0zkGACrQtim6nynJvbkbOX0#gid=0'

10. 주의
 -


### 참조 사이트
1. 아래 사이트 기반으로 작성함
2. http://tiii.tistory.com/22 (기반으로 작성함)
3. 잔디(JANDI) https://tosslab.github.io/android/2016/02/12/Android-and-automation/

### HISTORY
1. 2016-04-28 최초 작성


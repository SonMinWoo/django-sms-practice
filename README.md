# django-sms-practice
장고 본인인증 로직 구현 연습을 위한 레포지토리입니다.

## 코드설명

django-cors-headers, djangorestframework를 pip install하여 사용함

### tutorial directory

settings.py 
1. INSTALLED_APPS : rest_framework, 'snippets.apps.SnippetsConfig', 'corsheaders' 추가. 각각 post요청 처리, snippet app 추가, cors 요청 처리 담당
2. MIDDLEWARE : 'corsheaders.middleware.CorsMiddleware', 'django.middleware.common.CommonMiddleware', 추가. cors 위해 들어감
3. CORS_ORIGIN_ALLOW_ALL, CORS_ALLOW_CREDENTIALS, CORS_ORIGIN_WHITELIST : cors 허용 관련 옵션

urls.py
path('', include('snippets.urls'))를 이용해 snippets 폴더 내의 urls 파일 내 url 추가

### snippets directory

logic : 요청 시 phone_number라는 key로 들어온 전화번호를 key로 ,랜덤하게 생성된 verify_number를 value로 auth_db라는 dictionary에 저장. 
사용자가 수신한 인증번호를 입력한 후 확인요청을 보내면 auth_db에 저장되어 있는 값과 요청 시 같이 보낸 값을 비교해 동일하면 True를, 다르면 False return.

views.py 
1. auth_post(request) : 문자 발신 요청을 알리고 사이트에 post로 보냄. data dictionary는 알리고에서 요구하는 required data. 
2. verify_post(request) : 사용자가 인증번호를 입력하고 확인 요청을 보내면 이를 받아 값 비교함.

urls.py
1. http://127.0.0.1/auth/에 post 요청시 auth_post 실행.
2. http://127.0.0.1/auth/verify에 post 요청시 verify_post 실행.
# 사용된 라이브러리
 - [pycaw](https://pycaw.readthedocs.io/en/latest/)
<br>└```pip install pycaw```
 - [pywin32](https://pypi.org/project/pywin32/)
<br>└```pip install pywin32```
 - [pyinstaller](https://pyinstaller.org/en/stable/)
<br>└```pip install pyinstaller```
 - json
 - time<br><br>

# 사용 방법
## 매크로 키보드를 사용하시는 분들은<br>```Ctrl + Shift + 0``` 와/과 ```Ctrl + Shift + 9``` 로 소리 크기 조절 키를 바꿔주세요!

 -  ```Ctrl + Shift + 0``` 키를 입력 하여 볼륨을 올립니다.
 -  ```Ctrl + Shift + 9``` 키를 입력 하여 볼륨을 내립니다.<br><br>

# 설치 방법
[여기](https://github.com/Zandura1212/NewSoundControlProgram/releases)를 클릭해 최신 버전의 ```SoundControlProgram.exe``` 와 ```options.json``` 파일을 설치한다.<br><br>

```options.json``` 내의 ```programs``` 와/과 ```volume_lv``` 을/를 변경한다.<br><br>

```programs```에 ```name``` 에는 프로그램의 이름(아무거나 상관 없음) ```p_name``` 에는 프로세서의 이름을 적는다.<br><br>

```volume_lv``` 은/는 볼륨 조정 단계를 정한다.<br>
└ (예) ```50 => 0.5```<br>
└ (예) ```15 => 0.15```<br><br>


**sleep 시간이 낮을 수록 CPU 사용량이 늘어나고, 입력 시간이 줄어듭니다!**

```sleep``` 내의 ```enable``` 은/는 sleep을 활성화 여부를 결정한다.<br>
└ true: 활성화<br>└ false: 비활성화<br>
```sleep``` 내의 ```time``` 은/는 sleep 시간을 결정한다.<br>
└ (예) ```0.1 => 0.1초```<br><br>
└ (예) ```5 => 5초```<br><br>

그 후 ```SoundControlProgram.exe``` 프로그램 파일을 실행한다.<br><br>

# 시작 프로그램
 - ```SoundControlProgram.exe``` 프로그램 파일의 바로가기를 만든다.
 - ```Windows + R``` 키를 눌러 실행을 실행시킨다.
 - ```shell:startup``` 명령어를 실행하여 ```SoundControlProgram.exe``` 프로그램 파일의 바로가기 파일을 집어 넣는다.<br><br>

# NewSoundControlProgram
Made By Zandura1212

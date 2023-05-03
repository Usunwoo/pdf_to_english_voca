# 영어 파일에서 단어 추출해 단어장으로 만들기

## 프로젝트 진행 계기
친구가 국제무역사 자격증 준비를 하는데 자격증 기출문제의 영어지문에서 모르는 영단어가 많아 어려움을 겪고 있었습니다.
그래서 시험에 나온 영단어들을 빠르게 정리해 암기하기 위해 과거 기출문제들에서 영단어를 추출해 단어장으로 만들어보기로 했습니다.

## 프로젝트 설명
우선 시험문제를 가져와 영어 단어만 추출합니다.
그리고 추출한 영단어를 네이버 사전의 단어장에 저장해 공부하려고 합니다. 

## 진행 계획
1. 파일들을 불러온다.
2. pdf 파일을 text로 변환한다.
3. text 파일에서 무역영어 파트만 자르고 전체 파일을 합친다.
4. 정규식을 통해 영어 문장을 제외한 한글, 숫자, 특수문자 등은 제거한다.
6. 문장을 단어별로 나눈 후 전체가 대문자인 것은 삭제한다.(ABC, USD 등)
7. 단어들을 소문자로 변경 후 중복 단어를 제거한다
8. 표제어, 어간을 추출하고 불용어를 제거한다.
9. 셀레니움으로 네이버에 로그인하고 네이버 사전에 접속한다.(자동저장이 켜져 있어야 한다!)
10. 단어장에 있는 단어를 하나씩 검색해서 들어가면 자동으로 추가된다.

## 트러블 슈팅
- pdf파일을 텍스트로 변환할 때 줄바꿈 인식이 제대로 되지 않아 문장의 경계가 불분명해, 표제어 추출과 어간 추출에서 단어의 특성을 반영하지 못해 비슷한 단어의 수가 너무 많아졌다.
    - 자연어 전처리에 대해서 좀 더 공부해야 할 것 같다.
- 셀레니움을 통해 네이버 단어장에 추가할 때, readline()으로 단어파일을 읽어오면 속도가 저하됐다.
    - 단어 개수가 얼마 되지 않으므로 readlines()로 한 번에 다 불러왔더니 속도가 훨씬 증가했다.
- 셀레니움에서 명령 실행이 너무 빨라 가끔씩 코드를 넘어가는 경우가 있었다.
    - 작업 중간중간에 대기시간을 1초정도 넣어줘서 해결했다.
- 단어장에 추가할 때 반복이 길어질수록 속도가 저하되는 문제가 발생했다.

## 결과와 느낀점
결과적으로 단어장 제작에 성공했습니다. 그러나 전처리를 좀 더 잘 했으면 단어의 개수가 많이 줄었을텐데 그 부분이 아쉽고, 셀레니움 코드 속도도 개선시킬 수 있으면 좋을 것 같습니다.

나중에 코드를 좀 더 보완해봐야겠습니다.
import requests
from bs4 import BeautifulSoup

header_user = { "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# 멜론 월간 국내종합 차트 url
url = "https://www.melon.com/chart/month/index.htm?classCd=DM0000"
# 유저인 것처럼 get으로 리소스 요청 -> requests로 넘어오는 내용 req 변수에 저장
req = requests.get(url, headers=header_user)

# 가져온 데이터 텍스트 형태의 자료로 html 변수에 저장
html = req.text
# 컴퓨터가 이해할 수 있는 트리구조로 변경 후 soup 변수에 저장
soup = BeautifulSoup(html, 'html.parser')

# 차트 1~50위 & 51~100위
lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

# 차트 1~100위
lst_all = lst50 + lst100

# num : 순위
num = 1
print(f'\n✨ 국내종합 월간 순위 상승곡 ✨\n')
# 차트 1~100 반복
for i in lst_all :
    # 상승 순위 나타내는 클래스 up 변수 저장
    up = i.select_one('.up')
    # 상승 순위 확인 조건문
    if up :
        # up이 참인 경우, 해당 코드 실행
        title = i.select_one('.ellipsis.rank01 a')
        singer = i.select('.ellipsis.rank02 a')
        album = i.select_one('.ellipsis.rank03 a')

        print(f'[ {num}위 ]\n')
        print(f'▲ {up.text} 순위 상승!\n')
        print(f"제목 : {title.text}\n")
        print(f"앨범 : {album.text}\n")

        # 가수가 여러 명인 경우 출력 조건문
        # 가수가 혼자일 경우
        if len(singer) == 1 :
            # 인덱스[0]인 가수 text로 출력
            print(f'가수 : {singer[0].text}')
        # 가수가 한 명보다 많을 경우
        if len(singer) > 1 :
                # singer 반복 후, text 값을 쉼표(,)로 구분
                # set : 가수명이 중복되길래 중복 제거 함수 사용
                singers = ", ".join(set([s.text for s in singer]))
                print(f'가수 : {singers}')

        # 터미널 읽기 편하게 print문 추가
        print()
        print('-' * 60)
        print()
    
    # 상승곡이 아닐 경우, pass 한다. 
    else:
        pass
    # 순위 하나씩 증가
    num += 1
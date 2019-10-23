
import numpy as np # unique 쓸 거라 넘파이 임포트 해줍니다.
file_fath = input("파일 경로를 입력해 주세요.")
def e_mail(): # 입력에 파일 경로 받아줍니다.    
    try:
        with open(file_fath, 'r', encoding='UTF8') as email: # 파일 경로 열어주고
            data = email.read() # 이메일 주소 입력받고 자동 닫기
        # 패턴(문자열(갯수 상관 없음) + @ + 문자열(갯수 상관없음)+"."없어도 됨+문자열(갯수상관없음))
        pattern = re.compile("\w+[@]\w+[.]?\w+") 
        result = pattern.findall(data) # 패턴을 data에 대입해 찾아줍니다.
        result = np.unique(result) # 찾은 데이터의 중복값을 없애주고, 정렬해 줍니다.
        result = str(result)
        # 파일 생성하는 거 찾아보기

        with open('./email_list.txt', 'w') as el: # 찾은 데이터를 파일로 생성해 줍니다.
            el.write(result)

        return "성공했습니다. 새로운 파일은 현재경로에 email_list.txt로 생성되었습니다."
    except:
        return "파일 생성에 실패하였습니다."

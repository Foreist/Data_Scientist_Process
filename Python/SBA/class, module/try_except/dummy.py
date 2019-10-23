def exception_test4():
    print("[1] Can you add 2 and '2' in python? ")

    try:
        print("[2] Try it~! ", 2 + '2')  # TypeError 발생
    except TypeError:
        print("[2] I got TypeError! Check below! ")  # 에러 메시지 출력
        traceback.print_exc()  # 트레이스백 메시지 출력

    print("[3] It's not possible to add integer and string together. ")


exception_test4()
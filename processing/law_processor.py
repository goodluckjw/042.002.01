def process_search(query, unit):
    # 실제 구현 시 API 호출 + XML 파싱 + 단위별 필터링 적용 예정
    return {
        "공중 등 협박목적 및 대량살상무기확산을 위한 자금조달행위의 금지에 관한 법률": [
            f"🔍 <조문내용>에 '{query}' 포함된 결과입니다.",
            f"🔍 <항내용>에 '{query}' 포함된 결과입니다."
        ]
    }

def process_amendment(find_word, replace_word):
    # 실제 구현 시 XML 본문 분석 + 조항위치 추출 기반 생성
    return [
        f"① 공중 등 협박목적 및 대량살상무기확산을 위한 자금조달행위의 금지에 관한 법률 일부를 다음과 같이 개정한다. 제2조제1항 및 제4항 중 “{find_word}”을 각각 “{replace_word}”로 한다."
    ]
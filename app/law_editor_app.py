import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "processing")))
from law_processor import process_search, process_amendment

st.set_page_config(layout="wide")
st.title("📘 부칙개정 도우미")

with st.expander("ℹ️ 읽어주세요"):
    st.markdown("이 앱은 검색 기능과 개정문 자동생성 기능을 제공합니다.\n- 검색: 법령에서 특정 단어가 포함된 조문을 검색합니다.\n- 개정문 생성: 특정 단어를 다른 단어로 대체하는 부칙 개정문을 생성합니다.")

# --- 검색 기능 UI ---
st.header("🔍 검색 기능")
search_col1, search_col2, search_col3 = st.columns([6, 1, 1])
with search_col1:
    query = st.text_input("검색어 입력", key="query")
with search_col2:
    search_clicked = st.button("검색 시작")
with search_col3:
    reset_clicked = st.button("초기화")

search_unit = st.radio("다중검색 단위선택 (미선택시 법률 단위 필터링)", ["법률", "조", "항", "호", "목"], horizontal=True, index=0)
st.caption("※ 예: '행정 & 기본' → 선택된 단위 내에 두 검색어가 모두 포함될 때 결과 출력")

if search_clicked and query:
    with st.spinner("검색 중입니다..."):
        results = process_search(query, search_unit)
        st.success("검색 완료")
        for law_name, matches in results.items():
            with st.expander(f"📄 {law_name}"):
                for text in matches:
                    st.markdown(f"<div style='padding-left:1em; line-height: 1.8;'>{text}</div>", unsafe_allow_html=True)

# --- 개정문 생성 기능 UI ---
st.header("✏️ 타법개정문 생성")
amend_col1, amend_col2, amend_col3 = st.columns([4, 4, 1])
with amend_col1:
    find_word = st.text_input("찾을 단어", key="find")
with amend_col2:
    replace_word = st.text_input("바꿀 단어", key="replace")
with amend_col3:
    amend_clicked = st.button("개정문 생성")

if amend_clicked and find_word and replace_word:
    with st.spinner("개정문 생성 중..."):
        amendments = process_amendment(find_word, replace_word)
        st.success("생성 완료")
        for amend in amendments:
            st.markdown(f"➤ {amend}")
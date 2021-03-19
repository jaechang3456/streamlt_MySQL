import streamlit as st
import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd
import json

from insert import run_insert
from selects import run_select
from update import run_update
from delete import run_delete

def main():

    st.title('데이터 베이스 다루기')

    menu = ['Home','Insert','Select','Update','Delete']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        st.write('이 앱은 MySQL의 DB와 연동하여, 데이터를 다루는 앱입니다.')       
        st.write('왼쪽의 사이드바에서 선택하세요.')

    elif choice == 'Insert' :
        run_insert()
    elif choice == 'Select' :
        run_select()
    elif choice == 'Update' :
        run_update()
    elif choice == 'Delete' :
        run_delete()

if __name__ == '__main__':
    main()



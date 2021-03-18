import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time


def main():

    name = st.text_input('이름을 입력하세요.')
    date = st.date_input('생년월일을 입력하세요.')
    time = st.time_input('태어난 시간을 입력하세요.')
    date_time = datetime.combine(date, time)
 
    print(date)
    print(time)
    print(date_time)

    if st.button('저장'):

        try :
            # 1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = '1q2w3e4r5t'
            )

            if connection.is_connected() :
                print('연결됨')
                db_info = connection.get_server_info()
                print("MySQL sercer version : ", db_info)

                # 2. 커서를 가져온다
                cursor = connection.cursor()
                print('커서 가져옴')

                # 3. 우리가 원하는거 실행 가능
                query = '''insert into people (name, birthdate, birthtime, birthdt)
                        values (%s, %s, %s, %s);'''

                record = (name, date, time, date_time)
                print(datetime.now())
                
                cursor.execute(query, record)
                connection.commit()

                print('{}개 적용됨'.format(cursor.rowcount))

                # 4. 실행 후 커서에서 결과를 빼낸다.
                # record = cursor.fetchone()
                # print('Connected to db : ', record)

        except Error as e :
            print('디비 관련 에러 발생' , e)

        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')


if __name__ == '__main__' :
    main()
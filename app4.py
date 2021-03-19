import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():

    book_id_list = [ ]

    try :
        connection = mysql.connector.connect(
        host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
        database = 'yhdb',
        user = 'streamlit',
        password = '1q2w3e4r5t'
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary=True)

            query = """ select *
                        from books
                        limit 5; """
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results :
                st.write(row)
                book_id_list.append( row['book_id'] )

    except Error as e :
        print('디비 관련 에러 발생',e)

    finally :
        cursor.close()
        connection.close()
        print('MySQL 커넥션 종료')

    book_id = st.number_input('책 아이디 입력', min_value=book_id_list[0], max_value=book_id_list[-1])
    
    if st.button('실행') :

        try :
            # 1. 커넥터로 부터 커넥션 받기
            connection = mysql.connector.connect(
                host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = '1q2w3e4r5t'
            )

            if connection.is_connected() :
                # 2. 커서 가져오기
                cursor = connection.cursor()
                # 3. 우리가 원하는 동작 실행하기
                query = """ delete from books
                            where book_id = %s ; """

                data = (book_id, )

                cursor.execute(query, data)

                connection.commit()

        except Error as e :
            print('디비 관련 에러 발생' , e)

        finally :
            # 4. 모든 데이터 베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션 닫기
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')

if __name__ == '__main__' :
    main()
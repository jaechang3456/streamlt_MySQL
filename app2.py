import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():

    st.subheader('도서 검색')
    released_year = st.number_input('몇년도 이후의 책을 조회할지 입력하세요.', min_value=1500, max_value=2500)
    pages = st.number_input('몇 페이지 이상의 책을 조회할지 입력하세요.', min_value=0, max_value=1000)

    order = 'asc'
    if st.checkbox('최신순으로 조회 할 경우 선택하세요'):
        order='desc'

    if st.button('조회'):

        try :
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

                cursor = connection.cursor()

                if order == 'asc' :
                    query = '''select title, released_year, pages
                                from books
                                where released_year > %s and pages > %s
                                order by released_year asc;'''

                else :
                    query = '''select title, released_year, pages
                    from books
                    where released_year > %s and pages > %s
                    order by released_year desc;'''

                # released_year = 2005
                # pages = 400

                param = (released_year, pages)

                cursor.execute(query, param)

                print('{}개 적용됨'.format(cursor.rowcount))

                results = cursor.fetchall()
                print(results)
                st.write(results)

                # for data in results:
                #     print(data[1], data[4])

                # cursor = connection.cursor(dictionary=True)
                # cursor.execute(query)
                # result = cursor.fetchall()
                #print(result)

                # for data in results:
                #     print(data['title'], data['released_year'])
                #     st.write(data)

        except Error as e :
            print('디비 관련 에러 발생' , e)

        finally :
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')
        
        

if __name__ == '__main__' :
    main()
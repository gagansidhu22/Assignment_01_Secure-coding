import os
import pymysql
from urllib.request import urlopen
import smtplib
from email.message import EmailMessage
import requests
import logging
logging.basicConfig(level=logging.INFO)


db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS')
}


def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    msg = EmailMessage()
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP('smtp.example.com', 587) as smtp:
        smtp.send_message(msg)

def get_data():
    url = 'https://secure-api.com/get-data'
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def save_to_db(data):
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    cursor.execute(query, (data, "Another Value"))
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def get_data():
    try:
        url = 'https://secure-api.com/get-data'
        data = urlopen(url).read().decode()
        return data
    except Exception as e:
        logging.error("Error fetching data: %s", e)
        return None


if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)

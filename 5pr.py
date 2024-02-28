import pika


# Параметры подключения к удаленному RabbitMQ-серверу
connection_params = pika.ConnectionParameters(
    host='51.250.26.59',
    port=5672,
    virtual_host='/',  # Ваш виртуальный хост (обычно '/')
    credentials=pika.PlainCredentials(username='guest', password='guest123')
)

# Создание соединения
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

queue_name_exclusive = 'ikbo-07_kiselev_exclusive'
channel.queue_declare(queue=queue_name_exclusive, exclusive=True)
print(f'Created exclusive queue: {queue_name_exclusive}')

# Задание 1.2: Создание очереди, сохраняемой при перезапуске сервера RabbitMQ
queue_name_durable = 'ikbo-07_kiselev_durable'
channel.queue_declare(queue=queue_name_durable, durable=True)
print(f'Created durable queue: {queue_name_durable}')

# Задание 1.3: Создание автоудаляемой очереди
queue_name_auto_delete = 'ikbo-07_kiselev_auto_delete'
channel.queue_declare(queue=queue_name_auto_delete, auto_delete=True)
print(f'Created auto-deletable queue: {queue_name_auto_delete}')

connection.close()

# Задание 2.1: Символ для обозначения времени сна: #, Тип обменника: fanout
remote_connection_params = pika.ConnectionParameters(
    host='51.250.26.59',
    port=5672,
    virtual_host='/',  # Ваш виртуальный хост (обычно '/')
    credentials=pika.PlainCredentials(username='guest', password='guest123')
)

connection = pika.BlockingConnection(remote_connection_params)
channel = connection.channel()

exchange_name_fanout = 'sleep_exchange_fanout'
channel.exchange_declare(exchange=exchange_name_fanout, exchange_type='fanout')

message_fanout = '# Message for fanout exchange'
channel.basic_publish(exchange=exchange_name_fanout, routing_key='', body=message_fanout)
print(f'Sent message to fanout exchange: {message_fanout}')

# Задание 2.2: Символ для обозначения времени сна: *, Тип обменника: direct
exchange_name_direct = 'sleep_exchange_direct'
channel.exchange_declare(exchange=exchange_name_direct, exchange_type='direct')

message_direct = '* Message for direct exchange'
channel.basic_publish(exchange=exchange_name_direct, routing_key='sleep', body=message_direct)
print(f'Sent message to direct exchange: {message_direct}')

# Задание 2.3: Символ для обозначения времени сна: -, Тип обменника: topic
exchange_name_topic = 'sleep_exchange_topic'
channel.exchange_declare(exchange=exchange_name_topic, exchange_type='topic')

message_topic = '- Message for topic exchange'
channel.basic_publish(exchange=exchange_name_topic, routing_key='sleep.time', body=message_topic)
print(f'Sent message to topic exchange: {message_topic}')

connection.close()

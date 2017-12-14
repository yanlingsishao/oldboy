#encoding: utf-8
#!/usr/bin/python

import os
import redis
import configparser

__all__=('init', 'get_conn', 'ping', 'clear', 'get', 'put', 'incr', 'decr', 'expire', 'exists', 'pop', 'keys', 'fn')

# redis 连接池
__connection_pool = None
print(os.pat)
class RedisUtil(object):
    def __init__(self):
        CONFIG_FILE = '../conf/config.cfg'
        config = configparser.ConfigParser()
        config.sections()
        config.read(CONFIG_FILE, encoding='utf-8')
        self.__db_host = config['DB_Config']['database_host']
        self.__db_user = config['DB_Config']['database_username']
        self.__db_port = int(config['DB_Config']['database_port'])
        self.__db_database = config['DB_Config']['database_name']
        self.__db_password = config['DB_Config']['database_password']

    def connect(self):
        global __connection_pool
        conn_config = {'host': CONFIG['host'], 'port': CONFIG['port'], 'password': CONFIG['password'],
                       'db': CONFIG['db']}
        __connection_pool = redis.Redis(connection_pool=redis.ConnectionPool(**conn_config))
        res = __connection_pool.ping()
        if not res:
            __connection_pool = None
            logger.error(u"[red]redis 连接异常, 无法连接上！[/red]", extra={'color': True})
            raise RuntimeError(u'无法连接 Redis, 请检查配置信息！')
        return res



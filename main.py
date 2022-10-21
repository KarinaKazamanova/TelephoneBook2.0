import init
import getdata as gd
import logger
format = 'txt'
name, phone, what_to_do = gd.get_data(format)
t_book = {}
t_book = init.action(what_to_do, name, phone, format)
logger.writing_down(format, t_book)
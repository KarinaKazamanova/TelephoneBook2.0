import init
import getdata as gd
import logger


format = 'txt'
n = gd.get_name(format)
p = gd.get_phone(format)
wtd = gd.get_action(format)
init.init(n, p, wtd)
t_book = {}
t_book = init.action(wtd, n, p, format)
logger.writing_down(format, t_book)
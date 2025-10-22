import logging
console_output = logging.StreamHandler()
root_logger = logging.getLogger()
# root_logger.addHandler(console_output)
# root_logger.setLevel(logging.DEBUG)
# příklad přidávání handleru na logger (zachycování zpráv loggeru)

x_logger = logging.getLogger('x')

x_y_logger = logging.getLogger('x.y')
x_z_logger = logging.getLogger('x.z')

root_logger.info('zpráva 1')
x_logger.info('zpráva 2')
x_y_logger.info('zpráva 3')
x_z_logger.info('zpráva 4')

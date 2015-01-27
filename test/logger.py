import logging
import config

g_logger = None

def initLogManager():
    global g_logger
    g_logger = logging.getLogger(config.loger_name)
    g_logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(config.ui_log_path)
    fh.setLevel(config.file_lvl)
    ch = logging.StreamHandler()
    ch.setLevel(config.con_lvl)
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    g_logger.addHandler(fh)
    g_logger.addHandler(ch)

# logLvl 1:debug 2:info 3:warning 4:error
def log(logLvl,logStr):
    global g_logger
    if logLvl == 1:
        g_logger.debug(logStr)
    elif logLvl == 2:
        g_logger.info(logStr)
    elif logLvl == 3:
        g_logger.warning(logStr)
    elif logLvl == 4:
        g_logger.error(logStr)
    else:
        g_logger.info("not define log level error!")
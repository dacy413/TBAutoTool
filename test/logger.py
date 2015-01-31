import logging
import ConfigParser

g_logger = None
g_config = ConfigParser.ConfigParser()

def initLogManager():
    global g_logger,g_config
    g_config.read("config.ini")
    g_logger = logging.getLogger(g_config.get("Log","loger_name"))
    g_logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(g_config.get("Log","ui_log_path"))
    fh.setLevel(int(g_config.get("Log","file_lvl")))
    ch = logging.StreamHandler()
    ch.setLevel(int(g_config.get("Log","con_lvl")))
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
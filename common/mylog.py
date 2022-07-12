import logging
import os
import time
from common.other import get_abs_path
import colorlog


class MyLogger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        log_colors_config = {
            'DEBUG': 'white',  # cyan white
            'INFO': 'cyan',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_blue',
        }
        struct_time = time.localtime(time.time())
        now_time = time.strftime("%Y-%m-%d", struct_time)
        rootpath = get_abs_path(project_name="web_test")
        logs_dir_path = os.path.join(rootpath, "logs")
        info_log_name = time.strftime(f'Pytest_{now_time}.log', time.localtime(time.time()))
        info_log_path = os.path.join(logs_dir_path, info_log_name)
        print("日志输出路径", info_log_path)
        cmd_ch = logging.StreamHandler()
        fh = logging.FileHandler(info_log_path, mode="a", encoding="utf-8")
        # fh = handlers.TimedRotatingFileHandler(filename=info_log_path, when='S', backupCount=100,
        #                                                encoding='utf-8')
        # fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("\n[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%("
                                      "levelname)s]: %(message)s")
        console_formatter = colorlog.ColoredFormatter(
            fmt='\n%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s]'
                ': %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=log_colors_config
        )
        cmd_ch.setFormatter(console_formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(cmd_ch)
        self.logger.addHandler(fh)


logger = MyLogger().logger

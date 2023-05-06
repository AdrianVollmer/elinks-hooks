import logging
import os

import xdg.BaseDirectory


def init_logger():
    log_file = os.path.join(
        xdg.BaseDirectory.save_data_path('elinks_hooks'),
        'elinks.log',
        )

    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(levelname)s %(asctime)s,%(msecs)d %(name)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG,
        )

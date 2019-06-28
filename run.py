# coding=utf-8

"""
程序运行入口
"""

import wechat_avatar
import avatar_mosaic
import os

def run():
    """ 主程序入口"""
    wechat_avatar.run()
    # avatar_mosaic.run("template.jpg", "wechat_mosaic.jpg")
    avatar_mosaic.run(os.getcwd() + "\\wechat\\" + "0.jpg", "wechat_mosaic.jpg", is_big_size=True)


if __name__ == '__main__':
    run()
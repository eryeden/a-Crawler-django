#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import bs4
import re
import subprocess
import psycopg2
import psycopg2.extras
from datetime import datetime as dt
import json



#DB設定
dbhost = '133.130.106.168'
dbname = 'anime'
dbuser = 'ery'
dbpswd = 'biztablet'


#DBのアニメ題名すべてを返す
def get_all_anime_names():
    # Create connection to anime DB

    dbcn = psycopg2.connect("host=" + dbhost + " dbname=" + dbname + " user=" + dbuser + " password=" + dbpswd)
    cur = dbcn.cursor()

    cur.execute("SELECT DISTINCT anime_name FROM anime")
    anime_names = []
    for row in cur:
        anime_names.append(str(row[0]));

    #切断
    cur.close()
    dbcn.close()

    return anime_names;


#ある題名のアニメのすべての話を返す
def get_all_episodes(anime_name):
    # Create connection to anime DB
    dbcn = psycopg2.connect("host=" + dbhost + " dbname=" + dbname + " user=" + dbuser + " password=" + dbpswd)
    cur = dbcn.cursor()

    cur.execute("SELECT anime_description FROM anime WHERE anime_name = (%s)", [str(anime_name)])
    anime_ds = []
    for row in cur:
        anime_ds.append(str(row[0]));
    # 切断
    cur.close()
    dbcn.close()
    return anime_ds

#ある題名のアニメのすべての話を返す + 詳細な情報
def get_all_info_by_anime_name(anime_name):
    # Create connection to anime DB
    dbcn = psycopg2.connect("host=" + dbhost + " dbname=" + dbname + " user=" + dbuser + " password=" + dbpswd)
    cur = dbcn.cursor()

    cur.execute("SELECT anime_description, episode, src_link, links FROM anime WHERE anime_name = (%s)", [str(anime_name)])
    anime_infos = []
    for row in cur:
        links = str(row[3]).split('|')
        links.pop()
        anime_infos.append([str(row[0]), str(row[1]), str(row[2]), links])
    # 切断
    cur.close()
    dbcn.close()
    return anime_infos






















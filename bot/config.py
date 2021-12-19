#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1222651878
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset fast -c:v libx265 -crf 24 -s 1280x720 -tune psnr -b:v 2M -metadata title="IndiAnime"  -metadata:s:v title="IndiAnime - 720p - HEVC"  -metadata:s:a title="IndiAnime"  -map 0:v -c:a aac -b:a 256k -map 0:a -c:s copy -map 0:s? -max_muxing_queue_size 999999 "{}" -y',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/49b803cac3d7eb804d07e.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()

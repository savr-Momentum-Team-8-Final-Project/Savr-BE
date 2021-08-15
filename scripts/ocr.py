import cv2 
import numpy as np

import pytesseract
from pytesseract import Output

import re
import json

img_path = 'r21.png'

def OcrReceipt(img_path):

    img = cv2.imread(img_path)
    ### BGR
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    ### Adding custom options ### this is important 
    custom_config = r'--oem 3 --psm 6'

    string_data = pytesseract.image_to_string(img, config=custom_config)

    receipt_ocr = {}

    splits = string_data.splitlines()

    ### rule: vender name is the first line 
    vender_name = splits[0]

    #### date transfermations 03/4/2021 and only 1 date appear on the receipt **** 
    lines_with_date = []
    for line in splits:
        if re.search(r'/',line):
            lines_with_date.append(line)
        else:lines_with_date 

    if lines_with_date != [] :
        lines_with_date = lines_with_date[0].split(" ")
        date = []
        for item in lines_with_date:
            if "/" in item:
                date.append(item)
        date = date[0]
    else:
        date = []

    ### total 
    lines_with_total = []
    for line in splits:
        if re.search(r'TOTAL',line,flags=re.I):
            lines_with_total.append(line)

    #### biggest number
    prices = []
    for item in lines_with_total:
    ### split the text with space and :
        item=re.split("[' ':$]",item)

    prices.append(float(item[-1]))

    total = max(prices)

    # # # Store the results in the dict
    receipt_ocr['total'] = total
    receipt_ocr['vender'] = vender_name
    receipt_ocr['date'] = date

    receipt_json = json.dumps(receipt_ocr)

    return receipt_json

# print(OcrReceipt('r21.png'))
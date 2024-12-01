#!/usr/bin/env python

# observation.py

import rospy
from sensor_msgs.msg import Image
from PIL import Image as PILImage
import os
# from openai import OpenAI
import json
import base64
import requests

class ImageSaver:
    def __init__(self):
        # rospy.init_node('image_saver_node', anonymous=True)
        
        self.save_dir = './images'  # 修改为你想要保存图像的路径
        self.file_name = 'current.png' 

    def image_callback(self, msg):
        try:
            # 获取图像数据
            image_data = msg.data

            # 创建PIL Image对象
            pil_image = PILImage.frombytes(mode='RGB', size=(msg.width, msg.height), data=image_data)

            # 构造保存路径
             # 使用时间戳作为文件名
            save_path = os.path.join(self.save_dir, self.file_name)

            # 保存图像到文件系统
            pil_image.save(save_path)
            rospy.loginfo(f"Saved image to {save_path}")

            self.image_sub.unregister()
            rospy.loginfo("Stopped saving images.")
            return

        except Exception as e:
            rospy.logerr(f"Error processing image: {str(e)}")

    def run(self):
        self.image_sub = rospy.Subscriber('/l_camera/color/image_raw', Image, self.image_callback)
        print('#run#')


    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def gpt4o_refine(self):

        # 初始化OpenAI客户端
        api_key='YOUR API IS HERE'

        # Getting the base64 string
        base64_image = self.encode_image(self.save_dir+self.file_name)

        # 调用GPT-4 API
        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
        }

        payload = {
        "model": "gpt-4o",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "Please tell me which side of the table the cokecan is closer to, 1. left side, 2. far side, 3. right side 4. close side. the output should be the corresponding number, and the color and shape of the object in json format."
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        
        data = response.json()
        print(data)

        # 获取content中的json字符串
        content = data['choices'][0]['message']['content']

        # 去掉content中的```json\n和\n```，以获取纯json字符串
        json_str = content.strip('```json\n').strip('\n```')

        # 解析json字符串
        parsed_data = json.loads(json_str)

        # 获取found_objects
        # found_objects = parsed_data['cokecan']
        pos = parsed_data['position']
        color = parsed_data['color']
        shape = parsed_data['shape']

        print(pos,color,shape)

        if pos==4:
            print(pos+1)



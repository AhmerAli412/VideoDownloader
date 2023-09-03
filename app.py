# import yt_dlp
# def download_instagram_video(url):
#     ydl_opts = {}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
# instagram_url = input("Enter the Instagram video URL: ")
# download_instagram_video(instagram_url)









# from flask import Flask, request
# from flask_cors import CORS
# import yt_dlp

# app = Flask(__name__)
# CORS(app) 
# @app.route('/download-instagram-video', methods=['POST'])
# def download_instagram_video():
#     video_url = request.json.get('url')

#     ydl_opts = {}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([video_url])

#     return {'message': 'Video downloaded successfully!'}

# if __name__ == '__main__':
#     app.run()








# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import yt_dlp

# app = Flask(__name__)
# CORS(app)

# @app.route('/download-instagram-video', methods=['POST'])
# def download_instagram_video():
#     video_url = request.json.get('url')

#     ydl_opts = {}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([video_url])

#     return jsonify({'message': 'Video downloaded successfully!'})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')











#working
# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import yt_dlp
# import os

# app = Flask(__name__)
# CORS(app)

# @app.route('/download-instagram-video', methods=['POST'])
# def download_instagram_video():
#     video_url = request.json.get('url')
#     ydl_opts = {}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(video_url, download=False)
#         filename = ydl.prepare_filename(info)
#         ydl.download([video_url])

#     return send_from_directory(directory='', filename=filename, as_attachment=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')




#confirm
# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import yt_dlp
# import os
# import cloudinary
# from cloudinary.uploader import upload

# app = Flask(__name__)
# CORS(app)

# cloudinary.config(
#     cloud_name='dqurkmuo2',
#     api_key='252778716182869',
#     api_secret='xVE6CtmPClsvvjjkTP567YxPZmk'
# )

# @app.route('/download-instagram-video', methods=['POST'])
# def download_instagram_video():
#     video_url = request.json.get('url')
#     ydl_opts = {}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(video_url, download=False)
#         filename = ydl.prepare_filename(info)
#         ydl.download([video_url])

#     upload_result = upload(filename, resource_type='video')
#     public_id = upload_result['public_id']
#     video_url = upload_result['secure_url']

#     os.remove(filename)

#     return jsonify({'video_url': video_url, 'public_id': public_id})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')










from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os
import cloudinary
from cloudinary.uploader import upload

app = Flask(__name__)
CORS(app)

cloudinary.config(
    cloud_name='dqurkmuo2',
    api_key='252778716182869',
    api_secret='xVE6CtmPClsvvjjkTP567YxPZmk'
)

@app.route('/download-social-video', methods=['POST'])
def download_instagram_video():
    video_url = request.json.get('url')
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        filename = ydl.prepare_filename(info)
        ydl.download([video_url])

    upload_result = upload(filename, resource_type='video')
    public_id = upload_result['public_id']
    video_url = upload_result['secure_url']

    os.remove(filename)

    return jsonify({'video_url': video_url, 'public_id': public_id})

@app.route('/download-youtube-video', methods=['POST'])
def download_youtube_video():
    video_url = request.json.get('url')
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        filename = ydl.prepare_filename(info)
        ydl.download([video_url])

    upload_result = upload(filename, resource_type='video')
    public_id = upload_result['public_id']
    video_url = upload_result['secure_url']

    os.remove(filename)

    return jsonify({'video_url': video_url, 'public_id': public_id})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

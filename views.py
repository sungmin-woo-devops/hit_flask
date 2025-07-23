import os
from flask import Blueprint, render_template
from map import create_map

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # 지도를 생성하고 static 폴더에 저장
    create_map()

    # index.html 템플릿을 렌더링 (지도는 iframe으로 로드됨)
    return render_template('index.html')


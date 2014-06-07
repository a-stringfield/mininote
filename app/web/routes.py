from flask import Blueprint, render_template

from app.web import web_interface

@web_interface.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html')
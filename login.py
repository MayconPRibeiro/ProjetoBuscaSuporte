from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import conexao_db
from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug import generate_password_hash, check_password_hash
from main import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"
from datetime import datetime
<<<<<<< HEAD
from email.policy import default
=======
>>>>>>> 5cf65cab0257c9d9dbd159eb4f4d6151e551d20a
from apps.app import db


class UserImage(db.Model):
    __tablename__ = "user_images"
    id = db.Column(db.Integer, primary_key=True)
    # user_idはusersテーブルのidカラムを外部キーとして設定する
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    image_path = db.Column(db.String)
    is_detected = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
<<<<<<< HEAD
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class UserImageTag(db.Model):
    __tablename__ = "user_image_tag"
    id = db.Column(db.Integer, primary_key=True)
    user_image_id = db.Column(db.String, db.ForeignKey("user_images.id"))
    tag_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
=======
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
>>>>>>> 5cf65cab0257c9d9dbd159eb4f4d6151e551d20a

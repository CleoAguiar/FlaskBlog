from nose.tools import *
# import unittest
from datetime import datetime, timedelta
from app import app, db
from app.models import User, Post


def setUp():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

def tearDown():
    db.session.remove()
    db.drop_all()

def test_password_hashing():
    u = User(username='susan')
    u.set_password('cat')
    assert_equal(u.check_password('cat'), True)
    assert_equal(u.check_password('dog'), False)

def test_avatar():
    u = User(username='suzan', email='suzan@mail.com')
    assert_equal(u.avatar(128), 'https://www.gravatar.com/avatar/'
                                '831bc7864c819c3ab17bc9199c342905'
                                '?d=identicon&s=128')

def test_follow():
    u1 = User(username='suzan', email='suzan@mail.com')
    u2 = User(username='user', email='user@mail.com')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()
    assert_equal(u1.followed.all(), [])
    assert_equal(u1.followers.all(), [])

    u1.follow(u2)
    db.session.commit()
    assert_equal(u1.is_following(u2), True)
    assert_equal(u1.followed.count(), 1)
    assert_equal(u1.followed.first().username, 'user')
    assert_equal(u2.followers.count(), 1)
    assert_equal(u2.followers.first().username, 'suzan')

    u1.unfollow(u2)
    db.session.commit()
    assert_equal(u1.is_following(u2), False)
    assert_equal(u1.followed.count(), 0)
    assert_equal(u2.followers.count(), 0)

def test_follow_posts():
    # creating 4 users
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    u3 = User(username='mary', email='mary@example.com')
    u4 = User(username='david', email='david@example.com')
    db.session.add_all([u1, u2, u3, u4])

    # creating 4 posts
    now = datetime.utcnow()
    p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
    p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
    p3 = Post(body="post from mary", author=u3,
              timestamp=now + timedelta(seconds=3))
    p4 = Post(body="post from david", author=u4,
              timestamp=now + timedelta(seconds=2))
    db.session.add_all([p1, p2,  p3, p4])
    db.session.commit()

    # setup followers
    u1.follow(u2) # john follows susan
    u1.follow(u4) # john follows david
    u2.follow(u3) # susan follows mary
    u3.follow(u4) # mary follows david
    db.session.commit()

    # check followed posts of each user
    f1 = u1.followed_posts().all()
    f2 = u2.followed_posts().all()
    f3 = u3.followed_posts().all()
    f4 = u4.followed_posts().all()
    assert_equal(f1, [p2, p4, p1])
    assert_equal(f2, [p2, p3])
    assert_equal(f3, [p3, p4])
    assert_equal(f4, [p4])

SYSTEM_VERSION = '2.2.3'

import datetime

from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import users

class Member(db.Model):
    num = db.IntegerProperty(indexed=True)
    auth = db.StringProperty(required=False, indexed=True)
    username = db.StringProperty(required=False, indexed=True)
    username_lower = db.StringProperty(required=False, indexed=True)
    password = db.StringProperty(required=False, indexed=True)
    email = db.StringProperty(required=False, indexed=True)
    website = db.StringProperty(required=False, default='')
    twitter = db.StringProperty(required=False, default='')
    location = db.StringProperty(required=False, default='')
    tagline = db.TextProperty(required=False, default='')
    bio = db.TextProperty(required=False, default='')
    avatar_large_url = db.StringProperty(required=False, indexed=False)
    avatar_normal_url = db.StringProperty(required=False, indexed=False)
    avatar_mini_url = db.StringProperty(required=False, indexed=False)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    last_signin = db.DateTimeProperty()
    
class Counter(db.Model):
    name = db.StringProperty(required=False, indexed=True)
    value = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    last_increased = db.DateTimeProperty(auto_now=True)
    
class Section(db.Model):
    num = db.IntegerProperty(indexed=True)
    name = db.StringProperty(required=False, indexed=True)
    title = db.StringProperty(required=False, indexed=True)
    title_alternative = db.StringProperty(required=False, indexed=True)
    header = db.TextProperty(required=False)
    footer = db.TextProperty(required=False)
    nodes = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    
class Node(db.Model):
    num = db.IntegerProperty(indexed=True)
    section_num = db.IntegerProperty(indexed=True)
    name = db.StringProperty(required=False, indexed=True)
    title = db.StringProperty(required=False, indexed=True)
    title_alternative = db.StringProperty(required=False, indexed=True)
    header = db.TextProperty(required=False)
    footer = db.TextProperty(required=False)
    category = db.StringProperty(required=False, indexed=True)
    topics = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    
class Topic(db.Model):
    num = db.IntegerProperty(indexed=True)
    node = db.ReferenceProperty(Node)
    node_num = db.IntegerProperty(indexed=True)
    node_name = db.StringProperty(required=False, indexed=True)
    node_title = db.StringProperty(required=False, indexed=False)
    member = db.ReferenceProperty(Member)
    member_num = db.IntegerProperty(indexed=True)
    title = db.StringProperty(required=False, indexed=True)
    content = db.TextProperty(required=False)
    content_length = db.IntegerProperty(default=0)
    hits = db.IntegerProperty(default=0)
    replies = db.IntegerProperty(default=0)
    created_by = db.StringProperty(required=False, indexed=True)
    last_reply_by = db.StringProperty(required=False, indexed=True)
    source = db.StringProperty(required=False, indexed=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    last_touched = db.DateTimeProperty()
    
class Reply(db.Model):
    num = db.IntegerProperty(indexed=True)
    topic = db.ReferenceProperty(Topic)
    topic_num = db.IntegerProperty(indexed=True)
    member = db.ReferenceProperty(Member)
    member_num = db.IntegerProperty(indexed=True)
    content = db.TextProperty(required=False)
    source = db.StringProperty(required=False, indexed=True)
    created_by = db.StringProperty(required=False, indexed=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    
class Avatar(db.Model):
    num = db.IntegerProperty(indexed=True)
    name = db.StringProperty(required=False, indexed=True)
    content = db.BlobProperty()
    
class Note(db.Model):
    num = db.IntegerProperty(indexed=True)
    member = db.ReferenceProperty(Member)
    member_num = db.IntegerProperty(indexed=True)
    title = db.StringProperty(required=False, indexed=True)
    content = db.TextProperty(required=False)
    body = db.TextProperty(required=False)
    length = db.IntegerProperty(indexed=False, default=0)
    edits = db.IntegerProperty(indexed=False, default=1)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
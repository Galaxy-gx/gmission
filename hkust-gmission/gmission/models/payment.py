__author__ = 'chenzhao'

from base import *


class CreditPayment(db.Model, BasicModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    credit = db.Column(db.Integer, nullable=False)

    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    hit_id = db.Column(db.Integer, db.ForeignKey('hit.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))

    worker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    worker = db.relationship('User', foreign_keys=worker_id)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    requester = db.relationship('User', foreign_keys=requester_id)

    created_on = db.Column(db.DateTime, default=datetime.datetime.now)



class CreditTransactiont(db.Model, BasicModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    credit = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String, nullable=False)
    money = db.Column(db.DECIMAL, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', foreign_keys=user_id)

    created_on = db.Column(db.DateTime, default=datetime.datetime.now)
